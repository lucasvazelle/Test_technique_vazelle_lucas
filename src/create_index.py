import pandas as pd
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import duckdb


def load_documents_from_duckdb(
    db_path: str, table_name: str = "info_particulier_impot"
) -> list[Document]:
    """Récupère les documents de la base de données DuckDB et les formates pour créer des vecteurs de ces fiches"""
    con = duckdb.connect(database=db_path)
    df = con.execute(f"SELECT * FROM {table_name}").fetchdf()
    con.close()

    documents = []
    for _, row in df.iterrows():
        titre = row.get("Titre", "")
        texte = row.get("Texte", "")
        url = row.get("URL", "")
        content = f"{titre}\n\n{texte}"

        metadata = {"source": url, "titre": titre}

        documents.append(Document(page_content=content, metadata=metadata))

    return documents


def create_faiss_index(
    documents: list[Document], save_path: str = "index/faiss_data"
) -> FAISS:
    """Creation du vecteur store FAISS, embedding pour la transformation en vecteur des documents en input"""

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    faiss_index = FAISS.from_documents(documents, embedding_model)
    faiss_index.save_local(save_path)

    return faiss_index


if __name__ == "__main__":
    csv_path = "../data/info_particulier_impot.csv"
    save_path = "../index/faiss_data"

    print("Chargement des documents...")
    docs = load_documents_from_duckdb(csv_path)

    print(f"{len(docs)} documents chargés. Création de l’index FAISS...")
    create_faiss_index(docs, save_path)

    print(f"Index sauvegardé dans {save_path}")
