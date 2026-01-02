"""Release Notes Manager Integration v0.4.0"""
import logging
from pathlib import Path
import shutil
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from .storage import get_storage
from .api import register_api_views

_LOGGER = logging.getLogger(__name__)
DOMAIN = "release_notes_manager"
VERSION = "0.4.0"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Release Notes Manager component."""
    
    _LOGGER.info("Setting up Release Notes Manager v%s", VERSION)
    
    # Get configuration
    conf = config.get(DOMAIN, {})
    storage_type = conf.get('storage', 'json')
    require_token = conf.get('require_token', False)
    
    _LOGGER.info("Configuration - Storage: %s, Token required: %s", 
                storage_type, require_token)
    
    # Initialize storage
    storage = get_storage(hass, storage_type)
    
    # Store in hass.data for access from other components
    hass.data[DOMAIN] = {
        'storage': storage,
        'require_token': require_token
    }
    
    # Deploy HTML files
    await deploy_www_files(hass)
    
    # Register API endpoints
    register_api_views(hass, storage, require_token)
    
    _LOGGER.info("Release Notes Manager v%s setup complete", VERSION)
    
    return True


async def deploy_www_files(hass: HomeAssistant) -> bool:
    """Deploy HTML files to www directory with cache-busting."""
    try:
        # Source: custom_components directory
        integration_path = Path(__file__).parent
        
        # Destination: Home Assistant www directory
        www_dest = Path(hass.config.path("www")) / "release-notes"
        
        # Create destination directory
        www_dest.mkdir(parents=True, exist_ok=True)
        
        # Files to copy
        files_to_copy = [
            ('release-notes.html', 'Admin HTML'),
            ('release-notes-widget.html', 'Widget HTML')
        ]
        
        files_copied = 0
        for filename, description in files_to_copy:
            source = integration_path / filename
            target = www_dest / filename
            
            if source.exists():
                # ALWAYS copy (even if exists) to ensure updates
                await hass.async_add_executor_job(shutil.copy2, source, target)
                files_copied += 1
                _LOGGER.info("Deployed %s to www/release-notes/ (updated)", description)
            else:
                _LOGGER.warning("Source file not found: %s", filename)
        
        if files_copied > 0:
            _LOGGER.info(
                "Release Notes Manager v%s deployed %d file(s). "
                "Access at: /local/release-notes/release-notes.html",
                VERSION, files_copied
            )
            return True
        else:
            _LOGGER.warning(
                "No files were copied. Check integration installation."
            )
            return False
            
    except Exception as e:
        _LOGGER.error("Error deploying www files: %s", str(e))
        return False


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
