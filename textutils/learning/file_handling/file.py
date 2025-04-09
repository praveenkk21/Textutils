

# file = open('C:/Users/pkumarb/Downloads/personal/py/file_handling/test.txt','a')
# file.write(" Yes i am mari")

# file= open('C:/Users/pkumarb/Downloads/personal/py/file_handling/test.txt','r')
# content=file.read()
# print(content)
# file.close()


import os

file_path = "C:/Users/pkumarb/Downloads/personal/py/file_handling/test.txt"

# Check if file exists
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")
