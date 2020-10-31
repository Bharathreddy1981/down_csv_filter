
#pip install openpyxl module
import pymysql

def read():

    z = pymysql.connect(
                host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
                user="admin",
                passwd="bharath**",
                db="transction_prod"
    )

    return z


