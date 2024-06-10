import os
import requests

from sqlalchemy import create_engine, text
from sqlalchemy.engine import url

import requests

# Send a GET request
response = requests.get(
    'https://cockroachlabs.cloud/clusters/3263bee0-49b6-4ac3-84c6-19f69cb4398d/cert'
)

import os
import requests

import pathlib

# current working directory

print(
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
)
print(pathlib.Path().absolute())

#os.chdir('/home')

print(pathlib.Path().absolute())

#base_url= os.environ.get('/$Home/postgresql/root.crt')

# Save the response content to a file (use 'wb' for binary files like images, PDFs, etc.)
with open("root.crt", 'w') as file:
    file.write(response.text)



check= open('root.crt', 'r')

print('check', check)

DATABASE_URL = 'cockroachdb://murphy15713_outlook_:SdJjsfiDs3HNjdkZ11LM6A@spore-whippet-14967.7tt.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=root.crt'

print(DATABASE_URL)
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)
conn = engine.connect()

res = conn.execute(text("SELECT now()")).fetchall()
print(res)

res1 = conn.execute(text("SELECT * from jobs")).fetchall()
print(res1)

result_dics = []

for row in res1:
    result_dics.append(row._asdict())

print(result_dics)
