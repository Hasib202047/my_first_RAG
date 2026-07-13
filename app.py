from src.data_loader import load_all_documents
from src.embedding import EmbaddingPipeline
from src.search import RAGSearch,RAGSearch2
from src.vector_store import FaissVectorStore

if __name__ == "__main__":
    # docs = load_all_documents("data/pdf")
    # store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    # store.load()
    # print(store.query("Tell me in details about sanjana", top_k=3))

    rag_search = RAGSearch2()
    query = "Can you provide more details about Sanjana's work experience?"
    summary = rag_search.search_and_summarize(query=query)
    print("Summary:", summary)