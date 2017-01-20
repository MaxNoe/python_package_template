from .json2yaml import json2yaml
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')


def main():
    args = parser.parse_args()

    json2yaml(args.inputfile, args.outputfile)


if __name__ == '__main__':
    main()
