"""Release Notes Manager Integration."""
import logging
import json
import os
import shutil
from pathlib import Path
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from .api import ReleaseNotesAPIView

_LOGGER = logging.getLogger(__name__)
DOMAIN = "release_notes_manager"

async def copy_www_files(hass: HomeAssistant) -> bool:
    """Copy HTML files to www directory."""
    try:
        # Source: custom_components directory
        integration_path = Path(__file__).parent
        www_source = integration_path / "www"
        
        # Destination: Home Assistant www directory
        www_dest = Path(hass.config.path("www")) / "release-notes"
        
        # Create destination directory (blocking call in executor)
        await hass.async_add_executor_job(www_dest.mkdir, True, True)
        
        # Copy files if source exists
        if www_source.exists():
            for file in www_source.glob("*.html"):
                dest_file = www_dest / file.name
                # Use executor for blocking I/O
                await hass.async_add_executor_job(shutil.copy2, file, dest_file)
                _LOGGER.info("Copied %s to %s", file.name, dest_file)
            return True
        else:
            _LOGGER.warning("Source www directory not found at %s", www_source)
            return False
            
    except Exception as e:
        _LOGGER.error("Error copying www files: %s", str(e))
        return False

async def initialize_data_file(hass: HomeAssistant) -> None:
    """Initialize release_data.json if it doesn't exist."""
    try:
        www_path = Path(hass.config.path("www"))
        await hass.async_add_executor_job(www_path.mkdir, True, True)
        
        data_file = www_path / "release_data.json"
        
        # Only create if doesn't exist (preserve existing data!)
        if not data_file.exists():
            _LOGGER.info("Creating initial release_data.json")
            initial_data = {
                "releases": [],
                "knownIssues": [],
                "categories": [
                    {"id": "general", "label": "Allgemein", "color": "bg-gray-100 text-gray-800"},
                    {"id": "heating", "label": "Heizung", "color": "bg-orange-100 text-orange-800"},
                    {"id": "energy", "label": "Energie", "color": "bg-green-100 text-green-800"},
                    {"id": "automation", "label": "Automation", "color": "bg-blue-100 text-blue-800"},
                    {"id": "device", "label": "Gerät", "color": "bg-purple-100 text-purple-800"},
                    {"id": "integration", "label": "Integration", "color": "bg-pink-100 text-pink-800"}
                ],
                "lastUpdate": None
            }
            
            # Write file in executor
            def write_json():
                with open(data_file, 'w', encoding='utf-8') as f:
                    json.dump(initial_data, f, ensure_ascii=False, indent=2)
            
            await hass.async_add_executor_job(write_json)
            
            _LOGGER.info("Successfully created %s", data_file)
        else:
            _LOGGER.info("release_data.json already exists, preserving existing data")
            
    except Exception as e:
        _LOGGER.error("Error initializing data file: %s", str(e))

async def create_backup(hass: HomeAssistant) -> bool:
    """Create backup of existing release_data.json before updates."""
    try:
        www_path = Path(hass.config.path("www"))
        data_file = www_path / "release_data.json"
        
        if data_file.exists():
            backup_file = www_path / "release_data.json.backup"
            
            # Use executor for blocking I/O
            await hass.async_add_executor_job(shutil.copy2, data_file, backup_file)
            
            _LOGGER.info("Created backup: %s", backup_file)
            return True
        return False
        
    except Exception as e:
        _LOGGER.error("Error creating backup: %s", str(e))
        return False

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Release Notes Manager component."""
    
    _LOGGER.info("Setting up Release Notes Manager v0.2.3")
    
    # Create backup of existing data before any changes
    await create_backup(hass)
    
    # Copy HTML files to www directory on startup (always update to latest version)
    if await copy_www_files(hass):
        _LOGGER.info("HTML files successfully deployed to /config/www/release-notes/")
    
    # Initialize data file if it doesn't exist (preserves existing data)
    await initialize_data_file(hass)
    
    async def save_release_data(call: ServiceCall) -> None:
        """Save release data to JSON file."""
        try:
            data_str = call.data.get('data')
            
            if not data_str:
                _LOGGER.error("No data provided to save_release_data service")
                return
            
            # Parse JSON
            try:
                release_data = json.loads(data_str)
            except json.JSONDecodeError as e:
                _LOGGER.error("Invalid JSON data: %s", str(e))
                return
            
            # Ensure www directory exists
            www_path = Path(hass.config.path("www"))
            www_path.mkdir(parents=True, exist_ok=True)
            
            # Create backup before saving
            data_file = www_path / "release_data.json"
            if data_file.exists():
                backup_file = www_path / "release_data.json.backup"
                try:
                    shutil.copy2(data_file, backup_file)
                    _LOGGER.debug("Created backup: %s", backup_file)
                except Exception as e:
                    _LOGGER.warning("Could not create backup: %s", str(e))
            
            # Save to file
            try:
                with open(data_file, 'w', encoding='utf-8') as f:
                    json.dump(release_data, f, ensure_ascii=False, indent=2)
                
                _LOGGER.info("Release notes saved successfully to %s", data_file)
                
                # Verify file was written
                if data_file.exists():
                    file_size = data_file.stat().st_size
                    _LOGGER.info("File size: %d bytes", file_size)
                else:
                    _LOGGER.error("File was not created!")
                    
            except PermissionError as e:
                _LOGGER.error("Permission denied writing to %s: %s", data_file, str(e))
            except Exception as e:
                _LOGGER.error("Error writing file: %s", str(e))
            
        except Exception as e:
            _LOGGER.error("Error in save_release_data: %s", str(e))
            import traceback
            _LOGGER.error("Traceback: %s", traceback.format_exc())
    
    hass.services.async_register(DOMAIN, "save_release_data", save_release_data)
    
    # Register API endpoint (no auth required for local access)
    hass.http.register_view(ReleaseNotesAPIView())
    _LOGGER.info("API endpoint registered: /api/release_notes_manager/save")
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
