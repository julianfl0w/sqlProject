from elasticsearch import Elasticsearch

class ElasticsearchManager:
    def __init__(self, host='localhost', port=9200, username="elastic", password="daFIiCqD_XW9wkv8RhNq"):
        self.es = Elasticsearch(
            hosts=[{'host': host, 'port': port, "scheme": "https"}],
            http_auth=(username, password),
            verify_certs=False # Set this to True and provide the path to the CA cert if you have one.
        )

    def insert_data(self, index_name="example-index"):
        # Sample data
        documents = [
            {"id": 1, "text": "The quick brown fox"},
            {"id": 2, "text": "Jumped over the lazy dog"},
            {"id": 4, "text": "Hello, World!"}
        ]

        # Index each document
        for doc in documents:
            self.es.index(index=index_name, id=doc["id"], body=doc)

    def retrieve_data(self, index_name="example-index"):
        # Retrieve and print all documents from the index
        result = self.es.search(index=index_name, body={"query": {"match_all": {}}})

        for hit in result['hits']['hits']:
            print(hit['_source'])

if __name__ == "__main__":
    es_manager = ElasticsearchManager()

    es_manager.insert_data()
    print("Data inserted into Elasticsearch. Retrieving now...")
    es_manager.retrieve_data()
