from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="DevOS",
    version="0.1 dev",
    author="UNT",
    author_email="unt.official.sup@gmail.com",
    description="Mini console operating system in Python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/UNT-Official/DevOS",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: MIT license",
    ],
)