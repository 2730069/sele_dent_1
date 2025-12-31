import streamlit as st
from datetime import date
from capaLogica.lPersona import LPersona


class PPersonas:

    def __init__(self):
        self.logica = LPersona()

    # ===============================
    # PACIENTES
    # ===============================
    def obtener_pacientes(self):
        return self.logica.mostrarPersona()

    def insertar_paciente(self, paciente):
        self.logica.insertarPersona(paciente)

    def actualizar_paciente(self, id_paciente, datos):
        self.logica.actualizarPersona(id_paciente, datos)

    def eliminar_paciente(self, id_paciente):
        self.logica.eliminarPersona(id_paciente)

    # ===============================
    # HISTORIAL / TRATAMIENTOS
    # ===============================
    def obtener_historial(self):
        return self.logica.obtener_historial()

    def obtener_tratamientos(self):
        return self.logica.obtener_tratamientos()

    # ===============================
    # CITAS
    # ===============================
    def obtener_citas(self):
        return self.logica.obtenerCitas()

    def registrar_cita(self, cita):
        self.logica.registrarCita(cita)

    def actualizar_estado_cita(self, id_cita, estado):
        self.logica.actualizarEstadoCita(id_cita, estado)

    # ===============================
    # PAGOS
    # ===============================
    def obtener_facturas(self):
        return self.logica.obtenerFacturas()

    def actualizar_estado_pago(self, id_factura, estado_pago):
        self.logica.actualizarEstadoPago(id_factura, estado_pago)

    # ===============================
    # INTERFAZ STREAMLIT
    # ===============================
    def run(self):

        st.set_page_config(
            page_title="Sele Dent",
            layout="wide"
        )

        st.title("Sistema Clínico – Sele Dent")

        menu = st.sidebar.selectbox(
            "Menú",
            [
                "Registrar Paciente",
                "Ver Pacientes",
                "Historial Clínico",
                "Tratamientos",
                "Citas",
                "Pagos"
            ]
        )

        # =====================================================
        if menu == "Registrar Paciente":

            st.subheader("Nuevo Paciente")

            with st.form("form_paciente"):
                dni = st.text_input("DNI")
                nombres = st.text_input("Nombres")
                apepaterno = st.text_input("Apellido Paterno")
                apematerno = st.text_input("Apellido Materno")
                fecha_nacimiento = st.date_input(
                    "Fecha de nacimiento",
                    value=date(2000, 1, 1)
                )
                telefono = st.text_input("Teléfono")
                correo = st.text_input("Correo")
                genero = st.selectbox("Género", ["M", "F"])

                guardar = st.form_submit_button("Guardar")

                if guardar:
                    self.insertar_paciente({
                        "dni": dni,
                        "nombres": nombres,
                        "apepaterno": apepaterno,
                        "apematerno": apematerno,
                        "fecha_nacimiento": str(fecha_nacimiento),
                        "telefono": telefono,
                        "correo": correo,
                        "genero": genero
                    })
                    st.success("Paciente registrado correctamente")
                    st.rerun()

        # =====================================================
        elif menu == "Ver Pacientes":

            st.subheader("Pacientes")
            st.dataframe(
                self.obtener_pacientes(),
                use_container_width=True
            )

            st.divider()
            st.subheader("Actualizar paciente")

            with st.form("form_actualizar"):
                id_paciente = st.number_input(
                    "ID Paciente",
                    min_value=1
                )
                dni = st.text_input("Nuevo DNI")
                nombres = st.text_input("Nuevos nombres")
                apepaterno = st.text_input("Nuevo apellido paterno")
                apematerno = st.text_input("Nuevo apellido materno")
                telefono = st.text_input("Nuevo teléfono")
                correo = st.text_input("Nuevo correo")
                genero = st.selectbox("Género", ["M", "F"])

                actualizar = st.form_submit_button("Actualizar")

                if actualizar:
                    self.actualizar_paciente(
                        id_paciente,
                        {
                            "dni": dni,
                            "nombres": nombres,
                            "apepaterno": apepaterno,
                            "apematerno": apematerno,
                            "telefono": telefono,
                            "correo": correo,
                            "genero": genero
                        }
                    )
                    st.success("Paciente actualizado")
                    st.rerun()

            st.divider()
            st.subheader("Eliminar paciente")

            id_eliminar = st.number_input(
                "ID a eliminar",
                min_value=1,
                key="del"
            )

            if st.button("Eliminar"):
                self.eliminar_paciente(id_eliminar)
                st.success("Paciente eliminado")
                st.rerun()

        # =====================================================
        elif menu == "Historial Clínico":

            st.subheader("Historial Clínico")
            st.dataframe(
                self.obtener_historial(),
                use_container_width=True
            )

        # =====================================================
        elif menu == "Tratamientos":

            st.subheader("Tratamientos")
            st.dataframe(
                self.obtener_tratamientos(),
                use_container_width=True
            )

        # =====================================================
        elif menu == "Citas":

            st.subheader("Citas")
            st.dataframe(
                self.obtener_citas(),
                use_container_width=True
            )

            st.divider()
            st.subheader("Registrar cita")

            with st.form("form_cita"):
                id_paciente = st.number_input(
                    "ID Paciente",
                    min_value=1
                )
                id_odontologo = st.number_input(
                    "ID Odontólogo",
                    min_value=1
                )
                fecha = st.date_input("Fecha")
                hora = st.time_input("Hora")
                motivo = st.text_input("Motivo")

                registrar = st.form_submit_button("Registrar")

                if registrar:
                    self.registrar_cita({
                        "id_paciente": id_paciente,
                        "id_odontologo": id_odontologo,
                        "fecha_cita": f"{fecha} {hora}",
                        "motivo": motivo,
                        "estado": "Pendiente"
                    })
                    st.success("Cita registrada")
                    st.rerun()

            st.divider()
            st.subheader("Actualizar estado")

            id_cita = st.number_input(
                "ID Cita",
                min_value=1,
                key="cita"
            )
            estado = st.selectbox(
                "Estado",
                ["Pendiente", "Atendido", "Cancelado"]
            )

            if st.button("Actualizar estado"):
                self.actualizar_estado_cita(id_cita, estado)
                st.success("Estado actualizado")
                st.rerun()

        # =====================================================
        elif menu == "Pagos":

            st.subheader("Pagos")
            st.dataframe(
                self.obtener_facturas(),
                use_container_width=True
            )

            st.divider()
            st.subheader("Actualizar pago")

            id_factura = st.number_input(
                "ID Factura",
                min_value=1
            )
            estado_pago = st.selectbox(
                "Estado",
                ["Pendiente", "Pagado"]
            )

            if st.button("Actualizar pago"):
                self.actualizar_estado_pago(
                    id_factura,
                    estado_pago
                )
                st.success("Pago actualizado")
                st.rerun()
