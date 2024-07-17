import os
#getting current working directory
# cwd=os.getcwd()
# print(cwd)
#renaming an existing file
#os.rename('write.txt','update.txt')

#os.remove('intro.txt')
#checking if file exists
if os.path.exists('intro.txt'):
      print("File exists.")
else:
      print("File does not exist.")
 