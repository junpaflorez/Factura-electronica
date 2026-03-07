from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = Field(default="API Facturacion")
    ENVIRONMENT: str = Field(default="dev")
    DEBUG: bool = Field(default=False)

    NIT_EMPRESA: str = Field(default="")
    RAZON_SOCIAL: str = Field(default="")

    DIAN_URL: str = Field(default="")
    CERTIFICATE_PATH: str = Field(default="")
    CERTIFICATE_PASSWORD: str = Field(default="")
    DATABASE_URL: str = Field(default="")
    JWT_SECRET: str = Field(default="")

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"

settings = Settings()