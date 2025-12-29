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
        # FIX: mkdir mit korrekten Parametern
        def create_dir():
            www_dest.mkdir(parents=True, exist_ok=True)
        
        await hass.async_add_executor_job(create_dir)
        
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
        
        # FIX: mkdir mit korrekten Parametern
        def create_dir():
            www_path.mkdir(parents=True, exist_ok=True)
        
        await hass.async_add_executor_job(create_dir)
        
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
    
    _LOGGER.info("Setting up Release Notes Manager v0.4.0")
    
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
            data = call.data.get("data")
            if not data:
                _LOGGER.error("No data provided to save")
                return
                
            www_path = Path(hass.config.path("www"))
            data_file = www_path / "release_data.json"
            
            # Create backup before saving
            if data_file.exists():
                backup_file = www_path / "release_data.json.backup"
                await hass.async_add_executor_job(shutil.copy2, data_file, backup_file)
            
            # Write new data
            def write_json():
                with open(data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            
            await hass.async_add_executor_job(write_json)
            
            _LOGGER.info("Successfully saved release data to %s", data_file)
            
        except Exception as e:
            _LOGGER.error("Error saving release data: %s", str(e))
    
    # Register service
    hass.services.async_register(DOMAIN, "save", save_release_data)
    
    # Register API view
    hass.http.register_view(ReleaseNotesAPIView(hass))
    
    _LOGGER.info("Release Notes Manager setup complete")
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
