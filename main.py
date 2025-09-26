# -*- coding: utf-8 -*-
"""
****************************************************************
* TP II de Python para CoderHouse, creado 21/09/2025 22:54:32  *
*                                                              *
* @author: Martin Hernandez                                    *
* Ultima Modificacion: 26/09/2025                              *
****************************************************************
"""

from paq_modulos_app.modcliente import Cliente, ClienteZona
from paq_modulos_app.modusuario import *
from paq_modulos_app.modpersistencia import cargar_clientes_json, guardar_clientes_json
from datetime import datetime
from pathlib import Path
import random
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ruta_app_ejecucion = sys.argv[0]
argumentos_ejecucion = sys.argv


# Ruta actual
ruta_directorio_log = os.path.dirname(os.path.abspath(__file__))
# Agregar carpeta "logs"
ruta_logs = os.path.join(ruta_directorio_log, "logs")
archivo_log = "/log.txt"


# Cargar clientes al inicio
clientes = cargar_clientes_json()


# Funcion para registrar logs de acciones.
def registrar_log(texto_log):    
    dt = datetime.now()
    ruta_log = ruta_logs + archivo_log
    with open(ruta_log, "a", encoding="utf-8") as f:
        f.write(f"{dt.strftime('%d/%m/%Y %H:%M:%S')}: {texto_log}\n")


registrar_log("* Aplicacion: Inicio.")
registrar_log(f"***** Archivo log: {ruta_directorio_log}{archivo_log}.")


# Funcion para limpiar pantalla.
def limpiar_pantalla():
    """Limpia la pantalla de la consola.    
    Si es MS Windows ejecta CLS, Si es Unix o derivado ejecuta CLEAR 
    """
    registrar_log("***** Limpiando Pantalla.")     
    os.system('cls' if os.name == 'nt' else 'clear')        


# Funcion para mostrar cartel de presentacion
def mostrar_banner():
    """Muestra el banner principal del sistema.    
    """    
    registrar_log("***** Mostrando Cartel Sist Model Cli.")    
    print("""
┌──────────────────────────────────────────────────────────────┐
│            SISTEMA DE MODELAMIENTO DE CLIENTES               │
├──────  Gestión de Clientes para Aplicacion e-Commerce  ──────┤
└──────────────────────────────────────────────────────────────┘""")


# Funcion para mostrar menu principal
def mostrar_menu_principal():
    """Muestra el menú principal de opciones.
    """
    dt = datetime.now()

    registrar_log("***** Mostrando Menu Principal.")    

    # Mostramos Fecha y Hora personalizada
    print("      Fecha y Hora: ",dt.strftime("%A %d de %b del %Y    %H:%M"))
    print("\n*** MENU PRINCIPAL ***")
    print("1. Administrar Usuarios del Sistema (PreEntrega I)")
    print("2. Crear Nuevo Cliente")
    print("3. Realizar compra")
    print("4. Agregar Categoria de Interes")
    print("5. Calcular precio final de Producto si Cliente pertenece al Staff")
    print("6. Validar Direccion de Correo Electronico")
    print("7. Mostrar Datos de Clientes Registrados")
    print("8. Obtener Nro total de Clientes Registrados")
    print("9. Crear Cliente en Zona Cercana para envio en 24hs")
    print("0. Salir")


# Funcion para crear solo un cliente, guardarlo, mostrar datos e historial de compras
def crear_cliente():
    registrar_log("***** Creando Solo Cliente.")    
    cliente1 = Cliente("Diego", "Capomas", "DNI", 29032054, "diegoc@diego.com", 43, "Calle 3 Nro 96", ["tecnologia", "moda", "farmacia"])
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON
    registrar_log(f"***** Cliente {cliente1.nombre} guardado en clientescompras.json")   
    print(cliente1)    
    print("Cantidad de Categorias de Interes", len(cliente1))
    cliente1.imprimir_datos()
    cliente1.mostrar_historial()


