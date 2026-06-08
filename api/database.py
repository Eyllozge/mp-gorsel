import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.environ["NEON_URL"],
    os.environ["NEON_KEY"]
)