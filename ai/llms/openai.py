
from langchain.llms import OpenAI

class Open_AI:
    """
    Simple wrapper for regular OpenAI langchain class, can adjust temperature and pass in api key
    """
    def __init__(self, api_key, temperature = 0):
        """
        Initializes an OpenAI object that can be passed in to a chain in a given chains module
        
        :param temperature:takes values 0-2, lower = more focused and deterministic, higher = random and diverse. 
        :param api_key: openai api key
        """
        self.model = OpenAI(temperature = temperature, openai_api_key = api_key, model_name="gpt-4")
