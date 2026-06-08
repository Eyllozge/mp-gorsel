import sys
import os
import psycopg2 # PostgreSQL bağlantısı için eklendi Supabase'den Neon a geçilmek zorunda kalındığı için.
from psycopg2.extras import RealDictCursor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://senin-vercel-url.vercel.app"], 
    allow_methods=["POST"],
    allow_headers=["*"],
)

class QuizSubmit(BaseModel):
    isim_soyisim: str


DATABASE_URL = os.environ.get("Neon_DATABASE_URL")

@app.post("/api/submit")
def submit(data: QuizSubmit):
    conn = None
    try:
        
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor(cursor_factory=RealDictCursor)

      
        insert_query = """
            INSERT INTO anaveri (isim_soyisim) 
            VALUES (%s) 
            RETURNING id;
        """
        
        cursor.execute(insert_query, (data.isim_soyisim,))
        
        inserted_id = cursor.fetchone()["id"]
        conn.commit()
        
        cursor.close()
        return {"mesaj": "Kaydedildi", "id": inserted_id}

    except Exception as e:
        print("Veritabanı hatası:", e)
        if conn:
            conn.rollback() 
        raise HTTPException(status_code=500, detail="Kayıt başarısız")
    
    finally:
    
        if conn:
            conn.close()