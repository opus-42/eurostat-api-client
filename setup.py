import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eurostat-api-client",
    version="0.1.1",
    author="Emmanuel Bavoux",
    author_email="emmanuel.bavoux@gmail.com",
    description="A simple Eurostat Rest API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opus-42/eurostat-api-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
