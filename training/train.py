import sys
sys.path.append('..')
import argparse
from ai.embeddings.embeddings_mapper import Embeddings_Mapper
from utils.loaders.loader_mapper import LoaderMapper
from utils.splitters.recursive import RecursiveCharacter_TextSplitter
from utils.vectorstores.deep_lake import DeeplakeDB

def choose_embeddings(model):
    embeddings_mapper = Embeddings_Mapper()
    embeddings = embeddings_mapper.find_model(model)
    return embeddings


def get_files():
    """
    takes an input string "model" that denotes which embeddings model to use(available options in embeddings_mapper)
    """
    parser = argparse.ArgumentParser(description='Training Script')
    parser.add_argument('PDF_paths', nargs='+', type=str, help='Paths to the documents')
    args = parser.parse_args()
    
    files = args.PDF_paths
    return files

def load_and_split(pdf):
    """
    This method takes an input pdf to be loaded and split into chunks
    
    :param pdf: path to training document
    
    :return: split langchain Document objects
    """
    mapper = LoaderMapper()
    loader = mapper.find_loader(pdf)
    data = loader.load()
    # split extracted text(tokenize)
    # split recursively by different characters - starting with "\n\n", then "\n", then " "
    splitter = RecursiveCharacter_TextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    docs = splitter.split_data(data)
    return docs

def embed_and_store(docs):
    """
    This method takes an input list of chunked documents to be embedded and stored
    
    :param docs: list of split langchain Document objects
    """
    # initialize embeddings model to pass in to db
    embeddings = choose_embeddings("openai")
    # initialize vector store, add split docs
    # (db will compute embeddings using embedding model and store in specified path)
    deeplake = DeeplakeDB(store_path='./embeddings_deeplake', embedding_model=embeddings)
    deeplake.add_docs(docs)

def main():
    """
    When file is run, command line takes input file paths separated by spaces. These will be loaded, split, and embedded, then stored.
    """
    docs = get_files()
    split_docs = []
    for doc in docs:
        chunks = load_and_split(doc)
        split_docs.append(chunks)
    
    embed_and_store(split_docs)
    
if __name__=="__main__":
    main()