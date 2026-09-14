import os
from chromadb import PersistentClient
from ollama import chat
from backend.app.core.config import settings

def get_vector_store():
    client = PersistentClient(path=settings.VECTOR_STORE_PATH)
    try:
        collection = client.get_collection(name="medical_rag")
    except Exception:
        collection = client.get_or_create_collection(name="medical_rag")
    return collection

def query_rag_pipeline(question: str):
    collection = get_vector_store()
    
    results = collection.query(
        query_texts=[question],
        n_results=3
    )
    
    retrieved_docs = results['documents'][0] if results['documents'] else []
    sources = results['metadatas'][0] if results['metadatas'] else []
    
    context = "\n\n".join(retrieved_docs)
    
    prompt = f"""You are a helpful medical AI assistant. Use the following medical context to answer the user's question accurately. If you don't know, say you don't know based on the context.

Context:
{context}

Question: {question}
Answer:"""

    response = chat(model=settings.OLLAMA_MODEL, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    
    answer_text = response['message']['content']
    
    source_list = [str(s.get('source', 'Unknown')) for s in sources] if sources else ["Medical Documents"]
    
    return {
        "answer": answer_text,
        "sources": list(set(source_list))
    }