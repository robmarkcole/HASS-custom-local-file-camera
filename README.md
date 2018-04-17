# HASS-custom-local-file-camera
Fork of the [local_file](https://www.home-assistant.io/components/camera.local_file/) camera adding new services. Place the custom_components folder in your configuration directory (or add its contents to an existing custom_components folder). 

Adds the service `camera.update_file_path`. Call with:
```yaml
{
"file_path":"new_file_path"
}
```
the image at `new_file_path` will then be displayed.
