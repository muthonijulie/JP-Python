# writing a new sentence to an existing file or a new file
# with open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/write.txt','w') as file:
#     file.write("Hello Work!\n ")

#writing multiple lines using a string
lines=["Hello World!\n","It is very cold\n","Do you have some coffe?\n"]
with open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/write.txt','w') as file:
    file.writelines(lines)
#appends a new line to the end of the file 
with open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/write.txt','a') as file:
  file.write("Add new line to the file")