# Funcion para crear solo un cliente, guardarlo, mostrar datos e historial de compras
# realizar 2 compras, calcular total gastado y volver a mostrar historial de compras
def generar_compra():
    registrar_log("***** Creando Cliente para generar compra.")    
    cliente1 = Cliente("Marcos", "Diago", "DNI", 19031443, "marcos@diago.com", 54, "Quiros Nro 9600", ["tecnologia", "cocina", "juegos"])
    registrar_log(f"***** Cliente {cliente1.nombre} guardado en clientescompras.json")
    print(cliente1)    
    print("Cantidad de Categorias de Interes", len(cliente1))    
    cliente1.imprimir_datos()
    cliente1.mostrar_historial()
    
    # Simular compra
    registrar_log("*** Creando Compra.")
    cliente1.comprar("Laptop", "Negociotres", 350.0)

    registrar_log("*** Creando Compra.")
    cliente1.comprar("Perfume", "TiendaUno", 210.0)

    cliente1.calcular_total_gastado()
    
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON
    registrar_log(f"***** Compra {cliente1.historial_compras} para {cliente1.nombre} guardada en clientescompras.json")

    cliente1.mostrar_historial()
    

# Funcion para crear solo un cliente, guardarlo, mostrar longtud de categorias de interes, mostrar datos
# agregar 5 categorias de interes de los cual 1 es repetido, volver a mostrar datos y longitud de categorias.
def agregar_categoria_interes():
    registrar_log("***** Creando Cliente.")    
    cliente1 = Cliente("Norma", "Maston", "DNI", 14658932, "norma@norma.com", 32, "Vidal Nro 350", [])
    print(cliente1)    
    print("Cantidad de Categorias de Interes", len(cliente1))
    cliente1.imprimir_datos()

    registrar_log(f"***** Ingresando Categorias de Interes a {cliente1.nombre}.")
    cliente1.agregar_interes("perfumes")
    cliente1.agregar_interes("bazar")
    cliente1.agregar_interes("cocina")
    cliente1.agregar_interes("hogar")
    cliente1.agregar_interes("bazar")
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON
    registrar_log(f"***** Cliente {cliente1.nombre} guardado en clientescompras.json")   
    print(cliente1)    
    print("Cantidad de Categorias de Interes", len(cliente1))


# Funcion para crear dos clientes, guardarlo, mostrar longtud de categorias de interes, mostrar datos
# calcular precio final de cada cliente creado por si posee descuento por ser parte del staff.
# PRecio calculado no se guarda en json
def calcular_precio_final():
    registrar_log("***** Creando Cliente.")    
    cliente1 = Cliente("Ignacio", "Parrot", "DNI", 19650350, "ignacio@parrot.com", 29, "Misiones Nro 128", [])
    print(cliente1)    
    print("Cantidad de Categorias de Interes", len(cliente1))
    cliente1.calcular_precio_final(2500.0)
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON

    registrar_log("***** Creando Cliente.")    
    cliente2 = Cliente("Mariano", "Rodd", "DNI", 24320350, "mariano@rodd.com", 32, "Calle 14 Nro 32", [], es_staff = True)
    print(cliente2)    
    print("Cantidad de Categorias de Interes", len(cliente2))
    cliente2.calcular_precio_final(5400.0)
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON

# Funcion para comprobar si es valido el correo electronico ingresado
def comprobar_correoe():    
    correo = "test@mail.com"
    print(f"El correo {correo} es valido?:", Cliente.validar_email(correo))

    correo = "testarrobmail.com"
    print(f"El correo {correo} es valido?:", Cliente.validar_email(correo))

    correo = "www.testmail.com"
    print(f"El correo {correo} es valido?:", Cliente.validar_email(correo))


# Funcion para mostrar clientes creados
def mostrar_clientes_creados():
    print(f"Clientes creados: {Cliente.obtener_total_clientes()}")

