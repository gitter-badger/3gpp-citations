from distutils.core import setup
from io import open
from os import path

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Martin Isaksson',
    author_email='martin.Isaksson@gmail.com',
    name='3gpp-citations',
    version='0.1dev',
    packages=['standardcitations', ],
    license=open('LICENSE').read(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['bin/3gpp-citations'],
    data_files=[
        ('examples', ['examples/3gpp.bib', 'examples/3gpp_38-series.bib'])],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
