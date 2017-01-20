import json
import yaml


def json2yaml(inputfile, outputfile):
    '''
    Converts a given json inputfile into a yaml file

    :param inputfile: The path to the json inputfile
    :type inputfile: str
    :param outputfile: The path to the yaml outputfile
    :type outputfile: str

    Returns None
    '''
    with open(inputfile) as f:
        data = json.load(f)

    with open(outputfile, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
