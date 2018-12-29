import setuptools
import sys
import os

if sys.version_info < (3, 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

PACKAGE_DIR = os.path.dirname(__file__)

with open(os.path.join(PACKAGE_DIR, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eurostatapiclient",
    version="0.2.1",
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
        'pandas==0.23.4',
        'requests==2.21.0',
    ]
)
