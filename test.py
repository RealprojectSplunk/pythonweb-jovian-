import os
import requests

import pathlib

# current working directory
print(pathlib.Path().absolute())

os.chdir('/home/runner/postgresql')

print(pathlib.Path().absolute())
#cd /home/runner/pythonweb-parayilLLC-/postgresql/

# Save the response content to a file (use 'wb' for binary files like images, PDFs, etc.)
#with open('root.crt', 'w') as file:
#file.write(response.text)  # Use response.content for binary files

#curl  --create-dirs -o  /postgresql/root.crt
#'https://cockroachlabs.cloud/clusters/3263bee0-49b6-4ac3-84c6-19f69cb4398d/cert'
