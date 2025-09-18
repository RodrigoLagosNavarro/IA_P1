# ============================================================
# Lección 2.02: Los comentarios en Python
# Autor: Rodrigo Lagos Navarro - Grupo 6E
# ============================================================

print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PYTHON BASICO")
print("Autor: Rodrigo Lagos Navarro | Matrícula: 23110148 | Grupo: 6E")

# Comentario de una línea: explica que esta línea imprime un mensaje
print("¡Hola mundo!")  # Esto se imprimirá en la consola

# Desactivar temporalmente código usando comentario
# print("Esta línea no se ejecutará")
print("Esta línea sí se ejecutará")

# Comentarios a la derecha del código
print("Línea 1.")  # Comentario a la derecha
print("Línea 2.")  # Otro comentario
print("Línea 3.")

# Dividir secciones del código
# ============================================================
# Ejemplo de una función con secciones comentadas
def funcion_larga():
    # Primera sección: inicialización
    print("Inicio de la función")

    # Segunda sección: proceso intermedio
    print("Procesando datos...")

    # Tercera sección: finalización
    print("Fin de la función")

funcion_larga()

# Comentarios multilínea usando comillas dobles
"""
Este es un comentario
multilínea que explica
varias líneas de código
"""

# Comentarios multilínea usando comillas simples
'''
Otro ejemplo de comentario
multilínea. Puede ocupar
todas las líneas que necesites.
'''

# Ejemplo de anular un bloque de código
for i in range(1, 6):
    print(i)

"""
for i in range(10, 0, -1):
    print(i)
"""

# Docstrings para documentación
""" Docstring del módulo """

class Clase:
    """ Docstring de la clase """
    
    def metodo(self):
        """ Docstring del método """
        pass

    def funcion():
        """ Docstring de la función """
        pass
