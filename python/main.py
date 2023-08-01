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

    # 2) Cambio el método presentation de la clase Trabajador manteniendo la función original pero añadiendo un nuevo print con departamento y puesto
    def presentation(self):
        super().presentation()  # Mantengo el método de la clase Persona
        print(f"Trabajo en el departamento de {self.departamento} y mi puesto es {self.puesto}")


# main
def main():
    # 2) Crea una instancia trabajador_1 y llama a su función presentación
    nombre = 'Alberto'
    trabajador_1 = Trabajador(nombre, 20, 'IT', 'Data Engineer')
    trabajador_1.presentation()

    # 3)  ¿Qué diferencia hay entre self.nombre y la variable llamada nombre?
    '''
    - self.nombre es una variable de instancia, y se utiliza para almacenar un dato que es único para cada objeto.
    Para poder acceder a ella, siempre habrá que instanciar la clase en un objeto

    - nombre, en este caso, es una variable local dentro de la función main().
    Cuando se pasa como argumento al constructor de la clase Trabajador, se utiliza para inicializar la variable de instancia self.nombre con el valor de nombre, 
    pero la variable local nombre existe al margen de instanciar la clase Trabajador o Persona en cualquier objeto.
    '''

if __name__ == "__main__":
    main()
