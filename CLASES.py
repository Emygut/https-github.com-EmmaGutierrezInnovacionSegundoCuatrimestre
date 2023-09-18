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

    def agregar_clase(self, clase):
        self.clases.append(clase)

class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive

class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave_acceso = clave_acceso
        self.estado = estado
        self.cursos_inscritos = []

    def inscribirse_a_curso(self, curso):
        self.cursos_inscritos.append(curso)

class Administrador(UsuarioFinal):
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso, estado):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave_acceso, estado)

class CarritoDeCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, curso):
        self.items.append(curso)

    def confirmar_compra(self, medio_de_pago, datos_pago):
        # Realizar el proceso de compra y registrar la información
        pass

class MedioDePago:
    def __init__(self, nombre, datos_basicos):
        self.nombre = nombre
        self.datos_basicos = datos_basicos

class TarjetaCreditoDebito(MedioDePago):
    def __init__(self, nombre, datos_basicos, numero_tarjeta, fecha_vencimiento):
        super().__init__(nombre, datos_basicos)
        self.numero_tarjeta = numero_tarjeta
        self.fecha_vencimiento = fecha_vencimiento
	
class TransferenciaBancaria(MedioDePago):
    def __init__(self, nombre, datos_basicos, numero_cuenta, banco):
        super().__init__(nombre, datos_basicos)
        self.numero_cuenta = numero_cuenta
        self.banco = banco