# Funciona para crear cliente en zona
def crear_cliente_zona():
    cliente1 = ClienteZona(nombre="Martin", apellido="Hernandez", tipodoc="DNI", nrodoc="12345678",
        email="martin@mail.com", edad=30, domicilio="Av. Siempre Viva 123", intereses=["tecnologia", "deportes"], 
        zona="Cordoba", es_staff=True
    )
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON
    print(cliente1)
    cliente1.imprimir_datos()
    # Mostrar historial de compras
    cliente1.mostrar_historial()

    # Hacer una compra estando en la misma zona
    #cliente1.comprar("Laptop Gaming", "Tech Store", 1500, ubicacion_cliente="Cordoba")
    cliente1.comprar("Laptop Gaming", "Tech Store", 1500)

    cliente1.calcular_total_gastado()

    # Hacer una compra fuera de la zona
    cliente2 = ClienteZona(nombre="Claudia", apellido="Horo", tipodoc="DNI", nrodoc="98766789",
        email="claudia@mail.com", edad=30, domicilio="Av. Septiembre 321", intereses=["tecnologia", "deportes"], 
        zona="Saldan", es_staff=False
    )
    clientes.append(cliente1)  # lo agregamos a la lista en memoria
    guardar_clientes_json(clientes)  # lo guardamos en archiv JSON
    print(cliente2)
    cliente1.imprimir_datos()
    cliente1.mostrar_historial()
    
    #cliente2.comprar("Smartphone", "Mobile Shop", 800, ubicacion_cliente="Rosario")
    cliente2.comprar("Smartphone", "Mobile Shop", 800)

    # Ver cuánto gastó en total
    cliente2.calcular_total_gastado()

# Funcion para mostrar Datos
def mostrar_datos():
    registrar_log("***** Mostrar Datos.")

    # Cargar clientes desde el archivo JSON
    clientes_guardados = cargar_clientes_json()

    if not clientes_guardados:
        print("***** No hay clientes registrados.")
        registrar_log("No se encontraron clientes en el archivo JSON.")
    else:
        registrar_log("***** Listado de clientes registrados.")
        print("\nListado de clientes registrados:\n")
        for i, cliente in enumerate(clientes_guardados, 1):
            print(f"--- Cliente #{i} ---")
            # Si cargar_clientes_json devuelve objetos Cliente:
            if isinstance(cliente, Cliente):
                cliente.imprimir_datos()
                cliente.mostrar_historial()
            else:
                # Si devuelve diccionarios, mostramos manualmente
                print(f"Nombre: {cliente['nombre']} {cliente['apellido']}")
                print(f"Email: {cliente['email']}")
                print(f"Edad: {cliente['edad']}")
                print(f"Domicilio: {cliente['domicilio']}")
                print(f"Intereses: {', '.join(cliente['intereses'])}")
                print(f"Historial de compras: {cliente.get('historial_compras', [])}")
            print()


