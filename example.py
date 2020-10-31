
from flask import Flask,jsonify
from database_upload import database_conn,csv_file,filter_database,download_csv_file_database,upload_s3_bucket1

example = Flask(__name__)
@example.route("/vbr/<value>", methods=["GET"])
def data(value):
    name = 'yellow.csv'
    connection = database_conn.read()
    file=csv_file.csv(name,value,connection)
    base=upload_s3_bucket1.upload(file)
    return jsonify(base)

@example.route("/filter/<info>", methods=["GET"])
def fun(info):
    connection = database_conn.read()
    name=filter_database.fill(connection,info)
    return jsonify(name)


@example.route("/loaddown", methods=["GET"])
def down():

    #csv_file_down=csv_file.csv()
    final=download_csv_file_database.read()
    return final


if __name__=="__main__":
   example.run(host='0.0.0.0')

