from setuptools import setup

setup(
    name="paq_modulos_app",
    version="3.0.0",
    description="Modelamiento de Clientes en página de compras",
    author="Martin Hernandez",
    author_email="martinh_h18@hotmail.com",
    packages=["paq_modulos_app"],    
)


#Crear paquete:
#Ingresar a la carpeta del proyecto, en cmd:
#cd C:\Proyectos\6_Python\CursoPython\C8_TPII_ModeloDeClientes+HernandezMartinv7d
#ingresar el comando, en cmd:
#python setup.py sdist

#Instalar paquete:
#Ingresar a la carpeta donde se encuentra el paquete .tar.gz, en cmd:
#cd dist
#ingresar el comando, en cmd:
#pip3 install nombre_archivo_paq.tar.gz
#Se instalara en:
#C:\Users\Martin\AppData\Local\pip\cache\wheels\CodigoAleatorio\CodigoAleatorio\CodigoAleatorio\IdCodigo