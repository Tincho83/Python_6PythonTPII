# -*- coding: utf-8 -*-
"""
***************************************************************
* Clase Cliente - Modelado de Clientes para pagina de compras *
*                                                             *
* @author: Martin Hernandez                                   *
* Ultima Modificacion: 26/09/2025                             *
***************************************************************
"""

# Elemnto Principal: Objeto
class Cliente:
    """Clase que representa a un cliente del sistema de compras."""
    
    # Atributo de clase.
    contador_clientes = 0

    # Atributo de clase. Encapsulados
    __iva = 0.21
    __descuento_staff = 10.0

    
    # Constructor de la claee con Carcateristics para el Objeto
    def __init__(self, nombre, apellido, tipodoc, nrodoc, email, edad, domicilio, intereses, es_staff=False, incrementar=True):
        """Constructor de Cliente. Inicializa un nuevo cliente."""

        # Atributos de la instancia.
        self.nombre = nombre
        self.apellido = apellido
        self.tipodoc = tipodoc
        self.nrodoc = nrodoc
        self.email = email
        self.edad = edad
        self.domicilio = domicilio
        self.es_staff = es_staff
        self.intereses = intereses if intereses is not None else []
        self.historial_compras = []
        self.saldo_credito = 0.0

        if incrementar:
            # Incrementar contador de clientes de la clase
            Cliente.contador_clientes += 1
            self.id = Cliente.contador_clientes
        else:
            self.id = None  # o lo asignás con lo que venga del JSON


    # Funcionalidades: Metodos Especiales
    
    # Representacion legible (cadena de texto strng) del objeto cliente
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} ({self.email}), Edad: {self.edad}, {self.tipodoc} {self.nrodoc}, Domicilio: {self.domicilio}, Intereses: {self.intereses}, # Cliente Creado: {Cliente.contador_clientes}"

    # Numero de elemntos de un objeto
    def __len__(self):
        return len(self.intereses)

    # Representacion tecnica del objeto Cliente.
    def __repr__(self):
        return f"Cliente('{self.nombre}','{self.email}',{self.edad},{self.intereses})"



    # Funcionalidades: Metodos Personalizados

    # Obtener Datos encapsulados
    def getiva(self):
        return self.__iva

    def getdescuento_staff(self):
        return self.__descuento_staff


    # Metodos varios

    # Funciona para convertir los datos de la clase en diccionario para guardarlo en persistencia json.
    def clase_cliente_a_diccionario(self):
        """Convierte el objeto Cliente en un diccionario serializable."""
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "tipodoc": self.tipodoc,
            "nrodoc": self.nrodoc,
            "email": self.email,
            "edad": self.edad,
            "domicilio": self.domicilio,
            "intereses": self.intereses,
            "historial_compras": self.historial_compras,
            "saldo_credito": self.saldo_credito
        }


    # Funcion mostrar de Datos
    def imprimir_datos(self):
        print(f"El cliente {self.nombre} {self.apellido} de {self.edad} años de edad, con correo {self.email} y domicilio {self.domicilio}, tiene interes en: {self.intereses}")


    # Funcion mostrar historial de compras
    def mostrar_historial(self):
        if not self.historial_compras:
         print(f"{self.nombre} no tiene compras registradas.")
        else:
          print(f"Historial de compras de {self.nombre}:")
          for i, compra in enumerate(self.historial_compras, 1):
            print(f"{i}. {compra['producto']} en {compra['negocio']} - ${compra['precio']} ({compra['fecha']})")


    # Funcion para realizar compra
    def comprar(self, producto, negocio, precio=0.0):
        """Registra una compra del cliente."""

        compra = {
            "producto": producto,
            "negocio": negocio,
            "precio": precio,
            "fecha": self._obtener_fecha_actual()
        }
        if precio > 0.0:
            self.historial_compras.append(compra)
            print(f"{self.nombre} compró {producto} en {negocio} por ${precio}.")


    # Funcion para obtener fecha para realizar compra
    def _obtener_fecha_actual(self):
        """Método privado para obtener la fecha actual simulada."""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y")


    # Funcion para calcular monto de dinero gastado de un cliente
    def calcular_total_gastado(self):
        """Calcula el total gastado por el cliente."""
        total = sum(compra['precio'] for compra in self.historial_compras)
        print(f"{self.nombre} ha gastado un total de: ${total:.2f}")
        return total
    
    # Funcion para agregar categorias de interes a un usuario
    def agregar_interes(self, categoria):
        """Agrega una nueva categoría de interés al cliente."""
        categoria = categoria.lower()
        if categoria not in self.intereses:
            self.intereses.append(categoria)
            print(f"Categoría '{categoria}' agregada a los intereses de {self.nombre}")
        else:
            print(f"{self.nombre} ya tiene interés en '{categoria}'")

    # Funcion para calcular precio final de compra
    def calcular_precio_final(self, monto):
        """Calcula el precio final aplicando descuento si es staff."""
        if self.es_staff:
            monto_final = monto * (1 - Cliente._Cliente__descuento_staff / 100)
            print(f"{self.nombre} es staff: se aplica {Cliente._Cliente__descuento_staff}% de descuento. Precio Final a pagar ${monto_final}")
            return monto_final
        else:
            print(f"{self.nombre} es cliente standart: NO se aplica descuento. Precio Final a pagar ${monto}")
        return monto



    # Funcion con decorador, para evitar tenerla fuera de la Clase

    # Funcion para validar correo electronico ingresado
    @staticmethod
    def validar_email(email):
        """Método estático para validar formato de email."""
        import re
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None


    # Funcion para obtener el total de clientes creados
    @classmethod
    def obtener_total_clientes(cls):
        """Método de clase que retorna el total de clientes creados."""
        return cls.contador_clientes

    # Funcion para convertir los datos del diccionario desde json a clase Cliente para cargarlo.
    @classmethod
    def clase_cliente_desde_diccionario(cls, data):
        """Crea un objeto Cliente a partir de un diccionario."""
        cliente = cls(
            data["nombre"],
            data["apellido"],
            data["tipodoc"],
            data["nrodoc"],
            data["email"],
            data["edad"],
            data["domicilio"],
            data.get("intereses", []),
            es_staff=data.get("es_staff", False),
            incrementar=False
        )
        cliente.id = data.get("id")
        cliente.historial_compras = data.get("historial_compras", [])
        cliente.saldo_credito = data.get("saldo_credito", 0.0)
        return cliente


