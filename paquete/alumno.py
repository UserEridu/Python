'''
Clase para crear alumnos
'''

class Alumno:
    def __init__(self,
                 cedula: str,
                 nombre: str,
                 apellido: str,
                 edad: int,
                 altura: float,
                 sexo: bool, # True = femenino, False = masculino
                 turno: int, # 1 = mañana, 2 = tarde, 3 = noche
                 ) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.sexo = sexo
        self.turno = turno
        
    def nombre_completo(self) -> str:
        return f'{self.nombre.upper()} {self.apellido.upper()}'
    
    def obtener_sexo(self) -> str:
        if self.sexo:
            return 'Femenino'
        else:
            return 'Masculino'
        
    def obtener_turno(self) -> str:
        match self.turno:
            case 1: return 'Mañana'
            case 2: return 'Tarde'
            case 3: return 'Noche'
            case _: return 'No tiene turno'