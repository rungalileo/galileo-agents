"""Research crew tools."""
from langchain_core.documents import Document

KNOWLEDGE_BASE_DOCS = [
    {
        "id": "arch1",
        "title": "Microservices Architecture",
        "content": "Microservices breaks applications into small, independent services. "
        "Benefits: independent deployment, technology flexibility. "
        "Challenges: distributed complexity, data consistency.",
    },
    {
        "id": "arch2",
        "title": "Monolithic Architecture",
        "content": "Monolithic bundles all functionality into a single unit. "
        "Benefits: simpler development and deployment. "
        "Drawbacks: scaling limitations, technology lock-in.",
    },
    {
        "id": "cloud1",
        "title": "Cloud Computing",
        "content": "Cloud offers scalability, cost efficiency, and global reach. "
        "Key benefits: pay-as-you-go, automatic scaling, managed services. "
        "Providers: AWS, Azure, GCP.",
    },
    {
        "id": "devops1",
        "title": "DevOps Practices",
        "content": "DevOps combines development and operations. "
        "Key practices: CI/CD, infrastructure as code, monitoring. "
        "Benefits: faster releases, better collaboration.",
    },
    {
        "id": "ai1",
        "title": "AI in Enterprise",
        "content": "Enterprise AI focuses on automation and insights. "
        "Use cases: chatbots, analytics, document processing. "
        "Challenges: data quality, model governance.",
    },
]


def create_knowledge_retriever(embeddings):
    """Create a retriever from the knowledge base."""
    from langchain_community.vectorstores import FAISS

    docs = [
        Document(page_content=d["content"], metadata={"id": d["id"], "title": d["title"]})
        for d in KNOWLEDGE_BASE_DOCS
    ]
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 3})


def search_knowledge_base(query: str, retriever) -> str:
    """Search the knowledge base."""
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant documents found."
    return "\n\n".join(
        f"[{i}] {d.metadata.get('title')}:\n{d.page_content}" for i, d in enumerate(docs, 1)
    )
