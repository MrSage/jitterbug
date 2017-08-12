import json
import pkg_resources

resource_package = __name__  # Could be any module/package name
resource_path = '/'.join(('static', 'plugins.json'))

preset_map = json.loads(pkg_resources.resource_string(resource_package, resource_path))