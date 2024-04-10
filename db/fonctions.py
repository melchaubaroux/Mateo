import requests
import psycopg2

import config_azure as config


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
    try : 
        cursor.execute(f"DROP TABLE {table} ;")
        
        print("no more table at this name")
    except Exception as e  : 
        print("fail to drop: ",e)


def table_existance (table) :

    conn,cur=connection_db()
    cur.execute("SELECT * FROM test;")
    result=cur.fetchone()
    try : 
        if len(result)>0 : 
            return "true"
        
    except : 
        return "false"







# fonction create table 
def create_table (table_name,colonne_name,colonne_type):

    conn,cur=connection_db()

    drop(table_name,cur)
    conn.commit()
    
    try : 
        col_name_type=(",").join([f"{d[0]} {d[1]} "  for d in zip(colonne_name,colonne_type)])

        query=f"CREATE TABLE {table_name} ({col_name_type});"
        # Execute a command: this creates a new table
        cur.execute(query)
        conn.commit()
        print("table créé avec succées" )
        

    except Exception as e : 

        print(e)

    save_and_stop_connection(conn,cur)


def insert_many(table_name,col_name,data):

    conn,cur=connection_db()
    
    try : 
        for info in data:

            # value=[info[0]]+list(map(str,info[1][0].values()))
            for i in range(len(info)):

                try :
                    
                    # print("info[0]:", info[0])

                    # print("info[1]:", info[1])

                    value=[info[0]]+list(map(str,info[1][i].values()))
                  


                    print(value)
            

                    # for x in range(len(value)):
                    #     value[x]=value[x].replace("None","")

                
                    cur.execute(f"INSERT INTO {table_name} ({(',').join(col_name)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",value)
                    conn.commit()
                    break
                
                except Exception as e  : 
                    print(e)
                    print("fail:\n",[info[0]]+list(map(str,info[1][i].values())) )

                    conn.rollback()
                break

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
def search (cursor,requete): 

    location=requete['location']
    cursor.execute(f"SELECT * FROM prevision where location like {location};")
    cursor.fetchone()



def get_table (table):

    conn,cur=connection_db()
    cur.execute("SELECT * FROM predictions;")
    return cur.fetchall()


 









