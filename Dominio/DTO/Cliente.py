class Cliente:
    def __init__(self,run,nombre,apellidos,direccion,fono,correo,
                 id_tipo_usuario,montoCredito=500,deuda=0):
        self.run=run
        self.nombre=nombre
        self.apellidos=apellidos
        self.direccion=direccion
        self.fono=fono
        self.correo=correo
        self.id_tipo_usuario=id_tipo_usuario
        self.montoCredito=montoCredito
        self.deuda=deuda

    def __str__(self):
        return "Run:{}\nNombre:{}\nApellidos:{}\nDireccion:{}\nFono:{}\nCorreo:{}\nTipo de Usuario:{}\nMonto Crédito:${}\nDeuda:${}".format(self.run,self.nombre,self.apellidos,self.direccion,self.fono,
                                                                                                                                            self.correo,self.id_tipo_usuario,self.montoCredito,self.deuda)
    
    def pagar(self,monto):
        if monto>0:
            self.deuda=self.deuda-monto
            print("Monto Pagado: ${}, La Deuda actualizada es:${}".format(monto,self.deuda))
        else:
            print("El monto a pagar debe ser Mayor a 0 :(")