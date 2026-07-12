from typing import List, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
from src.data_loader import load_all_documents

class EmbaddingPipeline:
    """docstring for EmbaddingPipeline."""
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5",chunk_size = 1000, chunk_overlap = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.model = SentenceTransformer(model_name)
        print(f"Loaded embedding model name: {model_name}")

    ### Text chunking
    def chunk_documents(self,documents:List[Any])-> List[Any]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap,
            length_function = len,
            separators = ["\n\n","\n"," ",""]
        )
        chunks = splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks")
        return chunks
    
    ### Text embeddings
    def embed_documents(self,chunks:List[Any])-> np.ndarray:
        embeddings = self.model.encode([chunk.page_content for chunk in chunks],show_progress_bar=True)
        print(f"Created embeddings for {len(embeddings)} chunks.")
        return embeddings

    