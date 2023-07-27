import sys
sys.path.append('..')
from utils.loaders.loader_mapper import LoaderMapper
from utils.splitters import character, nltk, recursive, tiktoken
import pytest

#difficult to formally compare results of text splitters, so I checked visually that it worked beforehand, and just tested to see that imports work correctly.
mapper = LoaderMapper()
loader = mapper.find_loader('tests/docs/dummy_doc_twinkle.pdf')
data = loader.load()

def test_character():
    splitter = character.Character_TextSplitter(
        separator= "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len,
    )
    split_docs = splitter.split_data(data)
    assert split_docs is not None

def test_ntlk():
    splitter = nltk.NLTK_TextSplitter(chunk_size = 1000)
    split_docs = splitter.split_data(data)
    assert split_docs is not None

def test_recursive():
    splitter = recursive.RecursiveCharacter_TextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    split_docs = splitter.split_data(data)
    assert split_docs is not None

def test_tiktoken():
    splitter = tiktoken.Token_TextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
    )
    split_docs = splitter.split_data(data)
    assert split_docs is not None
