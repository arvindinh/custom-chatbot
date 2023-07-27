import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

class Embeddings_Mapper:
    """
    A class to initalize a new embedding model based on the wrappers from langchain.
    """
    def __init__(self):
        self.openai_key = os.environ.get('OPENAI_API_KEY')

        self.model_map = {
            "openai" : (OpenAIEmbeddings, {"model": "text-embedding-ada-002", "openai_api_key": self.openai_key}),
            "huggingface": (HuggingFaceEmbeddings, {}),
        }
    
    def find_model(self, model):
        if model in self.model_map:
            model_class, model_args = self.model_map[model]
            model = model_class(**model_args)
            return model
        
        raise ValueError(f"Model '{model}' not recognized")
