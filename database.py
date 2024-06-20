import os

import requests
from sqlalchemy import (
    create_engine,
    text,
)

# Send a GET request
response = requests.get(
    'https://cockroachlabs.cloud/clusters/3263bee0-49b6-4ac3-84c6-19f69cb4398d/cert'
)

import requests

with open("root.crt", 'w') as file:
    file.write(response.text)

DATABASE_URL = os.environ['DB_CONNECTION']

engine = create_engine(DATABASE_URL)

def loaddb ():

    DATABASE_URL = os.environ['DB_CONNECTION']
    
     
    from sqlalchemy import create_engine
    
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    
    #res = conn.execute(text("SELECT now()")).fetchall()
   # print(res)
    
    res1 = conn.execute(text("SELECT * from jobs")).fetchall()
    #print( f'res1 is actually {res1}')
    
    result_dics = []
    
    for row in res1:
        result_dics.append(row._asdict())
    
   # print(result_dics)


    return result_dics






#print (loaddb())






            
        
def load_job_from_db(id):


    DATABASE_URL = os.environ['DB_CONNECTION']


    from sqlalchemy import create_engine

    engine = create_engine(DATABASE_URL)
    conn = engine.connect()

    
    with engine.connect() as conn:
        myparam={"val":id}
        sql=text("SELECT * FROM jobs WHERE jobs.id=:val")
        result=conn.execute(sql, myparam ).fetchall()
        #result=conn.execute(sql, ({'id':'975548584460845000'}))

  
          


  
        rows_dict=[]
        for row in result:
           rows_dict.append(row._asdict())
        return rows_dict
   




print(load_job_from_db(975548584460779521))

 