import os

import requests
from sqlalchemy import create_engine, text

from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction, transaction

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






            
        
def load_job_from_db(job_id):


    DATABASE_URL = os.environ['DB_CONNECTION']


    from sqlalchemy import create_engine

    engine = create_engine(DATABASE_URL)
    conn = engine.connect()

    
    with engine.connect() as conn:
        myparam={"val":job_id}
        sql=text("SELECT * FROM jobs WHERE jobs.id=:val")
        result=conn.execute(sql, myparam ).fetchall()
        #result=conn.execute(sql, ({'id':'975548584460845000'}))

  
          


  
        rows_dict=[]
        for row in result:
           rows_dict.append(row._asdict())
        return rows_dict
   




print(load_job_from_db(975548584460779521))


def add_application_to_db(job_id, data):

    DATABASE_URL = os.environ['DB_CONNECTION']
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    Session = sessionmaker(engine)
    session = Session()

    
    with engine.connect() as conn:
      mypara={'job_id':job_id, 'full_name':data['full_name'],
       'email':data['email'],
       'linkedin_url':data['linkedin_url'],
       'education':data['education'],
       'work_experience':data['work_experience'],
       'resume_url':data['resume_url']}
      query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url) ;")
      insert1=conn.execute(query,mypara)
      result = run_transaction(engine, lambda session: session.execute(query))
 

#add_application_to_db(job_id, data)


def add_application_to_db1():
    DATABASE_URL = os.environ['DB_CONNECTION']
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    Session = sessionmaker(engine)
    session = Session()

    with engine.connect() as conn:
           initialdata = conn.execute(text("SELECT * from applications")).fetchall()
           rows_dict=[]
           for row in initialdata:
                 rows_dict.append(row._asdict())
           print('Initial data ')#check initial data in the applications table
           for items in (rows_dict):
                 print( items['job_id'] )
    query = text("INSERT into applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(999999999999999999,'Employee Name','testaccount@gmail.com', 'www.linkedin.com','test data','datawork_experience','www.linkedin.com')  RETURNING id;")
    conn = engine.connect()
    insert= conn.execute(query)
    result = run_transaction(engine, lambda session: session.execute(query))

    afterdata = conn.execute(text("SELECT * from applications")).fetchall()
    rows_dict=[]
    for row in afterdata:
        rows_dict.append(row._asdict())
    print('Afterdata row for data 999999999999999999:  ')# check if it inserted the above row for data 999999999999999999
    for items in (rows_dict):
            print( items['job_id'] )
    
    
    





    
    
    
 
        
        
        
         