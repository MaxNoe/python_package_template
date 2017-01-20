import json
import yaml
import tempfile


def test_json2yaml():
    from json2yaml import json2yaml

    with tempfile.NamedTemporaryFile('r') as yaml_file:

        json2yaml('tests/test.json', yaml_file.name)

        data = yaml.load(yaml_file.file)

    assert data == {'a': 'Hello', 'b': 'World'}
