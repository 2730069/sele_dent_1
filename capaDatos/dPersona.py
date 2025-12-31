from conexion import supabase

class DPersona:

    # =========================
    # PACIENTES
    # =========================
    def insertarPersona(self, persona):
        return supabase.table("pacientes").insert(persona).execute().data

    def mostrarPersona(self):
        return supabase.table("pacientes").select("*").execute().data

    def eliminarPersona(self, id_paciente):
        supabase.table("pacientes").delete().eq("id_paciente", id_paciente).execute()

    def actualizarPaciente(self, id_paciente, datos):
        supabase.table("pacientes") \
            .update(datos) \
            .eq("id_paciente", id_paciente) \
            .execute()

    # =========================
    # HISTORIAL CLÍNICO
    # =========================
    def obtener_historial(self):
        return supabase.table("historialclinico").select("*").execute().data

    # =========================
    # TRATAMIENTOS
    # =========================
    def obtener_tratamientos(self):
        return supabase.table("tratamientos").select("*").execute().data

    # =========================
    # CITAS
    # =========================
    def obtenerCitas(self):
        return supabase.table("citas").select("*").execute().data

    def registrarCita(self, cita):
        supabase.table("citas").insert(cita).execute()

    def actualizarEstadoCita(self, id_cita, estado):
        supabase.table("citas") \
            .update({"estado": estado}) \
            .eq("id_cita", id_cita) \
            .execute()

    # =========================
    # FACTURAS
    # =========================
    def obtenerFacturas(self):
        return supabase.table("facturas").select("*").execute().data

    def actualizarEstadoPago(self, id_factura, estado_pago):
        supabase.table("facturas") \
            .update({"estado_pago": estado_pago}) \
            .eq("id_factura", id_factura) \
            .execute()
