"""REST API endpoints for Release Notes Manager."""
import logging
from aiohttp import web
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

class ReleaseNotesBaseView(HomeAssistantView):
    """Base view for Release Notes API."""
    
    def __init__(self, hass: HomeAssistant, storage, require_token: bool):
        """Initialize base view."""
        self._hass = hass
        self._storage = storage
        self.requires_auth = require_token


class DataView(ReleaseNotesBaseView):
    """Handle /api/release_notes_manager/save - POST to save data."""
    
    url = "/api/release_notes_manager/save"
    name = "api:release_notes_manager:save"
    
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
            
            import json
            data = json.loads(data_str)
            
            # Validate structure
            if not isinstance(data, dict):
                return web.json_response(
                    {"error": "Invalid data structure"},
                    status=400
                )
            
            success = await self._storage.save_all_data(data)
            
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
            _LOGGER.error("Error saving data: %s", str(e))
            return web.json_response(
                {"error": str(e)},
                status=500
            )


def register_api_views(hass: HomeAssistant, storage, require_token: bool = False):
    """Register all API views."""
    views = [
        DataView(hass, storage, require_token),
    ]
    
    for view in views:
        hass.http.register_view(view)
        _LOGGER.info("Registered API view: %s (auth: %s)", view.url, require_token)
