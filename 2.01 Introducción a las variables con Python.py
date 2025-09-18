# ============================================================
# Lección 2.01: Introducción a las variables con Python
# Autor: Rodrigo Lagos Navarro - Grupo 6E
# ============================================================


print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PYTHON BASICO")
print("Autor: Rodrigo Lagos Navarro | Matrícula: 23110148 | Grupo: 6E")

# DECLARACIÓN E INICIALIZACIÓN
print("\n> Declaración e inicialización de variables")
numero_1 = 10
print("numero_1 =", numero_1)  # Muestra el valor de la variable

# REASIGNACIÓN
print("\n> Reasignación de valores")
numero_1 = 20
print("numero_1 (nuevo valor) =", numero_1)

# TIPADO DINÁMICO
print("\n> Tipado dinámico: cambiar tipo de dato de una variable")
numero_1 = "Hola"
print("numero_1 ahora es un texto:", numero_1)

# ASIGNACIÓN MÚLTIPLE
print("\n> Asignación múltiple de variables")
numero_1, numero_2, numero_3 = 10, 12, 17
print("numero_1 =", numero_1, "| numero_2 =", numero_2, "| numero_3 =", numero_3)

print("\n> Flujo de ejecución: valores antes y después de reasignación")
numero_1 = 10
print("Valor inicial de numero_1:", numero_1)
numero_1 = 20
print("Valor reasignado de numero_1:", numero_1)

print("\n> Inicialización con tipo de dato (int)")
numero_vacio = int()
print("numero_vacio =", numero_vacio)

print("\n> Ejemplo usando punto y coma en una línea (no recomendado):")
numero_1 = 30; print("numero_1 con punto y coma =", numero_1)
# ============================================================
print("CODIGO")

numero_1 = 10
print(numero_1)

numero_1 = 20
print(numero_1)

numero_1 = "Hola"
print(numero_1)

numero_1, numero_2, numero_3 = 10, 12, 17
print(numero_1, numero_2, numero_3)

numero_1 = 10
print(numero_1)
numero_1 = 20
print(numero_1)

numero_vacio = int()
print(numero_vacio)

numero_1 = 30; print(numero_1)


