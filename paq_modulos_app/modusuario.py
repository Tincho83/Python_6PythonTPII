# -*- coding: utf-8 -*-
"""
***************************************************************
* TP I de Python para CoderHouse, creado 09/09/2025 09:21:32  *
*                                                             *
* @author: Martin Hernandez                                   *
* Ultima Modificacion: 12/09/2025                             *
***************************************************************
"""

import csv
import os

# Ruta directorio actual
ruta_directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Bajar un nivel
ruta_directorio_csv = os.path.dirname(ruta_directorio_actual)
# Agregar carpeta "persistencia"
ruta_persistencia_csv = os.path.join(ruta_directorio_csv, "persistencia")
# nombre de archivo para la persistencia
archivo_csv = "db.csv"
# ruta definitiva para gurdar datos csv en persistencia de archivo
ruta_csv = os.path.join(ruta_persistencia_csv, archivo_csv)


# Funcion para cargar desde archivo csv, los usuarios creados.
# Si existen datos se cragan, sino devuelve diccionario vacio.
def cargar_usuarios_desde_csv(ruta_csv):
    db = {}
    if os.path.exists(ruta_csv):
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # intentar saltar encabezado si existe
            try:
                #saltar primera linea
                next(lector)
            except StopIteration:
                # archivo vacio, devolver diccionario vacio
                return db  

            for fila in lector:
                if len(fila) == 2:
                    usuario, contrasena = fila
                    db[usuario] = contrasena
    return db


# Funcion para guardar usuario creado en archivo csv.
def guardar_usuarios_en_csv(db, ruta_csv):
    with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        for usuario, contrasena in db.items():
            escritor.writerow([usuario, contrasena])


# Base de datos Diccionario (En memoria durante la ejecucion. No Persistente)
#credenciales_db = {}

# Base de datos Diccionario desde persistencia en csv
credenciales_db = cargar_usuarios_desde_csv(ruta_csv)


# Funcion para Registro de Usuario.
def registrar_usuario(db_usuario):
    """Registra un nuevo usuario en la base de datos."""

    while True:
        usuario = input("Ingrese Nombre de Usuario: ")
        valido, resultado = validar_usuario(usuario, db_usuario)
        if not valido:
            print(resultado + "\n")
            continue
        usuario_normalizado = resultado

        contrasena = input("Ingrese contraseña: ")
        valido, resultado = validar_contrasena(contrasena)
        if not valido:
            print(resultado + "\n")
            continue
        contrasena = resultado

        db_usuario[usuario_normalizado] = contrasena
        guardar_usuarios_en_csv(db_usuario, ruta_csv)
        print(f"*** El Usuario '{usuario_normalizado}' se registró correctamente.\n")
        break


# Funcion para Validar datos ingresados de Usuario.
def validar_usuario(usuario, db):
    """Valida el nombre de usuario según reglas."""

    # Normalizamos el usuario a minusculas para comparar
    usuario_normalizado = usuario.lower()

    # Comprobar longitud de usuario ingresado
    tamano_usuario = len(usuario_normalizado)

    if not usuario_normalizado:
        return False, ">Error: El nombre de usuario no puede estar vacio."
    if len(usuario_normalizado) > 25:
        return False, ">Error: El usuario debe tener hasta 25 caracteres."
    if usuario_normalizado in db:
        return False, ">Error: El usuario ya existe."
    if usuario_normalizado.isdigit():
        return False, ">Error: El usuario no puede ser solo números. Debe contener al menos una letra."
    return True, usuario_normalizado


# Funcion para Validar datos ingresados de Contraseña.
def validar_contrasena(contrasena):
    """Valida la contraseña según reglas."""
    contrasena = contrasena.strip()
    if not contrasena:
        return False, ">Error: La contraseña no puede estar vacía."
    if len(contrasena) > 25:
        return False, ">Error: La contraseña debe tener hasta 25 caracteres."
    return True, contrasena


# Funcion para Listar Usuarios.
def listar_usuarios(db_usuario):
    """Muestra solo los usuarios registrados."""

    #Comprobamos si existe al menos un usuario registrado en la BD
    if not db_usuario:
        print("No existen usuarios registrados en la base de datos.\n")
    else:
        # Imprimir multi linea
        print("""Listado de usuarios registrados:
┌─────────────────────────────┐
│    Nombre/s de Usuario/s    │
├─────────────────────────────┤""")

        # Recorremos los usuarios en la BD
        contador_filas = len(db_usuario)
        for usuario in db_usuario:

            # Realizamos calculos para armar el cierre de fila de la tabla
            tamano_usuario = len(usuario)
            espacios_linea_columna_usuario_tabla = 31 - 3 - tamano_usuario
            cadena_espacios_linea_columna_usuario_tabla = " " * espacios_linea_columna_usuario_tabla

            if contador_filas > 1:
                print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│")
                print("├-----------------------------┤")
                contador_filas -= 1
            else:
                print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│")
        print("└─────────────────────────────┘\n\n")


