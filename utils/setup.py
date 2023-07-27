from setuptools import setup, find_packages

setup(
    name='utils',
    version='1.0',
    author='Arvin Dinh',
    description='A Python package containing common utility functions such as pdf reading, loading, and splitting into chunks',
    packages=find_packages(),
    install_requires=['langchain',
                      'pytest',
                      'pymupdf',
                      'unstructured',
                      'tiktoken',
                      'sentence_transformers',
                      'openai',
                      'deeplake'
                     ]
)
