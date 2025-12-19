import streamlit as st
from supabase import create_client, Client
from datetime import date

class PPersonas:

    def __init__(self):
        self.SUPABASE_URL = "https://nxambvgqormhaykxtvim.supabase.co"
        self.SUPABASE_KEY = "sb_secret_X-fnD5aPgSVbnAYnkHpWoA_dkOC5d5M"
        self.supabase: Client = create_client(
            self.SUPABASE_URL,
            self.SUPABASE_KEY
        )

    # ===============================
    # FUNCIONES
    # ===============================
    def obtener_pacientes(self):
        return self.supabase.table("pacientes").select("*").execute().data

    def obtener_historial(self):
        return self.supabase.table("historialclinico").select("*").execute().data

    def obtener_tratamientos(self):
        return self.supabase.table("tratamientos").select("*").execute().data

    def insertar_paciente(self, paciente):
        self.supabase.table("pacientes").insert(paciente).execute()

    # ===============================
    # INTERFAZ PRINCIPAL
    # ===============================
    def run(self):

        st.set_page_config(page_title="Sele Dent", layout="wide")
        st.title("🦷 Sistema Clínico - Sele Dent")

        menu = st.sidebar.selectbox(
            "Menú",
            ["Registrar Paciente", "Ver Pacientes", "Historial Clínico", "Tratamientos"]
        )

        # ----------------------------------
        if menu == "Registrar Paciente":
            st.subheader("➕ Nuevo Paciente")

            with st.form("form_paciente"):
                dni = st.text_input("DNI")
                nombres = st.text_input("Nombres")
                apepaterno = st.text_input("Apellido Paterno")
                apematerno = st.text_input("Apellido Materno")
                fecha_nacimiento = st.date_input("Fecha de nacimiento", value=date(2000,1,1))
                telefono = st.text_input("Teléfono")
                correo = st.text_input("Correo")
                contrasenia = st.text_input("Contraseña", type="password")
                genero = st.selectbox("Género", ["M", "F"])
                guardar = st.form_submit_button("Guardar")

            if guardar:
                paciente = {
                    "dni": dni,
                    "nombres": nombres,
                    "apepaterno": apepaterno,
                    "apematerno": apematerno,
                    "fecha_nacimiento": str(fecha_nacimiento),
                    "telefono": telefono,
                    "correo": correo,
                    "contrasenia": contrasenia,
                    "genero": genero
                }
                self.insertar_paciente(paciente)
                st.success("✅ Paciente registrado correctamente")

        # ----------------------------------
        elif menu == "Ver Pacientes":
            st.subheader("🧑‍⚕️ Pacientes")
            st.dataframe(self.obtener_pacientes(), use_container_width=True)

        elif menu == "Historial Clínico":
            st.subheader("📘 Historial Clínico")
            st.dataframe(self.obtener_historial(), use_container_width=True)

        elif menu == "Tratamientos":
            st.subheader("💊 Tratamientos")
            st.dataframe(self.obtener_tratamientos(), use_container_width=True)
