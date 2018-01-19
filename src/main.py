import argparse
import os


class Rapid:

    def __init__(self):
        self.boiler_plate_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'boilerplate'))
        self.supports = list(os.listdir(self.boiler_plate_dir))

    def boilerplate(self, language):
        if language in self.supports:
            dir = os.path.join(self.boiler_plate_dir, language)
            files = os.listdir(dir)
            for walk in os.walk(dir):
                d = walk[0]
                for f in walk[2]:
                    path = os.path.join(d, f)
                    print(path)
                    with open(path, 'r') as file:
                        print(file.read())
        else:
            print('This language is not supported. Please Try from this list.')
            for lang in self.supports:
                print(lang)


def main():
    parser = argparse.ArgumentParser(description='Generates boilerplate code.')
    parser.add_argument('language', help='boilerplate code to be generated')
    args = parser.parse_args()
    rapid = Rapid()
    rapid.boilerplate(args.language)


if __name__ == "__main__":
    main()
