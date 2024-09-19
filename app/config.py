from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG Location Recommender"
    PROJECT_VERSION: str = "1.0.0"
    
    DEBUG: bool = False
    LOG_FILE: str = "app.log"
    
    MODEL_PATH: str = "meta-llama/Meta-Llama-3.1-8B-Instruct"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    MAX_LENGTH: int = 1000
    TEMPERATURE: float = 0.7
    TOP_P: float = 0.95

settings = Settings()