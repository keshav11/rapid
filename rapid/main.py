import argparse
import os

parser = argparse.ArgumentParser(description='Generates boilerplate code.')
parser.add_argument('language', help='boilerplate code to be generated')    

args = parser.parse_args()

supports = ['html', 'java', 'csharp', 'c', 'cpp', 'empty', 'python'];

_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
_BOILERPLATE_DIR = os.path.join(_ROOT_DIR, 'boilerplate')

def _boilerplate(name):
    if name in supports:
        file_loc = os.path.join(_BOILERPLATE_DIR, name,'code.bp')
        with open(file_loc, 'r') as file:
            print file.read()
    else:
        print 'This language is not supported. Please Try from this list.'
        for l in supports:
            print l


def main():
    _boilerplate(args.language)

if __name__ == "__main__":
    main()
