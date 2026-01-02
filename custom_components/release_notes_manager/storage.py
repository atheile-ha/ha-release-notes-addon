"""Storage layer for Release Notes Manager."""
import logging
import json
from pathlib import Path
from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)


class JSONStorage:
    """JSON file-based storage."""
    
    def __init__(self, hass: HomeAssistant):
        """Initialize JSON storage."""
        self._hass = hass
        self._data_file = Path(hass.config.path("www")) / "release_data.json"
        self._cache = None
        self._cache_time = None
        self._cache_duration = timedelta(minutes=5)
        
        # Ensure www directory exists
        self._data_file.parent.mkdir(parents=True, exist_ok=True)
    
    async def get_all_data(self):
        """Get all data."""
        # Check cache first
        if self._cache and self._cache_time:
            if datetime.now() - self._cache_time < self._cache_duration:
                _LOGGER.debug("Returning cached data")
                return self._cache
        
        # Load from file
        try:
            if self._data_file.exists():
                data = await self._hass.async_add_executor_job(
                    self._read_json_file
                )
                self._cache = data
                self._cache_time = datetime.now()
                return data
            else:
                # Return default structure
                default_data = {
                    "releases": [],
                    "knownIssues": [],
                    "categories": self._get_default_categories()
                }
                return default_data
        
        except Exception as e:
            _LOGGER.error("Error loading data: %s", str(e))
            return {
                "releases": [],
                "knownIssues": [],
                "categories": self._get_default_categories()
            }
    
    async def save_all_data(self, data):
        """Save all data."""
        try:
            # Invalidate cache
            self._cache = None
            self._cache_time = None
            
            # Backup existing file
            if self._data_file.exists():
                backup_file = self._data_file.with_suffix('.json.backup')
                await self._hass.async_add_executor_job(
                    self._data_file.rename,
                    backup_file
                )
            
            # Write new data
            await self._hass.async_add_executor_job(
                self._write_json_file,
                data
            )
            
            _LOGGER.info("Data saved successfully")
            return True
        
        except Exception as e:
            _LOGGER.error("Error saving data: %s", str(e))
            return False
    
    def _read_json_file(self):
        """Read JSON file (sync)."""
        with open(self._data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _write_json_file(self, data):
        """Write JSON file (sync)."""
        with open(self._data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _get_default_categories(self):
        """Get default categories."""
        return [
            {"id": "general", "label": "Allgemein", "color": "bg-gray-500"},
            {"id": "heating", "label": "Heizung", "color": "bg-orange-500"},
            {"id": "energy", "label": "Energie", "color": "bg-green-500"},
            {"id": "automation", "label": "Automation", "color": "bg-blue-500"},
            {"id": "device", "label": "Gerät", "color": "bg-purple-500"},
            {"id": "integration", "label": "Integration", "color": "bg-pink-500"},
            {"id": "ui", "label": "UI/UX", "color": "bg-indigo-500"},
            {"id": "performance", "label": "Performance", "color": "bg-yellow-500"},
            {"id": "security", "label": "Sicherheit", "color": "bg-red-500"},
            {"id": "bugfix", "label": "Bugfix", "color": "bg-teal-500"},
            {"id": "breaking", "label": "Breaking Change", "color": "bg-rose-500"}
        ]


def get_storage(hass: HomeAssistant, storage_type: str = 'json'):
    """Get storage instance."""
    if storage_type == 'json':
        return JSONStorage(hass)
    else:
        raise ValueError(f"Unknown storage type: {storage_type}")
