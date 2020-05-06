from config.database import OracleDB

ora = OracleDB()

def getlotesite(id_lote):
    sqlString = """SELECT ID_LOTE,
                    NOMBRE_ARCHIVO,
                    ENCODE,
                    EXTENSION,
                    case when SEPARADOR_COLUMNA is null then ' ' else SEPARADOR_COLUMNA end SEPARADOR_COLUMNA,
                    FECHA_INSERCION,
                    case when TIEMPO_INSERCION is null then ' ' else TIEMPO_INSERCION end TIEMPO_INSERCION,
                    ESTADO,
                    case when DETALLE is null then ' ' else detalle end DETALLE
                    FROM meli1.lote_site """
    if id_lote is not None :
        sqlString = sqlString+" where id_lote = {} ".format(id_lote)

    sqlString = sqlString+ " order by ID_LOTE"
    l_lote = searchlote(sqlString)
    print (l_lote)
    return l_lote

def searchlote(sqlString):    
    connect = ora.connect()
    res = connect.execute(sqlString)
    data_lote = res.fetchall()
    ora.connection_close()
    return data_lote