############################
# Load environment variables
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(f'{Path(__file__).resolve().parents[1]}\env_vars.env')
load_dotenv(dotenv_path=dotenv_path)

CONNECTION_STRING = os.getenv('MONGODB_CONNECTION_STRING')