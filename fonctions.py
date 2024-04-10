import psycopg2

import config_azure as config



def connection_db():
    try : 
        conn = psycopg2.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password,
            options=config.options
        )
        print(f"success to connect with db at {config.host}") 
    except : 
        print("fail to connect with db")
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



# fonction create table 
def create_table (table_name,colonne_name,colonne_type):

    conn,cur=connection_db()

    drop(table_name,cur)
    conn.commit()
    
    try : 
        col_name_type=(",").join([f"{d[0]} {d[1]} "  for d in zip(colonne_name,colonne_type)])

        query=f"CREATE TABLE test ({col_name_type});"
        # Execute a command: this creates a new table
        cur.execute(query)
        conn.commit()
        print("table créé avec succées" )
        

    except Exception as e : 

        print(e)

    save_and_stop_connection(conn,cur)


def insert_many(table,col_name,data):

    conn,cur=connection_db()
    
    try : 
        for info in data:
            value=list(map(str,info.values()))

            for x in range(len(value)):
                value[x]=value[x].replace("None","0")

            cur.execute(f"INSERT INTO {table} ({(',').join(col_name)}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )",value)

        print("insert_many achived without problem")
        
        save_and_stop_connection(conn,cur)
          

    except Exception as e : 
        conn.rollback()
        print(e)



def get_colonne (ref): 
    col_type=["int" if type(r)==int else "varchar" for r in ref.values()]
    col_name=list(ref.keys())
    
    col_type=(",").join(col_type)
    col_name=(",").join(col_name)

    return col_type,col_name




