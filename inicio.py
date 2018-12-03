# - * - unicode: utf8 -*-
import uuid
from datetime import datetime

# Se utilizan un diccionarios para guardar inormacion en estructura NoSQL

reportes = {}
reportes_danos = {}

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
        self.resultado  = resultado
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

def registrar_dano(id_reporte):
    reporte = buscar_reporte(id_reporte)
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
    reportes_danos = [reporte_dano.id]  = reporte_dano
    print("Su registro ha sido guardado, el folio es: ", reporte_dano.id)




def accesar():
    usuario = {'admin': 'admin'}
    print("acceso")


def buscar_reporte(id_reporte):
    if id_reporte in reportes:
        return reportes[id_reporte]
    else:
        return None



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
                id_reporte = input("Favor de ingresar Folio de bache:")
                registrar_dano(id_reporte)
            if option == '3':
                accesar()
        answer = input("Desea registrar otro reporte? S/N: ").lower()
        while answer not in ['s', 'n']:
            answer = input("Desea registrar otro reporte? S/N: ").lower()
        if answer == 'n':
            break
