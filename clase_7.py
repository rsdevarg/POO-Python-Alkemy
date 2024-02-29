from enum import Enum

class Tipo(Enum):
  CAT1 = "Percusión"
  CAT2 = "Viento"
  CAT3 = "Cuerdas"

class Fabrica:
  def __init__(self):
    sucursales = []
  def agregarSucursal(self):
    pass
  def listarInstrumentos(self):
    pass
  def instrumentosPorTipo(self):
    pass
  def borrarInstrumento(self):
    pass
  def porcInstrumentosPorTipo(self):
    pass

class Sucursal:
  def __init__(self, nombre):
    self.nombre = nombre
    self.instrumentos = []
  
  def agregarInstrumento(self, instrumento):
    self.instrumentos.append(instrumento)
class Instrumento:
  def __init__(self, id, precio, tipo):
    self.id = id
    self.precio = float(precio)
    self.tipo = tipo

ins = Instrumento(1, 100, Tipo.CAT1)
suc = Sucursal("Sucursal 1")
suc.agregarInstrumento(ins)

'''
print(f'
ID: {suc.instrumentos[0].id}
Precio: {suc.instrumentos[0].precio}
Tipo: {suc.instrumentos[0].tipo.value}
')
'''
