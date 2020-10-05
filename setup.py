import setuptools
import sys
import os
import re
import codecs

if sys.version_info < (3, 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

PACKAGE_DIR = os.path.dirname(__file__)


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(PACKAGE_DIR, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
                             r"^__version__ = ['\"]([^'\"]*)['\"]",
                             version_file,
                             re.M,
                             )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


with open(os.path.join(PACKAGE_DIR, "README.md"), "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="eurostatapiclient",
    version=find_version('eurostatapiclient', '__init__.py'),
    author="Emmanuel Bavoux",
    author_email="emmanuel.bavoux@gmail.com",
    description="A simple Eurostat Rest API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opus-42/eurostat-api-client",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas>=0.23.4',
        'requests>=2.21.0',
    ]
)
