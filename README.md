🏆 FIFA Rules AI Chatbot
Description

FIFA Rules AI Chatbot est une application NLP basée sur une architecture moderne permettant de poser des questions en langage naturel sur les Lois du Jeu FIFA (saison 2024–2025).

Le projet implémente un chatbot spécialisé utilisant :

une API REST FastAPI

une recherche sémantique (RAG) avec ChromaDB

un LLM local exécuté via Ollama

une interface utilisateur interactive développée avec Streamlit

Ce projet vise à démontrer une expertise pratique en NLP appliqué, architecture backend moderne et intégration de modèles de langage.

Objectifs du projet

Construire une API NLP performante avec FastAPI

Implémenter un chatbot RAG (Retrieval-Augmented Generation)

Exploiter des embeddings sémantiques pour la recherche de contexte

Intégrer un LLM local pour la génération de réponses

Fournir une interface utilisateur simple et interactive

Préparer le projet pour une future extension MLOps / Docker / Sécurité

Fonctionnalités actuelles

Questions en langage naturel sur les règles FIFA
Recherche vectorielle avec ChromaDB
Génération de réponses avec Ollama (LLM local)
API REST documentée automatiquement (Swagger)
Interface Streamlit pour interagir avec le chatbot
Sources retournées avec chaque réponse

Architecture du projet
projetChatbot/
│
├── backend/
│   ├── main.py              # API FastAPI
│   ├── auth.py              # (Préparé pour JWT - non activé)
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py               # Interface Streamlit
│
├── vectors/
│   └── chroma_db/            # Base vectorielle persistée
│
├── data/
│   ├── fifa_rules.txt
│
├── scripts/
│   └── build_vectors.py      # Génération des embeddings
│
└── README.md

Technologies utilisées
Backend

Python 3.10+

FastAPI

Uvicorn

Pydantic

ChromaDB

Ollama

NLP / IA

LLM local (LLaMA / Mistral via Ollama)

Embeddings Sentence Transformers

Architecture RAG

Frontend

Streamlit

Installation et exécution
1-Prérequis

Python 3.10+

Ollama installé

Modèle téléchargé :

ollama pull llama3.2

2-Installation Backend
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt


Lancer l’API :

uvicorn main:app --reload


Swagger :

http://localhost:8000/docs

3-Lancer le Frontend
cd frontend
streamlit run app.py

Exemple de questions

Quelle est la durée d’un match de football ?

Quand un carton rouge est-il attribué ?

Quelle est la règle du hors-jeu ?

Combien de joueurs peuvent être remplacés ?

Quelles sont les sanctions pour une main volontaire ?


Améliorations futures

Authentification JWT

Déploiement Docker / Docker Compose

Cache Redis pour accélérer les réponses

Monitoring et logs structurés

Frontend React

Tests unitaires et intégration

Déploiement cloud (AWS / GCP)