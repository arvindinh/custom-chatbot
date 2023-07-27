import sys
sys.path.append('..')
import os
from ai.embeddings.embeddings_mapper import Embeddings_Mapper
from ai.llms.llms_mapper import LLMs_Mapper
from ai.chains.conversational import ConversationModel
from utils.vectorstores.deep_lake import DeeplakeDB

openai_api_key = os.environ.get('OPENAI_API_KEY')
current_dir = os.path.dirname(os.path.abspath(__file__))
deeplake_path = os.path.join(current_dir, "..", "training", "embeddings_deeplake")

def choose_embeddings(model):
    embeddings_mapper = Embeddings_Mapper()
    embeddings = embeddings_mapper.find_model(model)
    return embeddings

def choose_llm(model):
    llm_mapper = LLMs_Mapper()
    llm = llm_mapper.find_model(model)
    return llm

def main():
    """
    This test/prompting file is using embeddings created from documents in the vector store for 
    the language model to answer queries and return responses in a conversational manner
    """
    #initialize the necessary objects for the Conversational Model to function
    embeddings = choose_embeddings("openai")
    llm = choose_llm("openai")
    deeplake = DeeplakeDB(store_path=deeplake_path, embedding_model=embeddings)
    qa = ConversationModel(llm, deeplake.db)
    query = ""
    
    #simple question answer loop in terminal to receive input and print response
    while True:
        query = input("Ask me a question: ")
        if query.lower() == "exit":
            break
        print("\n")
        result = qa.get_response(query)
        print(result)

    #deeplake.delete_all()
    
if __name__ == '__main__':
    main()
