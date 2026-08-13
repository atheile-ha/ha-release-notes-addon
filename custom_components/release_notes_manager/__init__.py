"""Release Notes Manager Integration - HA-konform modernisiert."""
import logging
from pathlib import Path
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.http import StaticPathConfig

from .storage import get_storage
from .api import register_api_views

_LOGGER = logging.getLogger(__name__)
DOMAIN = "release_notes_manager"

# Drei unabhängige Versionsstände. Jede Konstante wird NUR erhöht, wenn an der
# jeweiligen Datei tatsächlich etwas geändert wurde - nicht automatisch bei
# jedem Release. manifest.json/hacs.json führen zusätzlich die übergreifende
# Paket-/Release-Version (für HACS), die von diesen dreien unabhängig ist.
BACKEND_VERSION = "0.5.2"   # __init__.py, api.py, storage.py
ADMIN_VERSION = "0.5.4"     # release-notes.html (Eingabe-Dashboard)
WIDGET_VERSION = "0.5.3"    # release-notes-widget.html (Read-only-Dashboard)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """
    Set up the Release Notes Manager component.
    """

    _LOGGER.info("Setting up Release Notes Manager (Backend v%s)", BACKEND_VERSION)

    # Initialize HA-Storage (with automatic migration)
    storage = get_storage(hass)

    # Trigger migration by loading data once
    # Migration happens transparently in storage.async_load()
    await storage.async_load()

    # Store in hass.data for access from API
    hass.data[DOMAIN] = {
        'storage': storage,
    }

    # Register static frontend assets (served from integration)
    await async_register_static_paths(hass)

    # Register API endpoints
    register_api_views(hass, storage, {
        "backend": BACKEND_VERSION,
        "admin": ADMIN_VERSION,
        "widget": WIDGET_VERSION,
    })

    _LOGGER.info("Release Notes Manager setup complete (Backend v%s)", BACKEND_VERSION)
    _LOGGER.info(
        "Access Admin at: /release-notes/release-notes.html"
    )
    _LOGGER.info(
        "Access Widget at: /release-notes/release-notes-widget.html"
    )
    
    return True


async def async_register_static_paths(hass: HomeAssistant) -> None:
    """
    Register static frontend assets to be served by HA HTTP server.
    
    Technical Decision: StaticPathConfig vs Panel
    - StaticPathConfig chosen because:
      * Simple file serving without HA sidebar integration
      * Allows direct URL access (/release-notes/...)
      * No need for panel registration (sidebar clutter)
      * Compatible with iframe dashboard cards
      * Follows HA best practice for custom frontend assets
    
    Assets are served directly from integration directory:
    - /release-notes/release-notes.html (Admin)
    - /release-notes/release-notes-widget.html (Widget)
    
    No files are copied to /config/www anymore.
    """
    integration_path = Path(__file__).parent
    
    # Register static path for frontend assets
    await hass.http.async_register_static_paths([
        StaticPathConfig(
            url_path="/release-notes",
            path=str(integration_path),
            cache_headers=False  # Always serve latest version (no cache)
        )
    ])
    
    _LOGGER.info(
        "Frontend assets registered: /release-notes/ → %s",
        integration_path
    )


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry (future use)."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry (future use)."""
    return True
