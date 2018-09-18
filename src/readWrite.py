from pathlib import Path
input_path = input("Please enter the input file path:")
output_path = input("Please enter the output file path:")
if Path(input_path).is_file()== False:
    print("The path you entered to the input file is invalid or the file has been moved!")
elif Path(output_path).is_file()==False:
    print("The path you entered to the output file is invalid or the file has been moved!")
else: ' if all is well read the contents of the input file, change the case and write it to the output file
    contents = open(input_path,'r').read()
    contents = [char.upper() if char.islower() else char.lower() for char in contents]
    contents = ''.join(contents)
    file = open(output_path,'w')
    file.write(contents)
    file.close()
    'The section below proves that the output file contains the altered input'
    file=open(output_path,'r')
    print(file.read())
    file.close()
