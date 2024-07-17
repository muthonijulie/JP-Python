#filenotfounderror
try:
      with open('nonexistent_file.txt', 'r') as file:
          content = file.read()

except FileNotFoundError:
      print("The file does not exist.")
except IOError:
      print("An I/O error occurred.")

#IO error-raised when I/O operations fail
try:
      with open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/write.txt', 'a') as file:
          content = file.read()
except FileNotFoundError as fnf_error:
      print(fnf_error)
except IOError as io_error:
      print(io_error)

#finally ensures that the file closes
try:
      file = open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/write.txt', 'r')
      content = file.read()
except Exception as e:
      print(e)
finally:
      file.close()

