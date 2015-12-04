import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rapid",
    version = "0.0.1",
    author = "Keshav Gupta",
    author_email = "keshav@keshav.xyz",
    description = ("rapid generates boilerplate code through command line"),
    license = "MIT",
    keywords = ["boilerplate", "cli", "generate" "command line"],
    url = "https://github.com/keshav11/rapid",
    packages=['rapid'],
    long_description=read('README.md'),
    download_url='https://github.com/keshav11/rapid/tarball/0.0.1',
    package_data={
        'rapid': [
        'boilerplate/c/*.bp',
        'boilerplate/csharp/*.bp',
        'boilerplate/html/*.bp',
        'boilerplate/java/*.bp'
        ]
    },
      entry_points = {
        'console_scripts': [
            'rapid = rapid.main:main',
        ],
    }
)
