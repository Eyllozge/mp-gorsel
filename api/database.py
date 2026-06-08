import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

neon_url = os.environ.get("NEON_URL") 

try:
    conn = psycopg2.connect(neon_url)
    cursor = conn.cursor()
    print("Neon veritabanına başarıyla bağlanıldı!")
    
except Exception as e:
    print(f"Bağlantı hatası: {e}")