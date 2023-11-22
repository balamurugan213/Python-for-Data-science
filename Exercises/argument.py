import sys

for i in range(len(sys.argv)):
    if i==0:
        print("Function Name: %s",sys.argv[0])
    else:
        print("%d Argument: %s",i,sys.argv[i])