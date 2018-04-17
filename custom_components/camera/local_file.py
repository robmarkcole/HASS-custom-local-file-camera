"""
Camera that loads a picture from a local file.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/camera.local_file/
"""
import logging
import mimetypes
import os

import voluptuous as vol

from homeassistant.const import CONF_NAME
from homeassistant.components.camera import Camera, PLATFORM_SCHEMA, DOMAIN
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_FILE_PATH = 'file_path'

DEFAULT_NAME = 'Local File'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_FILE_PATH): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Camera that works with local files."""
    file_path = config[CONF_FILE_PATH]

    # check filepath given is readable
    if not os.access(file_path, os.R_OK):
        _LOGGER.warning("Could not read camera %s image from file: %s",
                        config[CONF_NAME], file_path)

    camera = LocalFile(config[CONF_NAME], file_path)

    def update_file_path_service(call):
        """Update the file path."""
        camera.update_file_path(call.data.get("file_path"))
        return True

    hass.services.register(
            DOMAIN, 'update_file_path', update_file_path_service)

    add_devices([camera])


class LocalFile(Camera):
    """Representation of a local file camera."""

    def __init__(self, name, file_path):
        """Initialize Local File Camera component."""
        super().__init__()

        self._name = name
        self._file_path = file_path
        # Set content type of local file
        content, _ = mimetypes.guess_type(file_path)
        if content is not None:
            self.content_type = content

    def camera_image(self):
        """Return image response."""
        try:
            with open(self._file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            _LOGGER.warning("Could not read camera %s image from file: %s",
                            self._name, self._file_path)

    def update_file_path(self, file_path):
        """Update the camera file path."""
        self._file_path = file_path

    @property
    def name(self):
        """Return the name of this camera."""
        return self._name
