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
.
├── README.md
├── __pycache__
│   └── app.cpython-310.pyc
├── data
│   ├── info_particulier_impot.csv
│   └── questions_fiches_fip.csv
├── docker-compose.yml
├── frontend
│   ├── Home.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── app.cpython-310.pyc
│   │   ├── client_llm.cpython-310.pyc
│   │   ├── client_lmm.cpython-310.pyc
│   │   ├── context_manager.cpython-310.pyc
│   │   └── retriever.cpython-310.pyc
│   ├── client_llm.py
│   ├── dockerfile
│   ├── index
│   │   └── faiss_data
│   │       ├── index.faiss
│   │       └── index.pkl
│   ├── media
│   │   ├── CV.jpg
│   │   └── test.jpg
│   ├── pages
│   │   ├── 1 Assistant.py
│   │   ├── 2 CV.py
│   │   └── 3 Consignes.py
│   ├── requirements.txt
│   ├── retriever.py
│   └── utils
│       ├── __pycache__
│       │   └── styles.cpython-310.pyc
│       └── styles.py
├── index
│   └── faiss_data
│       ├── index.faiss
│       └── index.pkl
├── k8s
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── ollama-deployment.yaml
│   └── ollama-service.yaml
├── ollama
│   ├── Modelfile
│   └── dockerfile
├── requirments.txt
├── sandbox
│   ├── app_old.py
│   ├── faiss_data
│   │   ├── index.faiss
│   │   └── index.pkl
│   ├── faiss_data2
│   │   ├── index.faiss
│   │   └── index.pkl
│   └── notbook.ipynb.ipynb
└── src
    ├── Home.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-310.pyc
    │   ├── app.cpython-310.pyc
    │   ├── client_llm.cpython-310.pyc
    │   ├── client_lmm.cpython-310.pyc
    │   ├── context_manager.cpython-310.pyc
    │   └── retriever.cpython-310.pyc
    ├── client_llm.py
    ├── create_index.py
    ├── main.py
    └── retriever.py