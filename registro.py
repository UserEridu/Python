'''
Programa de registro de alumnos
'''
from paquete.alumno import Alumno
from paquete.utilidades import encabezado, linea

def main() -> None:
    alumno = Alumno(
        '26.124.788',
        'maritza',
        'lopez',
        21,
        1.76,
        True,
        1,
    )
    ver_datos_alumno(alumno)
    #print(alumno)
def ver_datos_alumno(alumno: Alumno) -> None:
    encabezado('mostrar datos del alumno', 50)
    print(f'Cédula: {alumno.cedula}' )
    print(f'Nombre Completo: {alumno.nombre_completo()}')
    print(f'edad: {alumno.edad}')
    print(f'Altura: {alumno.altura}')
    print(f'sexo: {alumno.obtener_sexo()}')
    print(f'Turno: {alumno.obtener_turno()}')
    
      
main()