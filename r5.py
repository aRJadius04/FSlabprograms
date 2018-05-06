i1 = []
cnt = -1

class student:
    def __init__(self,usn,name,sem):
        self.usn=usn
        self.name=name
        self.sem=sem
    def pack(self,file):
        global cnt,i1
        pos=file.tell()
        buf=self.usn+"|"+self.name+"|"+self.sem+"|"
        buf+="\n"
        file.write(buf)
        cnt+=1
        i1.append(index(self.usn,pos))
        i1.sort(key = lambda x:x.usn)

class index:
    def __init__(self,usn,addr):
        self.usn=usn
        self.addr=addr

def create_index():
    global cnt, pos, i1
    pos = 0
    try:
        with open("record5.txt","r") as fp:
            line = fp.readline()
            while line:
                if line.startswith('*') or len(line) == 0:#if the record is deleted, dont add to index and read the next record
                    line = fp.readline()
                    pos = fp.tell()
                else:
                    fields=line.strip('\n').split("|")[:-1]
                    i1.append(index(fields[0], pos))
                    pos = fp.tell()
                    cnt += 1
                line = fp.readline() #needed since when we delete, extra blank line is present at the end of the file
        i1.sort(key = lambda x:x.usn)#sort index list based on usn
#        for y in i1:#to check if i1 is correct when prog. closedand opened and if it prints in sorted order
#            print(y.usn,y.addr)
    except:
        pass
    
def find_index(usn_srch):
    ind = -1
    for i in range(cnt+1):
        if i1[i].usn == usn_srch:
            ind = i
    return ind

def search():
    global i1
    usn_srch = input("Enter the USN of the student to be found")
    ind = find_index(usn_srch)
    if ind == -1:
        print('Record not found')
    else:
        print('Record found\nUSN|Name|Sem')
        with open("record5.txt","r") as fp:
            fp.seek(i1[ind].addr)
            line = fp.readline()
            print(line.strip('\n'))

def delete():
    global i1,cnt
    usn_srch = input("Enter the USN of the student to be deleted")
    ind = find_index(usn_srch)
    if ind == -1:
        print('Record not found')
    else:
        print('Record deleted')
        print(i1[ind].addr)
        with open("record5.txt","r+") as fp:
            fp.seek(i1[ind].addr)
            fp.write('*')#if a record has *=>means it is deleted
        i1.pop(ind)#remove that element from the index array
        cnt -= 1#reduce the count of the no. of elements

create_index()#has to be called when prog. starts
while True:
    choice = int(input('1.Add a record\n2.Search for a record\n3.Delete a record\n4.Exit\nEnter choice'))
    if choice == 1:
        usn=input("Enter USN")
        name=input("Enter name")
        sem=input("Enter sem")
        s1=student(usn,name,sem)
        with open("record5.txt","a+") as fp:
            s1.pack(fp)
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    else:
        break
    