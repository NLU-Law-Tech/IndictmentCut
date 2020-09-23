from setuptools import setup, setuptools
import os

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="IndictmentCut",  # Replace with your own username
    version="0.0.1",
    author='yao',
    author_email="josiriser@gmail.com",
    description="To cut Indictment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NLU-Law-Tech/IndictmentCut",
    packages=setuptools.find_packages(),
    install_requires=[
        'ckiptagger_interface @ git+https://github.com/p208p2002/ckiptagger_interface@master',
        'ckiptagger @ git+https://github.com/p208p2002/ckiptagger@ckiptagger-tf2.1',
        'gdown'
    ],
    python_requires='>=3.5',
)
