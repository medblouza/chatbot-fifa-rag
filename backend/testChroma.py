import chromadb

client = chromadb.Client()
collection = client.create_collection(name="test")
collection.add(ids=["1"], documents=["Bonjour"])
print(collection.count())