import red

from flask import send_file
def read():


    #path=red.csv
    path = "C:/Users/vanga/PycharmProjects/first project/yellow.csv"
    return send_file(path, as_attachment=True)

