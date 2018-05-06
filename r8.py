lst = []

#sort function
for i in range(4):
    with open('n'+str(i+1)+'.txt') as fp:
        list1 = fp.read().split('\n')        
    list1.sort()
    with open('ns'+str(i+1)+'.txt','w') as fp:#to sort and store the files
        for x in list1:
            fp.write(x+'\n')

files = ["ns1.txt", "ns2.txt","ns3.txt","ns4.txt"]#list of all the sorted files

fhandler = []#list of the active filehandlers
for f in files:
    fhandler.append(open(f,'r'))
    
lines = []#read the first name from each file and store in list
for fh in fhandler:
    lines.append(fh.readline())

while len(fhandler) > 0:#while there are still files to be read
    smallest = min(lines)#find the smallest name
    smallestposition = lines.index(smallest)#find the file which has the smallest name
    lst.append(smallest)#append the smallest name in o/p list
    lines[smallestposition] = fhandler[smallestposition].readline()#and keep reading from that file
    if lines[smallestposition] == "":#if the file has been read completely
        fhandler.pop(smallestposition)#pop that file handler as it isnt needed
        lines.pop(smallestposition)#pop it from the lines file
print('Merged List:')
for names in sorted(set(lst)):#since set is unordered
    print(names.strip('\n'))