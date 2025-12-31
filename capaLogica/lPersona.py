from capaDatos.dPersona import DPersona

class LPersona:

    def __init__(self):
        self.d = DPersona()

    # PACIENTES
    def insertarPersona(self, p):
        return self.d.insertarPersona(p)

    def mostrarPersona(self):
        return self.d.mostrarPersona()

    def eliminarPersona(self, id_paciente):
        self.d.eliminarPersona(id_paciente)

    def actualizarPersona(self, id_paciente, datos):
        self.d.actualizarPaciente(id_paciente, datos)

    # HISTORIAL
    def obtener_historial(self):
        return self.d.obtener_historial()

    # TRATAMIENTOS
    def obtener_tratamientos(self):
        return self.d.obtener_tratamientos()

    # CITAS
    def obtenerCitas(self):
        return self.d.obtenerCitas()

    def registrarCita(self, cita):
        self.d.registrarCita(cita)

    def actualizarEstadoCita(self, id_cita, estado):
        self.d.actualizarEstadoCita(id_cita, estado)

    # PAGOS
    def obtenerFacturas(self):
        return self.d.obtenerFacturas()

    def actualizarEstadoPago(self, id_factura, estado):
        self.d.actualizarEstadoPago(id_factura, estado)
