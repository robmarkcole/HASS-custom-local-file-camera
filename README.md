# HASS-custom-local-file-camera
Fork of the [local_file](https://www.home-assistant.io/components/camera.local_file/) camera adding a new service to update the file shown by the camera.

Place the custom_components folder in your configuration directory (or add its contents to an existing custom_components folder).

Adds the service `camera.update_file_path`. Call with:
```yaml
{
"file_path":"/Users/robincole/Pictures/me.jpg"
}
```
the image at `file_path` will then be displayed if a valid file.

Example automation when [folder_watcher](https://www.home-assistant.io/components/folder_watcher/) detects a new image, display it using the local_file camera:
```yaml
- action:
    data_template:
      file_path: " {{ trigger.event.data.path }} "
    entity_id: camera.local_file
    service: camera.update_file_path
  alias: Display new image
  condition: []
  id: '1520092824633'
  trigger:
  - event_data: {"event_type":"created"}
    event_type: folder_watcher
    platform: event
```
