"""RAG agent prompts."""

RAG_AGENT_SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on retrieved documents.
Use the retrieve_documents tool to find relevant information before answering.
Cite which documents you used in your response.
"""

SAMPLE_DOCUMENTS = [
    {
        "id": "doc1",
        "title": "Introduction to Machine Learning",
        "content": "Machine learning is a subset of AI that enables systems to learn from experience. Key types include supervised learning, unsupervised learning, and reinforcement learning.",
    },
    {
        "id": "doc2",
        "title": "Neural Networks",
        "content": "Neural networks are computing systems inspired by biological neural networks. Deep learning uses networks with many layers. Common architectures include CNNs for images and Transformers for sequences.",
    },
    {
        "id": "doc3",
        "title": "Large Language Models",
        "content": "LLMs like GPT-4 are trained on vast text data to understand and generate language. They use transformer architecture and can perform tasks like generation, summarization, and Q&A.",
    },
    {
        "id": "doc4",
        "title": "RAG Systems",
        "content": "Retrieval-Augmented Generation combines retrieval with generative models. RAG retrieves relevant documents and uses them as context, improving accuracy and reducing hallucinations.",
    },
    {
        "id": "doc5",
        "title": "Vector Databases",
        "content": "Vector databases store data as embeddings and enable similarity search. Popular options include Pinecone, Weaviate, Chroma, and FAISS. Essential for RAG and semantic search.",
    },
]
