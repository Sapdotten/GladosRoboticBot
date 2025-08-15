from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    token: str
    channel_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        prefix="BOT"
    )


class DeepSeekConfig(BaseSettings):
    email: str
    password: str
    chat_id: str
    token: str
    headless: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        prefix="AI"
    )
