import os

file_path = 'c:\\users\\bruce\\Downloads\\dotnet-sdk-7.0.202-win-x64.exe'

print(file_path)

if os.path.isfile(file_path):
  os.remove(file_path)
  print("File has sucessfully been deleted")
else:
  print("this file does not exists!!!")