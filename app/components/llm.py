from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.chat_models import ChatHuggingFace
from langchain_groq import ChatGroq
from app.config.config import Configurations
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(groq_api_key : str = Configurations.GROQ_API_KEY, model : str = Configurations.MODEL):
    try:

        logger.info("Loading LLM from HuggingFace.")

        llm = ChatGroq(
            model = model,
            api_key = groq_api_key,
            temperature=0.3,
        )

        logger.info("LLM loaded successfully.")

        return llm
    
    except Exception as e:
        error_mesasge = CustomException("Failed to load LLM", e)
        logger.error(str(error_mesasge))
        