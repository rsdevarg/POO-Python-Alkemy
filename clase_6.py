class Empleado:
    def __init__(self, dni, nombre, apellido,
                 anioingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioingreso = anioingreso

    def mostrarSalario():
        pass

class PorComision(Empleado):
    def __init__(self, dni, nombre, apellido,
                 anioingreso, salarioMinimo,
                 clientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido,
                         anioingreso)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente

    def mostrarSalario(self, salarioMinimo,
                       clientesCaptados,
                       montoPorCliente):
        salario = clientesCaptados * montoPorCliente
        if salario < salarioMinimo:
            return salarioMinimo
        else:
            return salario

class SueldoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, 
                 anioingreso, sueldoBasico,
                 porcAdicional):
        super().__init__(dni, nombre, apellido,
                         anioingreso)
        self.sueldoBasico = sueldoBasico
        self.porcAdicional = porcAdicional
        
    def mostrarSalario(self):
        if 2024 - self.anioingreso < 2:
            sueldo = self.sueldoBasico
            return sueldo
        elif 2024 - self.anioingreso >= 2 and 2024 - self.anioingreso <= 5:
            sueldo += self.sueldoBasico * 0.05
            return sueldo
        elif 2024 - self.anioingreso > 5:
            sueldo += self.sueldoBasico * 0.1
            return sueldo



ejemplo = PorComision(29786765, "Carlos", "Perez", 1997, 2500.75, 10, 5)
print(ejemplo)