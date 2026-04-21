class Auto: 
    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color 
        self.ruedas = ruedas

 # Métodos añadidos
    def mostrar_info(self):
        print(f"marca: {self.marca}")
        print(f"color: {self.color}")
        print(f"ruedas: {self.ruedas}")

    def encender(self):
        print(f"El auto {self.marca} está encendido")


#Probar lo que hicimos
mi_auto = Auto ("Toyota","Rojo", 4)
print (f"marca: {mi_auto.marca}")
print (f"color: {mi_auto.color}")
print (f"ruedas: {mi_auto.ruedas}")

# Uso de métodos
mi_auto.mostrar_info()
mi_auto.encender()

auto2 = Auto("Honda","Lila",4)

auto3 = Auto("Ford","Verde",4)

print (f"Marca: { auto2.marca}")


#Ejercicio 1
class Celular:
    def __init__(self,diseño,batería,SistemaOperativo):
        self.diseño = diseño
        self.batería = batería
        self.SistemaOperativo = SistemaOperativo 

# Métodos añadidos
    def mostrar_info(self):
        print(f"diseño: {self.diseño}")
        print(f"batería: {self.batería}")
        print(f"SistemaOperativo: {self.SistemaOperativo}")

    def encender(self):
        print("El celular está encendido")

    def cargar(self):
        print("El celular se está cargando")

#Prueba
mi_Celular = Celular ("Ergonómico","3000Mhz","Android 16")
print (f"diseño: {mi_Celular.diseño}")
print (f"batería: {mi_Celular.batería}")
print (f"SistemaOperativo: {mi_Celular.SistemaOperativo}")

# Uso de métodos 
mi_Celular.mostrar_info()
mi_Celular.encender()
mi_Celular.cargar()

celular2 = Celular ("A Prueba de Agua","4000Mhz","Android 13")
celular3 = Celular ( "Z Flip","5000Mhz","Android 15")

print (f"SistemaOperativo: { celular3.SistemaOperativo}")

# Ejercicios Propios Tarea
#Clase 1
class Gato:
    def __init__(self,nombre,edad,color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    # Métodos
    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"color: {self.color}")

    def maullar(self):
        print(f"{self.nombre} dice: Miau")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")


#Prueba
mi_gato = Gato("Michi",2,"Gris")
print(f"nombre: {mi_gato.nombre}")
print(f"edad: {mi_gato.edad}")
print(f"color: {mi_gato.color}")

mi_gato.mostrar_info()
mi_gato.maullar()
mi_gato.dormir()
