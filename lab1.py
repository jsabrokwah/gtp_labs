
import os
import shutil
import requests
from datetime import datetime

if os.path.exists('joseph_senior_abrokwah'):
   try:
        shutil.rmtree('joseph_senior_abrokwah')
        print(f"Directory '{'joseph_senior_abrokwah'}' has been removed successfully.")

   except Exception as e:
        print(f"Error: {e}")

# Create a new directory
download_folder = 'joseph_senior_abrokwah'

if not os.path.exists('joseph_senior_abrokwah'):
    os.makedirs(download_folder)
    print(f"Directory '{'joseph_senior_abrokwah'}' created.")

local_file_path = os.path.join(download_folder, 'joseph_senior_abrokwah.txt')

# Download the file
url = 'https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt'

response = requests.get(url)

if response.status_code == 200:
    print('File successfully downloaded.')
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
    print('File saved successfully.')
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

#Take User input
user_input = input("Describe what you have learned so far in a sentence:\n ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(local_file_path, 'w') as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print('File successfully modified.')

#Display the content of the modified file
with open(local_file_path, "r") as file:
    print("\nYou Entered: ", end=' ')
    print(file.read())











