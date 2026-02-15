from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme = file.read()

setup(
    name="marzpy",
    version="0.4.0",
    author="Mewhrzad, Awake",
    description="a simple application with python to manage Marzban panel",
    long_description="text/markdown",
    url="https://github.com/oAwake/marzpy",
    keywords=["marzpy", "Marzban", "Gozargah", "Marzban python", "Marzban API"],
    packages=find_packages(),
    ins=["requests"],
    classifiers=["Programming Language :: Python :: 3"],
)
