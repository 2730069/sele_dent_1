from conexion import supabase

class DPersona:

    # Insertar un paciente
    def insertarPersona(self, persona: dict):
        try:
            response = supabase.table("Pacientes").insert(persona).execute()
            return response.data
        except Exception as e:
            print("Error al insertar:", e)
            return None

    # Obtener todos los pacientes
    def mostrarPersona(self):
        try:
            response = supabase.table("Pacientes").select("*").execute()
            return response.data
        except Exception as e:
            print("Error al obtener datos:", e)
            return []
