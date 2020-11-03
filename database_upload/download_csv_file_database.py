
from flask import send_file
def read():



    path = "yellow.csv"
    return send_file(path, as_attachment=True)

