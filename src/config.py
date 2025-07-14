from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    token: str
    channel_id: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DeepSeekConfig(BaseSettings):
    email: str
    password: str
    chat_id: str
    ai_token: str
    headless: bool

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
