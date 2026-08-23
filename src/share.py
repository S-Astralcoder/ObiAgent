import os
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
model = SentenceTransformer("all-MiniLm-L6-v2")
client = QdrantClient(url=os.environ["QDRANT_DB_URL"])