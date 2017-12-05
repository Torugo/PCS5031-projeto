from pymongo import MongoClient

class mongoConnector(object):
    def __init__(self):
        mongoConnectionString = self.readMongoString()
        self.client = MongoClient(mongoConnectionString)
        self.db = self.client.datascience_database

    @staticmethod
    def readMongoString():
        try:
            f = open("mongoString.txt","r")
            return f.readline()
        except FileNotFoundError:
            print("File Not Found. Using localhost")
            return "localhost"
