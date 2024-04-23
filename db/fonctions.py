
import psycopg2
import requests

import config_local as config


# Gestion des tables 
################################################

def connection_db():
    try : 
        conn = psycopg2.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password,
            port = 5432
            # options=config.options
        )
        print(f"success to connect with db at :{config.host}") 

    except Exception as e  : 

        print(f"fail to connect with db: \n {e}")

    return conn,conn.cursor()

def save_and_stop_connection(conn,cur):
    conn.commit() 
    cur.close()
    conn.close()
    print("connection closed to db ")


# Suppression 
def drop (table,cursor):

    print(f"dropping {table}: ",end="")
    try : 

        cursor.execute(f"DROP TABLE {table} ;")

        print("no more table at this name")
        
    except Exception as e  : 

        print("fail to drop: ",e)


def table_existance (table) :

    conn,cur=connection_db()

    try : 

        cur.execute(f"SELECT * FROM {table};")
        result=cur.fetchone()

        if len(result)>0 : 
            return "true"
        
    except : 
        return "false"



# fonction create table 
def create_table (table_name,colonne_name,colonne_type):

    print("create table process beginning")

    conn,cur=connection_db()

    drop(table_name,cur)
    conn.commit()
    
    try : 
        col_name_type=(",").join([f"{d[0]} {d[1]} "  for d in zip(colonne_name,colonne_type)])

        query=f"CREATE TABLE {table_name} ({col_name_type});"

        # Execute a command: this creates a new table
        cur.execute(query)
        conn.commit()
        print(f"{table_name} créé avec succées" )
        

    except Exception as e : 

        print(e)

    save_and_stop_connection(conn,cur)


def insert_many(table_name,col_name,data):

    conn,cur=connection_db()
 
    try : 
        for info in data:

            for i in range(len(info[1])):

                try :
                    
                    value=[info[0]]+list(map(str,info[1][i].values()))

                    cur.execute(f"INSERT INTO {table_name} ({(',').join(col_name)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",value)
                    conn.commit()
                    
                
                except Exception as e  : 
                    print(e)
                    print("fail:\n",[info[0]]+list(map(str,info[1][i].values())) )

                    conn.rollback()
                

        print("insert_many achived without problem")
        conn.commit()
        
        save_and_stop_connection(conn,cur)
          

    except Exception as e : 

        print(e)


# recuperation automatique des noms et types de colonne
def get_colonne (ref): 

    col_type=["int" if type(r)==int else "varchar" for r in ref.values()]
    col_name=list(ref.keys())

    return col_type,col_name


# TODO multi parametre ou formulaire
def search (cursor,location,date):
    date = calibrage (date)

    cursor.execute(f"SELECT * FROM predictions WHERE city_name LIKE '{location}' AND dt = {date} ;")

    data=cursor.fetchone()

    return  data



def get_table (table):

    conn,cur=connection_db()
    cur.execute(f"SELECT * FROM {table};")
    return cur.fetchall()




def calibrage (timestamp) : 
    """
        sert a convertir un timestamp en celle de minuit de la mme journée 
        afin de pouvoir trouver les correspondance dans la base de donnée
    
    """

    import datetime

    # timestamp to datetime 
    date = datetime.datetime.fromtimestamp(int(timestamp))

    # datetime to string
    date_string =  date.strftime('%Y-%m-%d %H:%M:%S')
    
    # date alteration 
    formated_date=date_string[:-8]+"02:00:00"

    # string to datetime 
    date = datetime.datetime.strptime(formated_date, '%Y-%m-%d %H:%M:%S')

    # datetime to stamp 
    return  int(datetime.datetime.timestamp(date))


    


 









