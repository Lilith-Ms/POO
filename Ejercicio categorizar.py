class Alumno: 
    def __init__(self, nombre: str, edad: int, matrícula: str):
        self.nombre = nombre
        self.edad = edad
        self.matrícula = matrícula


    def describir (self) -> str:
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y mi matrícula es {self.matrícula}."
    
    def calcular_categoría(self)-> str:
        if self.edad >=60:
            return "Adulto Mayor"
        elif self.edad >=18:
            return "Mayor de edad"
        else:
            return "Menor de edad"
        



# Bloque de prueba (Se ejecuta solo al correr el archivo directamente)
if __name__== "__main__":
    Hector = Alumno ("Hector Benavides", 58, "79756893")
    print(Hector.describir() )

categoría = Hector.calcular_categoría()

print(f"La categoría de {Hector.nombre} es: {categoría}")
print(Hector.nombre)
print(Hector.edad)
print(Hector.matrícula)


Alumno1 = Alumno ("Alex", 20, "89765")
print(Alumno1.describir())

categoría_Alex = Alumno1.calcular_categoría()
print(f"La categoría de {Alumno1.nombre} es: {categoría_Alex}")
print(Alumno1.nombre)
print(Alumno1.edad)
print(Alumno1.matrícula)

Alumno2 = Alumno ("Daniel", 15, "54673")
print(Alumno2.describir())

categoría_Daniel = Alumno2.calcular_categoría()
print(f"La categoría de {Alumno2.nombre} es: {categoría_Daniel}")
print(Alumno2.nombre)
print(Alumno2.edad)
print(Alumno2.matrícula)

Alumno3 = Alumno ("Emily",23, "27382")
print (Alumno3.describir())

categoría_Emily = Alumno3.calcular_categoría()
print (f"La categoría de {Alumno3.nombre} es: {categoría_Emily}")
print (Alumno3.nombre)
print (Alumno3.edad)
print (Alumno3.matrícula)
