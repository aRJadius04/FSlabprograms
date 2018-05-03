count=int(input("Enter the no. of names"))
outfile=input("Enter the output file name")
foutp=open(outfile,'w+')
for i in range(count):
    name=input("Enter the name:")
    foutp.write(name[::-1]+'\n')
foutp.close()