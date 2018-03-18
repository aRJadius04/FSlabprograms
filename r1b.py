infile=input("Enter the input file name")
finp=open(infile,'r')
outfile=input("Enter the output file name")
foutp=open(outfile,'w+')
if not finp or not foutp :
    print("FATAL ERROR")
    exit()
for line in finp:
    foutp.write(line.strip()[::-1]+'\n')#to strip any whitespaces from starting and ending of each line
finp.close()
foutp.close()
