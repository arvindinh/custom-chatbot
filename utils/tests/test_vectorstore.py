import pytest
import sys
sys.path.append('..')
from ai.embeddings.embeddings_mapper import Embeddings_Mapper
from utils.loaders.loader_mapper import LoaderMapper
from utils.splitters.recursive import RecursiveCharacter_TextSplitter
from utils.vectorstores.deep_lake import DeeplakeDB

def clear_db():
    embeddings_mapper = Embeddings_Mapper()
    embeddings = embeddings_mapper.find_model("openai")
    deeplake = DeeplakeDB(store_path = './test_deeplake', embedding_model = embeddings)
    deeplake.delete_all()

@pytest.fixture(scope="session", autouse=True)
def teardown(request):
    request.addfinalizer(clear_db)
    
@pytest.mark.parametrize("file, content", [
    ('tests/docs/dummy_doc_twinkle.pdf',
    """Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are!"""),
    ('tests/docs/example.csv', 
     """Name: John
        Age: 25
        Country: USA"""),
    ('tests/docs/dummy.txt',
    """Blah blah blah. Sample text. Blah Blah
    Blah Blah Blah. This is so fun. Blah Blah.
    Abcdefghijklmnopqrstuvwxyz.""" ),
    ('tests/docs/dummy.html', 
    """This is a dummy HTML file.
    It serves as an example."""),
    ('tests/docs/dummy.md', 
    """Dummy Markdown File
    This is a dummy Markdown file.
    It serves as an example. Item 1 Item 2 Item 3"""),
    ('tests/docs/dummy.docx',
    """Dummy Document
    This is a dummy Word document."""),
    ('tests/docs/dummy.pptx',
    """Dummy Presentation
    This is a dummy PowerPoint presentation."""),
    ('tests/docs/dummy.xlsx',
    """This is a dummy Excel spreadsheet."""),
])
def test_deeplake(file, content):
    #set up document to be embedded and stored
    loadermapper = LoaderMapper()
    loader = loadermapper.find_loader(file)
    data = loader.load()
    splitter = RecursiveCharacter_TextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    docs = [splitter.split_data(data)]
    #set up deeplake db and pass in relevant params
    embeddings_mapper = Embeddings_Mapper()
    embeddings = embeddings_mapper.find_model("huggingface")
    deeplake = DeeplakeDB(store_path = './test_deeplake', embedding_model = embeddings)
    deeplake.add_docs(docs)
    #pass in the file contents and see if it can return the most relevant document
    doc = deeplake.find_similar(content)
    source = doc[0].metadata["source"]
    assert file == source
    
    
