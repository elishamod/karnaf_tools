from setuptools import setup, find_packages
from os.path import join
source_dir = 'src'

setup(
    name="karnaf_tools",
    version="0.0.4",
    packages=[join(source_dir, pkg) for pkg in find_packages(source_dir)],
    install_requires=[
        # List your dependencies here
        "matplotlib",
        "argparse"
    ],
)
