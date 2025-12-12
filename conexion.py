import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_APIKEY = os.getenv("SUPABASE_APIKEY")

# Crear conexión global
supabase: Client = create_client(SUPABASE_URL, SUPABASE_APIKEY)
