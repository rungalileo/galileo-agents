"""RAG tools."""
from langchain_core.documents import Document


def create_knowledge_base(documents: list[dict], embeddings) -> tuple:
    """Create an in-memory vector store from documents."""
    from langchain_community.vectorstores import FAISS

    docs = [
        Document(page_content=doc["content"], metadata={"id": doc["id"], "title": doc["title"]})
        for doc in documents
    ]
    vector_store = FAISS.from_documents(docs, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return vector_store, retriever


def format_docs(docs: list[Document]) -> str:
    """Format retrieved documents for display."""
    return "\n\n".join(
        f"[{i}] {doc.metadata.get('title', 'Unknown')}:\n{doc.page_content}"
        for i, doc in enumerate(docs, 1)
    )
