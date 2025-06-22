python -m venv .venv
source .venv/Scripts/activate
pip install uv
uv pip install -r requirements.txt
python -m spacy download fr_core_news_sm