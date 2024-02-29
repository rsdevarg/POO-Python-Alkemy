class Empleado:
  def __init__(self, dni, nombre, apellido, anioingreso):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.anioingreso = anioingreso

class PorComision(Empleado):
  def __init__(self, dni, nombre, apellido, anioingreso, salarioMinimo, clientesCaptados, montoPorCliente):
    super().__init__(dni, nombre, apellido, anioingreso)
    self.salarioMinimo = float(salarioMinimo)
    self.clientesCaptados = clientesCaptados
    self.montoPorCliente = montoPorCliente

  def mostrarSalario(self):
    salario = float(self.clientesCaptados * self.montoPorCliente)
    if salario < self.salarioMinimo:
      return self.salarioMinimo
    else:
      return salario


class SueldoFijo(Empleado):
  def __init__(self, dni, nombre, apellido, anioingreso, sueldoBasico):
    super().__init__(dni, nombre, apellido, anioingreso)
    self.sueldoBasico = sueldoBasico

  def mostrarSalario(self):
    sueldo = float(self.sueldoBasico)
    porcAdicional = 0
    if 2024 - self.anioingreso < 2:
      porcAdicional = 0
    elif 2024 - self.anioingreso >= 2 and 2024 - self.anioingreso <= 5:
      porcAdicional = 0.05
    elif 2024 - self.anioingreso > 5:
      porcAdicional = 0.1
    sueldo += sueldo * porcAdicional
    return sueldo
      
      

empleado_c1 = PorComision(1, "Juan", "Perez", 2020, 1000, 1, 500)
print(empleado_c1.mostrarSalario())
empleado_c2 = PorComision(2, "Maria", "Gomez", 2021, 1000, 3, 500)
print(empleado_c2.mostrarSalario())
empleado_c3 = PorComision(3, "Pedro", "Lopez", 2022, 1000, 5, 500)
print(empleado_c3.mostrarSalario())
empleado_c4 = PorComision(4, "Ana", "Rodriguez", 2023, 1000, 7, 500)
print(empleado_c4.mostrarSalario())
                          
empleado2 = SueldoFijo(1, "Juan", "Perez", 2010, 2500)
print(empleado2.mostrarSalario())
empleado3 = SueldoFijo(2, "Pedro", "Alvarez", 2024, 1000)
print(empleado3.mostrarSalario())
