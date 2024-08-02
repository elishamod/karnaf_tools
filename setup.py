from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    # packages=find_packages(),
    packages=['src\karnaf_tools'],
    install_requires=[
        # List your dependencies here
        "matplotlib",
        "argparse"
    ],
)
