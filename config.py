from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=True)

LOGIN_URL = "https://www.eprocure.gov.bd/"

EGP_USERNAME = os.getenv("EGP_USERNAME")
EGP_PASSWORD = os.getenv("EGP_PASSWORD")

HEADLESS = os.getenv(
    "HEADLESS",
    "False"
).lower() == "true"