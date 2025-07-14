#assignment 4 part 1: Read a File and Handle Errors

with open('sample.txt','r') as file:
    file1=file.read()
    print(file1)
    file.close()
try :
    file=open('sample.txt','r')
    file1 = file.read()
    print(file1)
    file.close()

except FileNotFoundError :
    print('Error : the file sample.txt was not found')

#assignment 4 part 2 : Write and Append Data to a File

file1 = open('sampl.txt','w')
file=file1.write('hello, python ''!')
file1.close()

file1 = open('sample.txt','a')
file=file1.write('learning file handeling in python')
file1.close()

file1 = open('sampl.txt','r')
file=file1.read()
print(file)
file1.close()










