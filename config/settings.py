import json
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

ENV = os.getenv("TEST_ENV", "qa")  # dev / qa / prod

ENV_CONFIG = load_json(os.path.join(ROOT_DIR, "config", "env_config.json"))
BROWSER_CONFIG = load_json(os.path.join(ROOT_DIR, "config", "browser_config.json"))
BASE_URL = ENV_CONFIG[ENV]["base_url"]