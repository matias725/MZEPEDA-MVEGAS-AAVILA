from Persistencia.DAO.Conexion import Conexion
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de BD desde variables de entorno
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')

def agregar(c):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """
            INSERT INTO cliente 
            (run, nombre, apellido, direccion, fono, correo, montoCredito, deuda, id_tipo_usuario)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (c.run, c.nombre, c.apellidos, c.direccion, c.fono, 
                  c.correo, c.montoCredito, c.deuda, c.id_tipo_usuario)
        con.ejecuta_query(sql, valores)
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al agregar cliente: {str(e)}")
    finally:
        if con:
            con.desconectar()