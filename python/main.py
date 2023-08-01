# clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")


# 1) Define un nuevo objeto Trabajador, que herede de la clase Persona, añadiendo las propiedades departamento y puesto.  
class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad) # usamos la clase padre que ya aceptaba nombre y edad
        self.departamento = departamento
        self.puesto = puesto

# main
def main():
    # variables
    nombre = 'Alberto'

    persona_1 = Persona(nombre,20)
    persona_1.presentation()

if __name__ == "__main__":
    main()