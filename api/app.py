from flask import Flask, request, session
from flask_cors import CORS
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

app = Flask(__name__)
app.secret_key = 'bob123'
CORS(app)
conversation_models = {}

def get_conversation_model():
    """
    checks if a model has already been initialized for the current session.
    if not, it creates one for the session and stores it.
    """
    session_id = session.get('session_id')
    
    if session_id not in conversation_models:
        # Create a new conversation model for the session
        embeddings = choose_embeddings("openai")
        llm = choose_llm("openai")
        deeplake = DeeplakeDB(store_path=deeplake_path, embedding_model=embeddings)
        conversation_models[session_id] = ConversationModel(llm, deeplake.db)
        
    return conversation_models[session_id]

def choose_embeddings(model):
    embeddings_mapper = Embeddings_Mapper()
    embeddings = embeddings_mapper.find_model(model)
    return embeddings

def choose_llm(model):
    llm_mapper = LLMs_Mapper()
    llm = llm_mapper.find_model(model)
    return llm


@app.route('/api/response', methods=['GET'])
def return_response():
    #extract the query from the request, pass into model
    query = request.args.get('query')
    model = get_conversation_model()
    response = model.get_response(query)
    
    return {'response': response}

if __name__ == '__main__':
    app.run()