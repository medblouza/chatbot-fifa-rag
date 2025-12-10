from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions
from ollama import Client

# --- INITIALISATION ---
app = FastAPI()

# ChromaDB
client = chromadb.PersistentClient(path="../vectors/chroma_db")

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="fifa_rules",
    embedding_function=embedding_fn
)

# Ollama client
ollama = Client(host='http://localhost:11434')

# --- REQUEST MODEL ---
class Question(BaseModel):
    query: str

# --- ROUTE ---
@app.post("/ask")
def ask_fifa(question: Question):

    # 1. Recherche vectorielle
    results = collection.query(
        query_texts=[question.query],
        n_results=3
    )

    # 2. Contexte
    context = "\n\n".join(results["documents"][0])

    # 3. Prompt
    prompt = f"""
Tu es un expert des Lois du Jeu FIFA 2024-2025.
Réponds de manière claire et précise.
Si la question ne concerne pas le football, dis-le.

CONTEXTE :
{context}

QUESTION :
{question.query}

RÉPONSE :
"""

    # 4. Génération via Ollama
    response = ollama.generate(
    model="llama3.2",
    prompt=prompt
)

    answer = response["response"]

    return {
        "question": question.query,
        "answer": answer,
        "sources": results["documents"][0]
    }
