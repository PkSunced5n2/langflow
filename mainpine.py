import pinecone

# Initialize Pinecone
pinecone.init(api_key='84cb8feb-9710-4eee-9d6e-c95950ef4e84', environment='us-east1-gcp')

# Connect to the index
index = pinecone.Index('pkindex')

# Insert vectors
vectors = [
    {"id": "1", "values": [0.1, 0.2, 0.3]},
    {"id": "2", "values": [0.4, 0.5, 0.6]},
    {"id": "3", "values": [0.7, 0.8, 0.9]},
]
index.upsert(vectors)

# Query vectors
query_results = index.query(queries=[[0.1, 0.2, 0.3]], top_k=1)
print(query_results)
