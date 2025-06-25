# Test_technique_vazelle_lucas

# 1. Clone le repo

git clone https://github.com/lucasvazelle/Test_technique_vazelle_lucas.git
cd test_technique_vazelle_lucas

# 2. Lancer avec Docker Compose

Assurez-vous d’avoir Docker et Docker Compose installés.

***$ docker-compose up --build***

Deux images sont disponibles sur Docker Hub :

- Backend (Ollama) : [`lucasvazelle/test_technique_vazelle_lucas-ollama`](https://hub.docker.com/r/lucasvazelle/test_technique_vazelle_lucas-ollama)  
- Frontend (Streamlit) : [`lucasvazelle/test_technique_vazelle_lucas-frontend`](https://hub.docker.com/r/lucasvazelle test_technique_vazelle_lucas-frontend`)

Accès
- Frontend Streamlit : http://localhost:8501
- Serving Ollama : http://localhost:11434

# Architecture  

| Dossiers | Description |
| --- | --- |
| data/ | données |
| frontend/ | application |
| frontend/index/faiss_data/ | vector store |
| frontend/media/ | media de l'application |
| frontend/pages/ | pages de l'application |
| frontend/utils/ | fonctions pour l'application |
| index/faiss_data/ | vector store |
| k8s/ | fichiers de configuration Kubernetes |
| ollama/ | LLM serving |
| sandbox/ | exploration |
| src/ | création de vector store et tests |
