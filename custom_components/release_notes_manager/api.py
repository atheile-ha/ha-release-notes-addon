"""REST API endpoints for Release Notes Manager v0.5.0."""
import logging
import json
from aiohttp import web
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class ReleaseNotesVersionView(HomeAssistantView):
    """
    Handle /api/release_notes_manager/version
    - GET to get current backend version
    
    Used by frontend for auto-reload on version mismatch.
    """
    
    url = "/api/release_notes_manager/version"
    name = "api:release_notes_manager:version"
    requires_auth = False  # Local-only usage
    
    def __init__(self, hass: HomeAssistant, version: str):
        """Initialize view."""
        self._hass = hass
        self._version = version
    
    async def get(self, request):
        """Return current backend version."""
        return web.json_response({
            "version": self._version
        }, headers={
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        })


class ReleaseNotesDataView(HomeAssistantView):
    """
    Handle /api/release_notes_manager/data
    - GET to load data
    - POST to save data
    
    Changed in v0.5.0: Uses HA-Storage instead of direct file access.
    """
    
    url = "/api/release_notes_manager/data"
    name = "api:release_notes_manager:data"
    requires_auth = False  # Local-only usage
    
    def __init__(self, hass: HomeAssistant, storage):
        """Initialize view."""
        self._hass = hass
        self._storage = storage
    
    async def get(self, request):
        """Load all data from HA-Storage."""
        try:
            data = await self._storage.async_load()
            
            # Return data with CORS headers for local access
            return web.json_response(data, headers={
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache',
                'Expires': '0'
            })
        
        except Exception as e:
            _LOGGER.error("Error loading data: %s", str(e))
            return web.json_response(
                {"error": str(e)},
                status=500
            )
    
    async def post(self, request):
        """Save all data (bulk update)."""
        try:
            body = await request.json()
            data_str = body.get('data')
            
            if not data_str:
                return web.json_response(
                    {"error": "Missing 'data' in request"},
                    status=400
                )
            
            # Parse release data
            try:
                data = json.loads(data_str)
            except json.JSONDecodeError as e:
                _LOGGER.error("Invalid JSON data: %s", str(e))
                return web.json_response(
                    {"error": f"Invalid JSON: {str(e)}"},
                    status=400
                )
            
            # Validate structure
            if not isinstance(data, dict):
                return web.json_response(
                    {"error": "Invalid data structure"},
                    status=400
                )
            
            # Save to HA-Storage
            success = await self._storage.async_save(data)
            
            if success:
                return web.json_response({
                    "status": "saved",
                    "releases": len(data.get('releases', [])),
                    "knownIssues": len(data.get('knownIssues', [])),
                    "categories": len(data.get('categories', []))
                })
            else:
                return web.json_response(
                    {"error": "Failed to save data"},
                    status=500
                )
        
        except Exception as e:
            _LOGGER.error("Error in API endpoint: %s", str(e))
            return web.json_response(
                {"error": str(e)},
                status=500
            )


def register_api_views(hass: HomeAssistant, storage, version: str) -> None:
    """
    Register all API views.
    
    Changed in v0.5.0: 
    - Removed require_token parameter (always False for local use)
    - Added GET endpoint for data loading
    
    Changed in v0.5.1:
    - Added version endpoint for auto-reload
    """
    # Data endpoint
    data_view = ReleaseNotesDataView(hass, storage)
    hass.http.register_view(data_view)
    _LOGGER.info("Registered API view: %s (GET + POST)", data_view.url)
    
    # Version endpoint
    version_view = ReleaseNotesVersionView(hass, version)
    hass.http.register_view(version_view)
    _LOGGER.info("Registered API view: %s (GET)", version_view.url)
