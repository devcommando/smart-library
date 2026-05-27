from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool

    database_url: str

    jwt_secret_key: str
    jwt_access_token_expire_minutes: int
    jwt_algorithm: str

    cart_ttl_minutes: int
    waitlist_notification_window_hours: int
    first_librarian_email: str

    class Config:
        env_file = ".env"
        env_file_encoding: "utf-8"

# Instantiate the class
settings = Settings()

