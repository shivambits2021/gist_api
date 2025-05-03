from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SOURCE_API_URL: str
    PROJECT_NAME :str =  "GIST_API"
   
    class Config:
        env_file = ".env"

settings = Settings()
