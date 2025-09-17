# ============================================================
# Lección 7: Cómo instalar python en linux, configurar pip y entornos virtuales
# Autor: Rodrigo Lagos Navarro - Grupo 6E
# ============================================================

print("=== Portafolio Primer Parcial de Inteligencia Artificial ===")
print("Curso: PROGRAMACIÓN FÁCIL")
print("Autor: Rodrigo Lagos Navarro | Matrícula: 23110148 | Grupo: 6E")

# ACTUALIZAR PAQUETES
print("\n> Paso 1: Actualizar lista de paquetes")
print("CTRL + ALT + T  # Atajo para abrir terminal")
print("sudo apt-get update  # o sudo apt update")
print("- Esto asegura que tenemos la última versión de los paquetes disponibles.")

# COMPROBAR INSTALACIÓN DE PYTHON
print("\n> Paso 2: Comprobar si Python está instalado")
print("python3 --version  # Muestra versión instalada de Python")
print("- Si Python está desinstalado, reinstalar usando:")
print("sudo apt install python3")

# INSTALAR PIP
print("\n> Paso 3: Instalar PIP (gestor de paquetes de Python)")
print("sudo apt-get install python3-pip")
print("- Confirmar con 'S' o 'Y' según el idioma del sistema.")
print("- Comprobar instalación con:")
print("pip3 --version")

# POSIBLES ERRORES CON PIP
print("\n> Paso 4: Error común con PIP")
print("- Si aparece el error 'externally-managed-environment', significa que el sistema protege los paquetes instalados por APT.")
print("- Solución: usar entornos virtuales para evitar conflictos.")

# CREAR ENTORNO VIRTUAL
print("\n> Paso 5: Crear un entorno virtual de Python")
print("cd Documentos          # Moverse a la carpeta deseada")
print("mkdir pruebas-python   # Crear carpeta para el proyecto")
print("cd pruebas-python      # Entrar a la carpeta creada")
print("sudo apt install python3.11-venv   # Instalar módulo venv (ajustar versión)")
print("python3 -m venv entorno-pruebas   # Crear entorno virtual")

# ACTIVAR ENTORNO VIRTUAL
print("\n> Paso 6: Activar el entorno virtual")
print("source entorno-pruebas/bin/activate")
print("- Verás que el prompt cambia y muestra el nombre del entorno.")

# INSTALAR PAQUETES DENTRO DEL ENTORNO
print("\n> Paso 7: Instalar paquetes usando PIP en el entorno")
print("pip install numpy   # Ejemplo: instalar NumPy sin errores")

# DESACTIVAR ENTORNO
print("\n> Paso 8: Desactivar el entorno virtual")
print("deactivate")
print("- El prompt vuelve a su estado normal. Puedes activarlo de nuevo con 'source entorno-pruebas/bin/activate'.")

print("\n=== Recomendación Final ===")
print("Utiliza entornos virtuales para aislar dependencias y evitar conflictos entre paquetes de sistema y de PIP.")
print("De esta forma podrás instalar bibliotecas sin riesgo de dañar tu entorno de Linux.")

