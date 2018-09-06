file = open("example.txt",'w')
file.write("Hello world!")
file.close()
file = open("example.txt",'r')
print(file.read())
file.close()

