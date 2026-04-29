#Class Profesor,Hereda de Persona
#Profesión, Maestría
class Persona: 
    def __init__(self, nombre: str, apellido: str, email: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def get_nombre_completo(self) -> str:
        print (f"{self._nombre} {self._apellido}")

class Estudiante(Persona): 
    def __init__(self, nombre: str, apellido: str, email: str, matrícula: str, grado: str): 
        super().__init__(nombre, apellido, email)
        self._matrícula = matrícula
        self._grado = grado

objEstudiante1 = Estudiante("Marcelo", "Ariza", "Marcel@est.edu", "Est-001", "Semestre_3")
objEstudiante1.get_nombre_completo()   #imprime: Marcelo Ariza

# Herencia
class Profesor(Persona):
    def __init__(self, nombre: str, profesion: str, maestria: str):
        super().__init__(nombre, profesion, maestria)  
        self.profesion = profesion
        self.maestria = maestria

    def mostrar_profesor(self):
        self.mostrar_profesor
        print("Profesion:", self.profesion)
        print("Maestria:", self.maestria)



profe1 = Profesor("Carlos", "Ingeniero", "Educación")
profe1.mostrar_profesor()