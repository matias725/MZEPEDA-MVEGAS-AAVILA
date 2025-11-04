#Creamos la Clase Tipo Usuario
class TipoUsuario:
    #Creamos el constructor
    def __init__(self,descripcion):
        self.descripcion=descripcion
    
    def __str__(self):
        return "Descripción: {}".format(self.descripcion)
    