import json
import yaml


def json2yaml(inputfile, outputfile):
    with open(inputfile) as f:
        data = json.load(f)

    with open(outputfile, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