#Funcion Principal para opciones de menu
def principal():
    """Función principal del programa."""
    while True:        
        mostrar_banner()
        mostrar_menu_principal()
        
        try:
            registrar_log("********* Menu: Esperando Seleccion de Opciones.")
            opcion = input("\n>> Seleccione una opción (0-9): ").strip()
            
            if opcion == "1":                
                limpiar_pantalla()                
                registrar_log("************ Menu, Opcion #1 elegida.")
                registrar_log("*************** ingresando a Modulo Usuario.")
                # Usar el sistema de usuarios del modulo PreEntrega I
                menu()
                registrar_log("*************** regresando a Aplicacion principal.")
                limpiar_pantalla()              
            elif opcion == "2":                
                registrar_log("************ Menu, Opcion #2 elegida.")
                crear_cliente()                
            elif opcion == "3":               
                registrar_log("************ Menu, Opcion #3 elegida.")
                generar_compra()                
            elif opcion == "4":                
                registrar_log("************ Menu, Opcion #4 elegida.")
                agregar_categoria_interes()                
            elif opcion == "5":                
                registrar_log("************ Menu, Opcion #5 elegida.")                
                calcular_precio_final()
            elif opcion == "6":                
                registrar_log("************ Menu, Opcion #6 elegida.")                
                comprobar_correoe()
            elif opcion == "7":                
                registrar_log("************ Menu, Opcion #7 elegida.")                
                mostrar_datos()  
            elif opcion == "8":                
                registrar_log("************ Menu, Opcion #8 elegida.")                
                mostrar_clientes_creados()
            elif opcion == "9":                
                registrar_log("************ Menu, Opcion #9 elegida.")                
                crear_cliente_zona()
            elif opcion == "0":
                #limpiar_pantalla()
                print("Saliendo del Sistema de Modelamiento de Clientes. Proyecto Python. CoderHouse")                
                registrar_log("************ Menu, Opcion #0 elegida.")
                registrar_log("* Aplicacion: Fin.")                
                registrar_log("------------------------------------------------------------\n")
                break
            else:
                print(" Opción no válida. Seleccione entre 0-9.")
                input(" Presiona ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n Saliendo del programa...")
            registrar_log("* Aplicacion: Fin.")                
            registrar_log("------------------------------------------------------------\n")            
            break
        except Exception as e:
            registrar_log(f"Error inesperado: {e}")
            print(f"Error inesperado: {e}")
            input("Presiona ENTER para continuar...")



if __name__ == "__main__":
    
    # Limpiamos pantalla
    limpiar_pantalla()

    # Mostrar información del proyectos
    print(__doc__)

    # Mostramos ruta de archivo en ejecucion
    print(f"Aplicacion principal: {ruta_app_ejecucion}")

    if len(sys.argv) > 1:
        print(f"Argumentos: {str(sys.argv[1])}") 
    else:
        print(f"Argumentos de la Aplicacion: Sin Argumentos")

    # Inicio proceso principal    
    principal()


#Recursos:
# https://www.asciitable.com/
# ASCII: ┌ ┘─ ├ ┬ ┴ └ ┐ ┤ │ ┼

#python .\C8_TPII_ModeloDeClientes+HernandezMartinv7d\main.py

#python C:\Proyectos\6_Python\CursoPython\C8_TPII_ModeloDeClientes+HernandezMartinv7d\main.py

#Objetivos:
#[x] Demostrar la comprensión de los conceptos de “Clases” y “Objetos”
#[x] Ejecutar correctamente el uso de paquetes y librerías.
# 
# 
#Consigna:
#[x] Crear un programa que permita el modelamiento de Clientes en una página de compras con POO y aprendido en Clase.
#[x] Uso correcto de atributos y métodos.
#[x] Crea un paquete redistribuible con el programa creado. 
#[x] Se debe entregar todo el programa.
#
#  
#Requisitos:
#[x] Clases (para cliente),
#[x] Atributos de instancia (opcional alguno de clase)
#[x] Métodos (por fuera de los magic methods)
#[x] Uso de módulos/paquetes
#[x] Generación de paquete redistribuible
# 
# 
#Recomendaciones:
#[x] La Clase Cliente debe tener mínimo 4 atributos.
#[x] Se debe utilizar el método __init__, para definir uno o más de los atributos del punto anterior.
#[x] Se debe utilizar el método __str__() para darle nombre a los objetos.
#[x] Aparte, genera 2 métodos por fuera de los magic methods.
#[x] Para crear el paquete distribuible también como adicional el archivo de la Pre entrega #1.
# 
# 
#Formato:
#[x] El proyecto debe ser un archivo comprimido del paquete. Formatos aceptados: .zip o .tar.gz
#    bajo el nombre“TuModeloDeClientes+Apellido”
# 
#Contenidos adicionales: Estos contenidos adicionales no se incluyen en los criterios de evaluación,
#son optativos, pero si te gustaría agregar valor a tu proyecto. Solo ten en cuenta que aquello que incluyas debe funcionar correctamente:
#[x] Uso de herencia
#[x] Uso de archivos