
import pandas as pd
def csv(name,value,connection):


    df = pd.read_sql_query("select * from student where id='" + str(value) + "'", con=connection)
    df.to_csv(name, index=False)

    print(df)
    return name

