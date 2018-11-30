# - * - unicode: utf8 -*-
import uuid
from datetime import datetime

# Se utilizan un diccionarios para guardar inormacion en estructura NoSQL

reportes = {}


def buscar_reporte(id_reporte):
    if id in reportes:
        return reportes[id_reporte]
    else:
        return None


class Reporte(object):

    def __init__(self):
        self.id = uuid.uuid4()
        self.fecha = datetime.now()


class ReporteBache(Reporte):

    def __init__(self, bache, reporte, estatus, prioridad, orden_trabajo):
        super(Reporte, self).__init__()
        self.bache = bache
        self.reporte = reporte
        self.estatus = estatus
        self.prioridad = prioridad
        self.orden_trabajo = orden_trabajo



class ReporteDano(Reporte):

    def __init__(self, ciudadano, desperfectos, reporte_bache, vehiculo, estatus):
        super(Reporte, self).__init__()
        self.ciudadano = ciudadano
        self.desperfectos = desperfectos
        self.reporte = reporte_bache
        self.vehiculo = vehiculo
        self.estatus = estatus


class Vehiculo(object):

    def __init__(self, placas, descripcion):
        self.id = uuid.uuid4()
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
        if int(option) not in [1, 2, 3]:
            print("Opcion invalida")

        answer = input("Desea registrar otro reporte? S/N: ").lower()
        while answer not in ['s', 'n']:
            answer = input("Desea registrar otro reporte? S/N: ").lower()
        if answer == 'n':
            break
