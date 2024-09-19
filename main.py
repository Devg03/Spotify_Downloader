import os
from dotenv import load_dotenv

# Leveraging dotenv to keep the spotify credentials confidential
load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
