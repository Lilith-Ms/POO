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

#Clase 2
class Avion:
    def __init__(self,modelo,capacidad,color):
        self.modelo = modelo
        self.capacidad = capacidad
        self.color = color

    # Métodos
    def mostrar_info(self):
        print(f"modelo: {self.modelo}")
        print(f"capacidad: {self.capacidad}")
        print(f"color: {self.color}")

    def despegar(self):
        print(f"El avión {self.modelo} está despegando")

    def aterrizar(self):
        print(f"El avión {self.modelo} está aterrizando")


#Prueba
mi_avion = Avion("Boeing 747",400,"Rojo")
print(f"modelo: {mi_avion.modelo}")
print(f"capacidad: {mi_avion.capacidad}")
print(f"color: {mi_avion.color}")

mi_avion.mostrar_info()
mi_avion.despegar()
mi_avion.aterrizar()

#Clase 3
class Moto:
    def __init__(self,marca,cilindraje,color):
        self.marca = marca
        self.cilindraje = cilindraje
        self.color = color

    # Métodos
    def mostrar_info(self):
        print(f"marca: {self.marca}")
        print(f"cilindraje: {self.cilindraje}")
        print(f"color: {self.color}")

    def encender(self):
        print(f"La moto {self.marca} está encendida")

    def acelerar(self):
        print(f"La moto {self.marca} está acelerando")


#Prueba
mi_moto = Moto("Yamaha","150cc","Negra")
print(f"marca: {mi_moto.marca}")
print(f"cilindraje: {mi_moto.cilindraje}")
print(f"color: {mi_moto.color}")

mi_moto.mostrar_info()
mi_moto.encender()
mi_moto.acelerar()