from setuptools import setup, find_packages

setup(
    name="pdtext",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    author="Neal Caren",
    author_email="neal.caren@gmail.com",
    description=("Helper functions for working with text in pandas"),
    license="BSD",
    keywords="pandas",
    url="https://github.com/nealcaren/pdtext",
)
