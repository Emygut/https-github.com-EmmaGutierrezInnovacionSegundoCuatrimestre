from enum import Enum
class Curso:
    def __init__(self, fecha_inicio, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado, categoria):
        self.fecha_inicio = fecha_inicio
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado
        self.categoria = categoria
        self.clases = []

class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive

class Usuario:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = estado

class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado)
        self.cursos_dictados = []

class UsuarioFinal(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado, clave_acceso, activacion_email):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado)
        self.clave_acceso = clave_acceso
        self.activacion_email = activacion_email
        self.cursos_inscritos = []

class Administrador(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, estado)

class CarritoCompra:
    def __init__(self, usuario_final):
        self.usuario_final = usuario_final
        self.items = []

class Compra:
    def __init__(self, id_compra, id_carrito_compra, id_medio_pago, id_usuario, fecha, monto_total):
        self.id_compra = id_compra
        self.id_carrito_compra = id_carrito_compra
        self.id_medio_pago = id_medio_pago
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto_total = monto_total

class MedioContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

class TiposMedioContacto(Enum):
    WHATSAPP = "WhatsApp"
    CORREO_ELECTRONICO = "Correo electrónico"
    CALL_CENTER = "Call center"
    REFERIDO_INTERNO = "Referido interno"

