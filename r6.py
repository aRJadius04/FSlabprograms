i2 = []
cnt = -1
class student:
    def __init__(self,usn,name,sem):
        self.usn=usn
        self.name=name
        self.sem=sem
    def pack(self,file):
        global cnt,i2
        pos=file.tell()
        buf=self.usn+"|"+self.name+"|"+self.sem+"|"
        buf+="\n"
        file.write(buf)
        cnt+=1
        i2.append(sec_index(self.usn,self.name,pos))
        i2.sort(key = lambda x:x.name)

class sec_index:
    def __init__(self,usn,name,addr):
        self.usn=usn
        self.name=name
        self.addr=addr

def create_index():
    global cnt, pos, i2
    pos = 0
    try:
        with open("record6.txt","r") as fp:
            line = fp.readline()
            while line:
                if line.startswith('*') or len(line) == 0:#if the record is deleted, dont add to index and read the next record
                    line = fp.readline()
                    pos = fp.tell()
                else:
                    fields=line.strip('\n').split("|")[:-1]
                    i2.append(sec_index(fields[0], fields[1], pos))
                    pos = fp.tell()
                    cnt += 1
                line = fp.readline() #needed since when we delete, extra blank line is present at the end of the file
        i2.sort(key = lambda x:x.name)#sort index list based on usn
#        for y in i2:#to check if i1 is correct when prog. closedand opened and if it prints in sorted order
#            print(y.usn,y.addr)
    except:
        pass
    
def find_sec(name_srch):
    global find_cnt,found,indexnums
    find_cnt = 0
    indexnums = []
    found = []
    for ind, i in enumerate(i2):#enumerate=>to obtain index and val in same loop
        if i.name == name_srch:
            found.append(i)
            indexnums.append(ind)#array of the indices=> will be needed in delete
            find_cnt += 1

def search():
    global i2, found, find_cnt
    name_srch = input("Enter the name of the student to be searched")
    find_sec(name_srch)
    if find_cnt == 0:
        print('Record not found')
    elif find_cnt == 1:
        print('One record found')
        ch = 0
    else:
        print('Multiple records found')
        for i in range(find_cnt):
            print(i, "USN="+found[i].usn)
        ch = int(input('Enter choice:'))
        if ch > find_cnt:
            print('Invalid range')
            return
    print('USN|Name|Sem')
    with open("record6.txt","r") as fp:
        fp.seek(found[ch].addr)
        line = fp.readline()
        print(line.strip('\n'))

def delete():
    global i2, find_cnt, found, indexnums, cnt
    name_srch = input("Enter the name of the student to be deleted")
    find_sec(name_srch)
    if find_cnt == 0:
        print('Record not found')
    elif find_cnt == 1:
        print('One record found')
        ch = 0
    else:
        print('Multiple records found')
        for i in range(find_cnt):
            print(i, "USN="+found[i].usn)
        ch = int(input('Enter choice:'))
        if ch > find_cnt:
            print('Invalid range')
            return
    print('Record deleted')
    with open("record6.txt","r+") as fp:#r+ means read and write. stream positioned at beginning of file=>so we can use seek unlike a+
        fp.seek(found[ch].addr)
        fp.write('*')#if a record has *=>means it is deleted
    i2.pop(indexnums[ch])#remove that element from the index array
    cnt -= 1#reduce the count of the no. of elements

create_index()#has to be called when prog. starts
while True:
    choice = int(input('1.Add a record\n2.Search for a record\n3.Delete a record\n4.Exit\nEnter choice'))
    if choice == 1:
        usn=input("Enter USN")
        name=input("Enter name")
        sem=input("Enter sem")
        s1=student(usn,name,sem)
        with open("record6.txt","a+") as fp:
            s1.pack(fp)
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    else:
        break
    