import argparse

parser = argparse.ArgumentParser(description='Generates boilerplate code.')
parser.add_argument('language', help='boilerplate code to be generated')

args = parser.parse_args()

supports = ['html', 'java', 'csharp'];
data_loc = 'boilerplate'

def _boilerplate(name):
    if name in supports:
        with open(data_loc +'/'+ name +'/' + 'code', 'r') as file:
            print file.read()
    else:
        print 'This language is not supported. Please Try from this list.'
        for l in supports:
            print l


def main():
    _boilerplate(args.language)

if __name__ == "__main__":
    main()
