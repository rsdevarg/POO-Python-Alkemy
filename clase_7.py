from enum import Enum

class Tipo(Enum):
  CAT1 = "Percusión"
  CAT2 = "Viento"
  CAT3 = "Cuerdas"

class Fabrica:
  def __init__(self):
    self.sucursales = []
  def agregarSucursal(self, sucursal):
    self.sucursales.append(sucursal)
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
fab = Fabrica()
fab.agregarSucursal(suc)

#'''
print(f'''
Sucursal: {suc.nombre}
Instrumentos:
ID: {fab.sucursales[0].instrumentos[0].id}
Precio: {fab.sucursales[0].instrumentos[0].precio}
Tipo: {fab.sucursales[0].instrumentos[0].tipo.value}
''')
#'''
