from langchain.vectorstores import Pinecone

class Pinecone:
    def __init__(self, index, embedding_model):
        self.db = Pinecone(index=index, embedding_function = embedding_model)
    
    def add_docs(self, documents):
        ids = []
        for document in documents:
            id = self.db.add_documents(document)
            ids.append(id)
        if len(ids) == 1:
            return ids[0]
        return ids
    
    def find_similar(self, query):
        return self.db.similarity_search(query)
    
    def delete_by_ids(self, ids):
        self.db.delete(ids)
