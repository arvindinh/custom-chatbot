from setuptools import setup, find_packages

setup(
    name='ai',
    version='1.0',
    author='Arvin Dinh',
    description='A Python package containing LLM model implementation for embedding models, chat models',
    packages=find_packages(),
    install_requires=['langchain=0.0.200',
                      'openai=0.27.8',
                      'sentence-transformers=2.2.2'
                     ]
)