# Elemnto Heredado ClienteZona: Objeto con Herencia desde Clase Padre (Cliente)
class ClienteZona(Cliente):
    """Calcula envío según ubicación del cliente."""

    # Atributo de clase.
    zona_deposito = "cordoba"
    
    # Definición del constructor de ClienteZona. Inicializa todos los parametros de la clase Cliente como el atributo propio "zona".
    def __init__(self, nombre, apellido, tipodoc, nrodoc, email, edad, domicilio, intereses, zona, es_staff=False):
        
        #super(): Llama al constructor de la clase padre (Cliente.__init__), inicializa todos los atributos definidos en clase Padre Cliente y asi evitar repetir codigo
        super().__init__(nombre, apellido, tipodoc, nrodoc, email, edad, domicilio, intereses, es_staff)
        
        # Atributos de la instancia.
        self.zona = zona

    # Funcion para calcular el costo y tiempo del envio si la compra es para la zona de Cordoba.
    def calcular_envio(self, ubicacion_cliente):
        """Retorna costo y demora segun si el cliente esta en zona de Cordoba."""
        if ubicacion_cliente.lower() == self.zona_deposito.lower():
            return {"costo": 0, "demora": "24hs"}
        else:
            return {"costo": 100, "demora": "72hs"}

    # Funcion para comprar un producto. Permite "ubicacion_cliente" (opcional por defecto en None)
    # Permite comprar usando la zona del cliente registrado o especificar la ubicación al comprar.
    def comprar(self, producto, negocio, precio, ubicacion_cliente=None):

        if ubicacion_cliente is None:
            ubicacion_cliente = self.zona

        envio = self.calcular_envio(ubicacion_cliente)
        total = precio + envio["costo"]

        # aplicar descuento si es staff
        total = self.calcular_precio_final(total)

        super().comprar(producto, negocio, total)
        print(f"Envío: {envio['demora']} (costo ${envio['costo']})")
