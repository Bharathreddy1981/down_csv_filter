
def fill(connection,value):
    cursor= connection.cursor()
    w = "select * from student where studentname like '"+ str('%'+value+'%') +"'"

    cursor.execute(w)
    bha = cursor.fetchall()


    return bha

