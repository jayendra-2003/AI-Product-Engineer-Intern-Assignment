import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# ==========================
# API Keys
# ==========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# ==========================
# LLM Configuration
# ==========================
MODEL_NAME = "gpt-4.1-mini"
TEMPERATURE = 0.7


# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "text-embedding-3-small"


# ==========================
# ChromaDB Configuration
# ==========================
CHROMA_DB_PATH = "./chroma_db"

COLLECTION_NAME = "sports_quiz"


# ==========================
# Retrieval Configuration
# ==========================
TOP_K_RESULTS = 5


# ==========================
# Web Search Configuration
# ==========================
MAX_WEB_RESULTS = 3


# ==========================
# Supported Sports
# ==========================
SPORTS = [
    "Cricket",
    "Football",
    "Basketball",
    "Tennis",
    "Badminton",
    "Hockey",
    "Baseball",
    "Formula 1",
]


# ==========================
# Difficulty Levels
# ==========================
DIFFICULTIES = [
    "Easy",
    "Medium",
    "Hard",
]