# ============================================================
# Lección 6: Cómo instalar Python en linux - guía completa paso a paso
# Autor: Rodrigo Lagos Navarro - Grupo 6E
# ============================================================

print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PROGRAMACIÓN FÁCIL")
print("Autor: Rodrigo Lagos Navarro | Matrícula: 23110148 | Grupo: 6E")

# OPCIÓN 1: INSTALACIÓN DESDE TIENDA DE APLICACIONES
print("\n> Paso 1: Instalación desde la tienda de aplicaciones")
print("- Abrir la tienda de aplicaciones de tu distro (Ubuntu Software, Gestor de Software en Mint, etc.).")
print("- Buscar: 'vscode', 'visual studio code' o 'code'.")
print("- Seleccionar Visual Studio Code y hacer clic en 'Instalar'.")
print("- Esperar a que finalice la instalación y luego abrir la aplicación.")
print("- Configurar el tema de color y cerrar la pestaña de bienvenida.")

# OPCIÓN 2: INSTALACIÓN POR TERMINAL
print("\n> Paso 2: Instalación mediante terminal")
print("Atajo para abrir la terminal: CTRL + ALT + T")

print("\n>> Actualizar lista de paquetes:")
print("sudo apt-get update   # o sudo apt update")

print("\n>> Instalar dependencias:")
print("sudo apt install software-properties-common apt-transport-https")

print("\n>> Importar llave GPG de Microsoft:")
print("sudo wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -")

print("\n>> Habilitar repositorio de VSCode:")
print('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')

print("\n>> Volver a actualizar paquetes:")
print("sudo apt update")

print("\n>> Instalar Visual Studio Code:")
print("sudo apt install code")

print("\n> Paso 3: Abrir VSCode")
print("- Puedes abrir VSCode desde el menú de aplicaciones o desde la terminal escribiendo: code")

print("\n=== Recomendación Final ===")
print("Si usas Linux frecuentemente, la instalación por terminal es más rápida y te permitirá mantener VSCode siempre actualizado.")
print("Si eres principiante, la instalación desde la tienda de aplicaciones es la opción más sencilla.")

