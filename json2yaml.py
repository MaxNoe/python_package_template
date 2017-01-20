import json
import yaml


with open('my_json_file.json') as f:
    data = json.load(f)

with open('my_yaml_file.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
