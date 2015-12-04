import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rapid",
    version = "0.0.3",
    author = "Keshav Gupta",
    author_email = "keshav@keshav.xyz",
    description = ("rapid generates boilerplate code through command line"),
    license = "MIT",
    keywords = ["boilerplate", "cli", "generate" "command line"],
    url = "https://github.com/keshav11/rapid",
    packages=['rapid'],
    download_url='https://github.com/keshav11/rapid/tarball/0.0.3',
    package_data={
        'rapid': [
        'boilerplate/c/*.bp',
        'boilerplate/csharp/*.bp',
        'boilerplate/html/*.bp',
        'boilerplate/cpp/*.bp',
        'boilerplate/empty/*.bp',
        'boilerplate/python/*.bp',
        'boilerplate/java/*.bp'

        ]
    },
      entry_points = {
        'console_scripts': [
            'rapid = rapid.main:main',
        ],
    }
)
