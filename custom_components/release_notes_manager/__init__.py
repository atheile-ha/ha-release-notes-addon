"""
Home Assistant Release Notes Manager v0.4.2

A comprehensive release notes management system with frontend and widget support.
"""
import logging
import os
from pathlib import Path
import shutil

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "release_notes_manager"
VERSION = "0.4.2"


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Release Notes Manager component."""
    _LOGGER.info("Setting up Release Notes Manager v%s", VERSION)
    
    # Register static files
    www_path = Path(hass.config.path("www"))
    release_notes_path = www_path / "release-notes"
    
    # Ensure www/release-notes directory exists
    release_notes_path.mkdir(parents=True, exist_ok=True)
    
    # Copy HTML files - ALWAYS overwrite to ensure updates are applied
    integration_path = Path(__file__).parent
    
    files_copied = 0
    for filename in ["release-notes.html", "release-notes-widget.html"]:
        source = integration_path / filename
        target = release_notes_path / filename
        
        if source.exists():
            try:
                shutil.copy2(source, target)  # copy2 preserves metadata
                files_copied += 1
                _LOGGER.info("Copied %s to www/release-notes/ (updated)", filename)
            except Exception as e:
                _LOGGER.error("Failed to copy %s: %s", filename, str(e))
        else:
            _LOGGER.warning("Source file not found: %s", filename)
    
    if files_copied > 0:
        _LOGGER.info(
            "Release Notes Manager v%s is ready! "
            "Copied %d file(s). "
            "Access at: /local/release-notes/release-notes.html",
            VERSION,
            files_copied
        )
    else:
        _LOGGER.warning(
            "Release Notes Manager v%s loaded but no files were copied. "
            "Check integration installation.",
            VERSION
        )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
