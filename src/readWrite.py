contents = open("example.txt",'r').read()
contents = [char.upper() if char.islower() else char.lower() for char in contents]
contents = ''.join(contents)
file = open("changedFile.txt",'w')
file.write(contents)
file.close()
file = open("changedFile.txt", 'r')
print(file.read())
file.close()
