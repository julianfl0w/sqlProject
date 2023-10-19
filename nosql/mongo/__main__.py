import random
from pymongo import MongoClient

class MongoManager:
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client.exampleDB
        self.collection = self.db.exampleCollection

    def generate_random_name(self):
        first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah']
        last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Martinez']
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        return f"{first_name} {last_name}"

    def write_data_to_db(self, age=30, occupation='Software Engineer'):
        name = self.generate_random_name()
        
        data = {
            'name': name,
            'age': age,
            'occupation': occupation,
            'skills':{
                'cloud':{
                    'aws':{},
                    'azure':{}
                },
                'web':{
                    'javascript':{
                        'node.js':{},
                        'express.js':{},
                        },
                    'webRTC':{},
                    'REST API':{}
                },
                'numeric':{
                    'python':{},
                    'numpy':{}
                }
            }
        }
        
        self.collection.insert_one(data)

    def read_data_from_db(self):
        documents = self.collection.find({})
        for doc in documents:
            print(doc)

if __name__ == "__main__":
    mongo_manager = MongoManager()
    for i in range(1000):
        mongo_manager.write_data_to_db()
    print("Data written to DB. Reading now...")
    mongo_manager.read_data_from_db()
