import sys

print("GOing visa stdout")
sys.stdout.write("Another wat to do it ! \n")
x=  input("Read via stdin: ")
print(x)
print("Type in value: ",sys.stdin.readline()[:-1])