# Funcion para listar Usuarios con contraseña (Solo modo prueba)
def listar_usuarios_contrasenas(db_usuario):
    """Muestra usuarios registrados con sus contraseñas."""

    #Comprobamos si existe al menos un usuario registrado en la BD
    if not db_usuario:
        print("No existen usuarios registrados en la base de datos.\n")
    else:
         # Imprimir multi linea
        print("""Listado de usuarios registrados:
┌─────────────────────────────┬──────────────────────────┐
│    Nombre/s de Usuario/s    │       Contraseña/s       │
├─────────────────────────────┼──────────────────────────┤""")

        # Recorremos los usuarios en la BD
        contador_filas = len(db_usuario)
        for usuario, contrasena in db_usuario.items():

             # Realizamos calculos para armar el cierre de fila de la tabla
            tamano_usuario = len(usuario)
            espacios_linea_columna_usuario_tabla = 31 - 3 - tamano_usuario
            cadena_espacios_linea_columna_usuario_tabla = " " * espacios_linea_columna_usuario_tabla

            tamano_contrasena = len(contrasena)
            espacios_linea_columna_contrasena_tabla = 31 - 6 - tamano_contrasena
            cadena_espacios_linea_columna_contrasena_tabla = " " * espacios_linea_columna_contrasena_tabla

            if contador_filas > 1:
                print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│ {contrasena}{cadena_espacios_linea_columna_contrasena_tabla}│")
                print("├-----------------------------┼--------------------------┤")
                contador_filas -= 1
            else:
                print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│ {contrasena}{cadena_espacios_linea_columna_contrasena_tabla}│")
        print("└─────────────────────────────┴──────────────────────────┘\n\n")


# Funcion para inicio de sesion.
def inicio_sesion(db_usuario):
    """Inicio de sesión de usuario y contraseña. Hasta 3 intentos."""

    if not db_usuario:
        print("No existen usuarios registrados.\n")
        return

    for intento in range(3):
        usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")

        usuario_normalizado = usuario.strip().lower()

        if usuario_normalizado in db_usuario and db_usuario[usuario_normalizado] == contrasena:
            print(f"*** Sesión iniciada de {usuario.capitalize()}.\n")
            bienvenida(db_usuario, usuario)
            return
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.\n")

    print("Demasiados intentos incorrectos de inicio de sesión.\n")


# Funcion para mostrar el banner de bienvenida
def bienvenida(db_usuario, usuario):
    """Muestra el banner de bienvenida despues de iniciar sesion."""
    tamano_usuario = len(usuario)
    espacios_linea_mensaje_bienvenida = 29 - tamano_usuario
    cadena_espacios_linea_mensaje_bienvenida = " " * espacios_linea_mensaje_bienvenida

    print("***********************************************")
    print(f"*   Bienvenido, {usuario.capitalize()}!{cadena_espacios_linea_mensaje_bienvenida}*")
    print("***********************************************\n\n")

    menu_usuario(db_usuario, usuario)

# Funcion para cambiar contraseña
def cambiar_contrasena(db_usuario, usuario):
    """Permite a un usuario cambiar su contraseña."""

    usuario_normalizado = usuario.lower()
    actual = input("Ingrese su contraseña actual: ")

    if db_usuario.get(usuario_normalizado) != actual:
        print("Contraseña incorrecta. No se puede cambiar.")
        return

    nueva = input("Ingrese la nueva contraseña: ")
    valido, resultado = validar_contrasena(nueva)
    if not valido:
        print(resultado)
        return

    db_usuario[usuario_normalizado] = resultado
    guardar_usuarios_en_csv(db_usuario, ruta_csv)
    print("Contraseña cambiada con éxito.")


# Funcion para mostrar Menu
def menu():
    """Menu principal del programa."""

    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Registrar usuario")
        print("2. Inicio de sesion")
        print("3. Listar usuarios")
        print("4. Listar usuarios con contraseña (Solo para Prueba)")
        print("5. Salir\n")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_usuario(credenciales_db)
        elif opcion == "2":
            inicio_sesion(credenciales_db)
        elif opcion == "3":
            listar_usuarios(credenciales_db)
        elif opcion == "4":
            listar_usuarios_contrasenas(credenciales_db)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")


# Funcion para usuario logeado
def menu_usuario(db_usuario, usuario):
    """Menu para usuarios."""
    while True:
        print(f"\n*** MENU USUARIO ({usuario.capitalize()}) ***")
        print("1. Ver mi informacion")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesion")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print(f"Usuario: {usuario}")
        elif opcion == "2":
            cambiar_contrasena(db_usuario, usuario)
        elif opcion == "3":
            print("Cerrando sesión de usuario...")
            break
        elif opcion == "4":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida. Intente de nuevo.")


# Funcion principal. Solo se ejecuta si corres moduloUsuario.py directamente
if __name__ == "__main__":

    #Informacion del TP I
    print(__doc__)

    # Ejecutar programa
    menu()