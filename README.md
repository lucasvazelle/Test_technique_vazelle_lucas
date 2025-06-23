# Test_technique_vazelle_lucas

1. Clone le repo

git clone https://github.com/TON_UTILISATEUR/test_technique_vazelle_lucas.git
cd test_technique_vazelle_lucas



2. Lancer avec Docker Compose (pull des images sur Docker Hub)

$ docker compose up
Aucune construction (build) nécessaire : Docker va automatiquement télécharger les images depuis Docker Hub.


Deux images sont disponibles sur Docker Hub :

- Backend (Ollama) : [`lucasvazelle/ollama`](https://hub.docker.com/r/lucasvazelle/ollama)  
- Frontend (Streamlit) : [`lucasvazelle/ollama-frontend`](https://hub.docker.com/r/lucasvazelle/ollama-frontend)

Accès
- Frontend Streamlit : http://localhost:8501
- Serving Ollama : http://localhost:11434