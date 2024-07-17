#opening files
file=open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/intro.txt','r')
print(file.read())


#with open-closes the file automatically after the block is over
with open('/home/muthoni/Desktop/present/Project/Janja program/Python codes/file handling/intro.txt','r') as file:
    data=file.read()
    print(data)
#read the entire file
    content=file.read()
    print(content)
#readline()-reads one line at a time
    line=file.readline()
    while line:
        print(line,end='')
        line=file.readline()
    
    #readlines()-reads all lines at once
    lines=file.readlines()
    for line in lines:
        print(line,end='')
        #closing files
file.close()

