import os 
from dataclasses import dataclass
from dotenv import load_dotenv 

# Load .env when module is imported
load_dotenv() 

@dataclass
class Settings: 
    openai_api_key: str 
    openai_model: str 

    @classmethod 
    def from_env(cls) -> "Settings": 
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY missing. \n"
                "Add your key in a .env-file in the project root folder:\n"
            )
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        return cls(
            openai_api_key=api_key,
            openai_model=model,
        )
    
settings = Settings.from_env()