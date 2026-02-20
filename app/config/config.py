import os
from dotenv import load_dotenv

load_dotenv()


class Configurations:

    HF_TOKEN = os.environ.get("HF_TOKEN")
    HUGGINGFACE_REPO_ID = "google/flan-t5-large"

    DB_FAISS_PATH = "vectorstore/db_faiss"
    DATA_PATH = "data/"
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    MODEL = "llama-3.1-8b-instant"


class Paths:

    GITHUB_URL = os.getenv("GITHUB_URL")
    FILE_NAME = "Gale_Encyclopedia.pdf"
    DATA_DIR = "data"

