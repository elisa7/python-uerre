# - * - unicode: utf8 -*-
import uuid
from datetime import datetime


class Trabajador(object):
    def __init__(self, idtrabajador, nombre):
        self.idtrabajador = idtrabajador
        self.nombre = nombre
        
        
# Se utilizan un diccionarios para guardar inormacion en estructura NoSQL

reportes = {}
reportes_danos = {}
trabajadores = {}
trabajadores["tamano"] = 4
trabajadores["1"] = Trabajador(uuid.uuid4(), "Juan")
trabajadores["2"] = Trabajador(uuid.uuid4(), "Jose")
trabajadores["3"] = Trabajador(uuid.uuid4(), "Maria")
trabajadores["4"] = Trabajador(uuid.uuid4(), "Pedro")


class Reporte(object):

    def __init__(self):
        self.id = uuid.uuid4().int
        self.fecha = datetime.now()


class ReporteBache(Reporte):

    def __init__(self, bache, estatus, prioridad, orden_trabajo=None):
        super().__init__()
        self.bache = bache
        self.estatus = estatus
        self.prioridad = prioridad
        self.orden_trabajo = orden_trabajo


class ReporteDano(Reporte):

    def __init__(self, ciudadano, desperfectos, reporte_bache, vehiculo, estatus):
        super().__init__()
        self.ciudadano = ciudadano
        self.desperfectos = desperfectos
        self.reporte = reporte_bache
        self.vehiculo = vehiculo
        self.estatus = estatus


class Vehiculo(object):

    def __init__(self, placas, descripcion):
        self.id = uuid.uuid4().int
        self.placas = placas
        self.descripcion = descripcion


class Bache(object):

    def __init__(self, tipo, direccion, tamano, posicion):
        self.id = uuid.uuid4()
        self.tipo = tipo
        self.direccion = direccion
        self.tamano = tamano
        self.posicion = posicion


class Revision(object):

    def __init__(self, resultado, materiales, equipos, inspector):
        self.id = uuid.uuid4()
        self.resultado = resultado
        self.materiales = materiales
        self.equipos = equipos
        self.inspector = inspector


class OrdenTrabajo(object):

    def __init__(self, cuadrillas, revision, fecha_reparacion, costo):
        self.id = uuid.uuid4()
        self.cuadrillas = cuadrillas
        self.revision = revision
        self.fecha_reparacion = fecha_reparacion
        self.costo = costo


class Equipo(object):

    def __init__(self, tipo, descripcion):
        self.id = uuid.uuid4()
        self.tipo = tipo
        self.descipcion = descripcion


class Material(object):

    def __init__(self, tipo, descripcion):
        self.id = uuid.uuid4()
        self.tipo = tipo
        self.descipcion = descripcion


class MaterialRequerido(object):

    def __init__(self, material, cantidad):
        self.id = uuid.uuid4()
        self.materila = material
        self.cantidad = cantidad

        
class Cuadrilla(object):
    def __init__(self, idcuadrilla, trabajadores):
        self.idcuadrilla = idcuadrilla
        self.trabajadores = trabajadores
        
        
# Se  crea la clase Direccion
class Direccion(object):
    def __init__(self, pCalle, pNumero, pColonia, pEntrecalles):
        self.calle = pCalle
        self.numero = pNumero
        self.colonia = pColonia
        self.entrecalles = pEntrecalles


# Se  crea la clase Usuario
class Usuario(object):
    def __init__(self, pId, pNombre, pRol):
        self.Id = pId
        self.nombre = pNombre
        self.rol = pRol

    def getId(self):
        return self.Id

    def getNombre(self):
        return self.nombre

    def getRol(self):
        return self.rol


# Se  crea la clase Ciudadano
class Ciudadano(Usuario):
    def __init__(self, pId, pNombre, pDireccion, pTelefono):
        Usuario.__init__(self, pId, pNombre, "Ciudadano")
        self.Direccion = pDireccion
        self.Telefono = pTelefono

    def getDireccion(self):
        return self.Direccion

    def GetTelefono(self):
        return self.Telefono


# Se  crea la clase Inspector
class Inspector(Usuario):
    def __init__(self, pId, pNombre):
        Usuario.__init__(self, pId, pNombre, "Inspector")


# Se  crea la clase Administrador
class Administrador(Usuario):
    def __init__(self, pId, pNombre):
        Usuario.__init__(self, pId, pNombre, "Administrador")


def registrar_bache():
    print("Favor de ingresar los datos necesarios para el registro:\n")
    tipo = input("Tipo de Bache [hoyo/zanja/depresion/irregularidad]: ")
    print("Direccion\n")
    pCalle = input("Calle: ")
    pNumero = 0
    pColonia = input("Colonia: ")
    pEntrecalles = input("Entre calles:")
    tamano = input("Tamano [1 al 10]: ")
    posicion = input("Posicion [izquierda/centro/derecha: ")
    direccion = Direccion(pCalle, pNumero, pColonia, pEntrecalles)
    bache = Bache(tipo, direccion, tamano, posicion)
    estatus = 'Pendiente'
    prioridad = 1
    reporte = ReporteBache(bache, estatus, prioridad)
    reportes[reporte.id] = reporte
    print("Gracias Por registrar su reporte, su numero de registro es:", reporte.id)
    print("Favor de guardarlo para segumientos posteriores")


