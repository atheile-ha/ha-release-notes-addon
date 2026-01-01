"""
Home Assistant Release Notes Manager v0.4.0

A comprehensive release notes management system with frontend and widget support.
"""
import logging
import os
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "release_notes_manager"
VERSION = "0.4.0"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Release Notes Manager component."""
    _LOGGER.info("Setting up Release Notes Manager v%s", VERSION)
    
    # Register static files
    www_path = Path(hass.config.path("www"))
    release_notes_path = www_path / "release-notes"
    
    # Ensure www/release-notes directory exists
    release_notes_path.mkdir(parents=True, exist_ok=True)
    
    # Copy HTML files if they don't exist
    integration_path = Path(__file__).parent
    
    for filename in ["release-notes.html", "release-notes-widget.html"]:
        source = integration_path / filename
        target = release_notes_path / filename
        
        if source.exists() and not target.exists():
            import shutil
            shutil.copy(source, target)
            _LOGGER.info("Copied %s to www/release-notes/", filename)
    
    _LOGGER.info(
        "Release Notes Manager is ready! "
        "Access at: /local/release-notes/release-notes.html"
    )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
