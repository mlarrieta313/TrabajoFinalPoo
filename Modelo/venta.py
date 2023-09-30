class Venta:
    
    def __init__(self, id, nro_venta, fecha_venta, id_cliente, nombre_cliente):
        self.__id_venta = id
        self.__nro_venta = nro_venta # correspode al nro de factura que se auto genera ej, N° xxxx-xxxxxxxx
        self.__fecha_venta = fecha_venta
        #self.__tipo_factura = tener en cuenta este atributo para diferenciar en el caso de tener herencia con presupuesto
        self.__nombre_distribuidora = 'Clean Stock'
        self.__domicilio_distribuidora = " "
        self.__telefono_distribuidora = " "
        self.__correo_electronico_dist = " "
        self.__cuit_distribuidora = " "
        self.__id_cliente = id_cliente
        self.__nombre_cliente = nombre_cliente
        