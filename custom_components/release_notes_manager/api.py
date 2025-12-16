"""API endpoints for Release Notes Manager."""
import logging
import json
from pathlib import Path
import shutil
from aiohttp import web
from homeassistant.components.http import HomeAssistantView

_LOGGER = logging.getLogger(__name__)

class ReleaseNotesAPIView(HomeAssistantView):
    """Handle Release Notes API requests."""
    
    url = "/api/release_notes_manager/save"
    name = "api:release_notes_manager:save"
    requires_auth = False  # Keine Auth erforderlich für lokale Nutzung
    
    async def post(self, request):
        """Handle POST request to save release data."""
        try:
            data = await request.json()
            
            if 'data' not in data:
                _LOGGER.error("No data field in request")
                return web.json_response(
                    {"error": "No data provided"},
                    status=400
                )
            
            # Parse release data
            try:
                release_data = json.loads(data['data'])
            except json.JSONDecodeError as e:
                _LOGGER.error("Invalid JSON data: %s", str(e))
                return web.json_response(
                    {"error": f"Invalid JSON: {str(e)}"},
                    status=400
                )
            
            # Get Home Assistant instance
            hass = request.app["hass"]
            
            # Ensure www directory exists
            www_path = Path(hass.config.path("www"))
            www_path.mkdir(parents=True, exist_ok=True)
            
            data_file = www_path / "release_data.json"
            
            # Create backup if file exists
            if data_file.exists():
                backup_file = www_path / "release_data.json.backup"
                try:
                    shutil.copy2(data_file, backup_file)
                    _LOGGER.debug("Created backup: %s", backup_file)
                except Exception as e:
                    _LOGGER.warning("Could not create backup: %s", str(e))
            
            # Write new data
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(release_data, f, ensure_ascii=False, indent=2)
            
            file_size = data_file.stat().st_size
            _LOGGER.info("Release notes saved via API: %s (%d bytes)", data_file, file_size)
            
            return web.json_response({
                "status": "ok",
                "file": str(data_file),
                "size": file_size
            })
            
        except Exception as e:
            _LOGGER.error("Error in API endpoint: %s", str(e))
            import traceback
            _LOGGER.error("Traceback: %s", traceback.format_exc())
            return web.json_response(
                {"error": str(e)},
                status=500
            )
