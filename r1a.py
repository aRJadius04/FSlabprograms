count=int(input("Enter the no. of names"))
for i in range(count):
    name=input("Enter the name:")
    print(name[::-1])#reverses string. ::-1 means it goes from beginning to end with step of -1, so backwards

