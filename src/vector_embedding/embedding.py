import os
import pathlib
from typing import Literal
from uuid import uuid4
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer
from rich.console import Console
load_dotenv()

class VaultEmbeddingEngine:
    def __init__(self, client, model) -> None:
        self.working_directory = pathlib.Path(".").resolve()
        
        self.collection_name = os.environ["COLLECTION_NAME"]
        self.client = client

        self.model = model

        self.console = Console()



    def _embed_markdown_file(self, markdown_file_path : pathlib.Path):
        chunk_limit = int(os.environ["TEXT_CHUNK"])
        with open(markdown_file_path, "r", encoding="utf-8") as file:
            file_contents_list = file.read().split()

        for index in range(0, len(file_contents_list), chunk_limit):
            chunk = " ".join(file_contents_list[index : index + chunk_limit])
            self.client.upsert(collection_name=self.collection_name, points=[PointStruct(id=uuid4(), vector=self.model.encode(chunk), payload={"file_path" : markdown_file_path.resolve()})])
    

    def load_vault_data_to_vector_database(self, mode : Literal["passive", "active"]):
        if mode == "active":
            if self.client.collection_exists(collection_name=self.collection_name):
                self.client.delete_collection(collection_name=self.collection_name)
            self.client.create_collection(collection_name=self.collection_name, vectors_config=VectorParams(size=384, distance=Distance.COSINE))
        elif mode == "passive":
            if not self.client.collection_exists(collection_name=self.collection_name):
                self.client.create_collection(collection_name=self.collection_name, vectors_config=VectorParams(size=384, distance=Distance.COSINE))
            else:
                return 

        with self.console.status("Creating Vector embeddings.."):
            for markdown_file_path in self.working_directory.rglob("**/*.md"):
                self._embed_markdown_file(markdown_file_path=markdown_file_path)            
        print("Completed Embeddings process..")
    