import cx_Oracle
from sqlalchemy import create_engine
#from decouple import config
from pprint import pprint
import datetime
from flask import jsonify


class OracleDB:
    """
       OracleDB Database
    """
    def __init__(self):
        self.username = 'meli1'
        self.password = 'meli'
        self.hostname = '192.168.0.11'
        self.port = '1521'
        self.sid = 'XE'
        self.engine = None
        self.conn = None
        self.rconn = None
        self.oracle_connection_string = ('oracle+cx_oracle://{username}:{password}@' +
            cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
        )

    def connect(self):
        try:
            self.engine = create_engine(
                self.oracle_connection_string.format(
                    username=self.username,
                    password=self.password,
                    hostname=self.hostname,
                    port=self.port,
                    service_name=self.sid,
                ), pool_size=100)
            self.conn = self.engine.connect()
            self.rconn = self.engine.raw_connection()
            return self.conn
            print("conected...")

        except cx_Oracle.DatabaseError as e:
            self.engine = None
            print(e)
            exit(1)

    def connection_close(self):
        self.conn.close()
        print("Not Conected...")


if __name__ == '__main__':
    ora = OracleDB()
    ora.connect()
    ora.connection_close()