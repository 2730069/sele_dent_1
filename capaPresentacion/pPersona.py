import streamlit as st
from capaLogica.dPersona import LPersona

class PPersonas:

    def __init__(self):
        self.__lPersona = LPersona()
        self.construirInterfaz()

    def construirInterfaz(self):

        st.title("Registro de Pacientes - Clínica Sele Dent")

        with st.form("formPaciente"):
            dni = st.text_input("DNI")
            nombres = st.text_input("Nombres")
            apePaterno = st.text_input("Apellido Paterno")
            apeMaterno = st.text_input("Apellido Materno")
            fecha_nacimiento = st.date_input("Fecha de nacimiento")
            telefono = st.text_input("Teléfono")
            correo = st.text_input("Correo")
            contrasenia = st.text_input("Contraseña", type="password")
            genero = st.selectbox("Género", ["M", "F"])

            btnGuardar = st.form_submit_button("Guardar Paciente", type='primary')

        if btnGuardar:
            paciente = {
                "dni": dni,
                "nombres": nombres,
                "apePaterno": apePaterno,
                "apeMaterno": apeMaterno,
                "fecha_nacimiento": str(fecha_nacimiento),
                "telefono": telefono,
                "correo": correo,
                "contrasenia": contrasenia,
                "genero": genero
            }
            self.insertarPaciente(paciente)

        self.mostrarPacientes()

    def insertarPaciente(self, paciente):
        resultado = self.__lPersona.insertarPersona(paciente)
        if resultado:
            st.success("Paciente registrado correctamente")
        else:
            st.error("No se pudo registrar al paciente")

    def mostrarPacientes(self):
        st.subheader("Lista de pacientes")
        lista = self.__lPersona.mostrarPersona()

        if lista:
            st.dataframe(lista)
        else:
            st.info("No hay pacientes registrados")
