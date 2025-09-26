# -*- coding: utf-8 -*-
"""
***************************************************************
* Modulo Persistencia - Sistema de Modelado de Clientes       *
*                                                             *
* @author: Martin Hernandez                                   *
* Ultima Modificacion: 24/09/2025                             *
***************************************************************
"""

from paq_modulos_app.modcliente import Cliente
import json
import os

# Ruta directorio actual
ruta_directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Bajar un nivel
ruta_directorio_json = os.path.dirname(ruta_directorio_actual)
# Agregar carpeta "persistencia"
ruta_persistencia_json = os.path.join(ruta_directorio_json, "persistencia")
# nombre de archivo para la persistencia
archivo_json = "clientescompras.json"
# ruta definitiva para gurdar datos json en persistencia de archivo
ruta_json = os.path.join(ruta_persistencia_json, archivo_json)


# Funcion para guardar cliente creado en archivo json.
def guardar_clientes_json(lista_clientes, ruta_archivo=ruta_json):
    """Guarda una lista de clientes en un archivo JSON."""
    
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump([c.clase_cliente_a_diccionario() for c in lista_clientes], f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar clientes: {e}")
        

# Funcion para cargar desde archivo json, los clientes creados.
# Si existen datos se cragan, sino devuelve lista vacia.
def cargar_clientes_json(ruta_archivo=ruta_json):
    """Carga clientes desde un archivo JSON y devuelve una lista de objetos Cliente."""

    if not os.path.exists(ruta_archivo):
        # Si no existe, devolvemos lista vacia
        return []
    
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            
            # Si el archivo esta vacio, el json.load mostrara error de JSONDecodeError
            if os.path.getsize(ruta_archivo) == 0:
                return []

            data = json.load(f)            
            return [Cliente.clase_cliente_desde_diccionario(item) for item in data]            
    except json.JSONDecodeError as e:
        print(f"Error al leer JSON: {e}. Se devolverá lista vacía.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar clientes: {e}")
        return []
