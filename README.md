# HASS-custom-local-file-camera
Place the `custom_components` folder in your configuration directory (or add its contents to an existing custom_components folder).

Fork of the [local_file](https://www.home-assistant.io/components/camera.local_file/) camera adding the service `camera.local_file_update_file_path` which updates the image displayed by the camera. The service can be called using the `SERVICES` tool with:
```
{
  "entity_id": "camera.local_file",
  "file_path":"/Users/robincole/Pictures/me.jpg"
}
```

An example automation to display new images detected by the [folder_watcher](https://www.home-assistant.io/components/folder_watcher/) component is:

```yaml
- action:
    data_template:
      file_path: ' {{ trigger.event.data.path }} '
    entity_id: camera.local_file
    service: camera.update_file_path
  alias: Display new image
  condition: []
  id: '1520092824633'
  trigger:
  - event_data:
      event_type: created
    event_type: folder_watcher
    platform: event
```