def registrar_dano():
    reporte = buscar_reporte()
    if not reporte:
        print("Reporte no encontrado")
        print("Para continuar primero registre el Bache")
        registrar_bache()
    pId = uuid.uuid4().int
    pNombre = input("Nombre Ciudadano: ")
    print("Direccion Ciudadano\n")
    pCalle = input("Calle: ")
    pNumero = input("Numero: ")
    pColonia = input("Colonia: ")
    pEntrecalles = input("Entre calles:")
    direccion = Direccion(pCalle, pNumero, pColonia, pEntrecalles)
    pTelefono = input("Telefono de contacto: ")
    ciudadano = Ciudadano(pId, pNombre, direccion, pTelefono)
    placas = input("Placas del vehiculo: ")
    descripcion = input("Descripcion del Vehiculo; color, modelo, marca :")
    vehiculo = Vehiculo(placas, descripcion)
    desperfectos = 'desperfectos'
    estatus = 'En Revision'
    reporte_dano = ReporteDano(ciudadano, desperfectos, reporte, vehiculo, estatus)
    reportes_danos[reporte_dano.id] = reporte_dano
    print("Su registro ha sido guardado, el folio es: ", reporte_dano.id)


def accesar():
    usuario = {'admin': 'admin'}
    menuAdmin = {'1': buscar_reporte, '2': buscar_dano, }
    answer = 's'
    print("=" * 80)
    print("Sistema de Administración de Reportes de desperfectos viales")
    print("\t\tAlcaldia de Monterrey")
    print("=" * 80)
    while answer == 's':
        option = input("""
            1) Reportes de Baches
            2) Reportes de daños a vehiculos
            Favor de elequir una opcion del menu?: """)
        print("=" * 80)
        if option not in ['1', '2']:
            print("Opcion invalida")
        else:
            menuAdmin[option]()
        answer = input("Desea registrar otro reporte? S/N: ").lower()
        while answer not in ['s', 'n']:
            answer = input("Desea registrar otro reporte? S/N: ").lower()
        if answer == 'n':
            break


def buscar_dano():
    id_dano = input("Introduzca el ID del daño: ")
    if id_dano in reportes_danos:
        return reportes[id_dano]
    else:
        return None


def buscar_reporte():
    id_reporte = input("Introduzca el ID del reporte: ")
    if id_reporte in reportes:
        return reportes[id_reporte]
    else:
        return None

    
def crear_orden_trabajo(id_reporte):

    trab = {}
    answer_reg_trabajador = 's'
    print("=" * 80)
    print("Asginar Trabajadores a Cuadrilla")

    print("=" * 80)

    while answer_reg_trabajador == 's':
        tam = trabajadores["tamano"]

        for x in range(tam):
            print(x + ") " + trabajadores[x].nombre)

        option = input("Selecione el numero de trabajador")
        
        if option > 0 & option < tam:
            trab[option] = trabajadores[option]
        else: 
            print("Opcion invalida")
        answer_reg_trabajador = input("Desea registrar asignar otro trabajador? S/N: ").lower()
        while answer_reg_trabajador not in ['s', 'n']:
            answer_reg_trabajador = input("Desea registrar asignar otro trabajador: ").lower()
        if answer_reg_trabajador == 'n':
            break
    cuadrilla = Cuadrilla(uuid.uuid4(), trab)
    fechare = input("Ingresa Fecha de reparación: ")
    costo = input("Ingresa Costo de reparación: ")
    orden = OrdenTrabajo(cuadrilla, revision, fechare, costo)

    if id_reporte in reportes:
        r = reportes[id_reporte]
        reportes[id_reporte] = ReporteBache(r.bache, r.estatus, r.prioridad, orden)

        
# inicio de programa
if __name__ == '__main__':
    answer = 's'
    print("=" * 80)
    print("Sistema de Reportes de desperfectos viales")
    print("\t\tAlcaldia de Monterrey")
    print("=" * 80)
    while answer == 's':
        option = input("""
        1) Reporte de Bache
        2) Reporte daño a vehiculo
        3) Ingresar Sistema Interno

        Favor de elequir una opcion del menu?: """)
        print("=" * 80)
        if option not in ['1', '2', '3']:
            print("Opcion invalida")
        else:
            if option == '1':
                registrar_bache()
            if option == '2':
                registrar_dano()
            if option == '3':
                accesar()
        answer = input("Desea registrar otro reporte? S/N: ").lower()
        while answer not in ['s', 'n']:
            answer = input("Desea registrar otro reporte? S/N: ").lower()
        if answer == 'n':
            break
