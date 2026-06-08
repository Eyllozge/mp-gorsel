import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("NEON_DATABASE_URL") 

try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("Neon veritabanına başarıyla bağlanıldı!")
    
except Exception as e:
    print(f"Bağlantı hatası: {e}")