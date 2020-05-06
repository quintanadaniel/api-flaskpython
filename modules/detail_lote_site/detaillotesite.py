from config.database import OracleDB

ora = OracleDB()


def getdetaillotesite(id_lote):
    sqlString ="""select id_lote,
                         site,
                         id_item,
                         case when start_time is null then to_date('2100/01/01','yyyy/mm/dd') else start_time end start_time,
                         case when price is null then 0.00 else price end price,
                         case when descripcion is null then ' ' else descripcion end descripcion,
                         case when nickname is null then ' ' else nickname end nickname,
                         case when name is null then ' ' else name end name,
                         case when categoria is null then ' ' else categoria end categoria
                    from meli1.detalle_lote_site dls"""
    if id_lote is not None :
        sqlString = sqlString+" where id_lote = {} ".format(id_lote)

    sqlString = sqlString+ " order by ID_LOTE"
    l_detaillotesite = searchDetailLoteSite(sqlString)
    print (l_detaillotesite)
    return l_detaillotesite

def searchDetailLoteSite(sqlString):
    connect = ora.connect()
    res = connect.execute(sqlString)
    data_detaillotesite = res.fetchall()
    ora.connection_close()
    return data_detaillotesite