from src.data_loader import load_all_documents
from src.embedding import EmbaddingPipeline
from src.search import RAGSearch
from src.vector_store import FaissVectorStore

if __name__ == "__main__":
    # docs = load_all_documents("data/pdf")
    # store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    # store.load()
    # print(store.query("Tell me in details about sanjana", top_k=3))

    rag_search = RAGSearch()
    query = "Tell me in details about hasibul?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)