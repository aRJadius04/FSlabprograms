rrn=[-1]
cnt=0
class student:
    def __init__(self,usn,name,sem):
        self.usn=usn
        self.name=name
        self.sem=sem
    def display_data(self):
        print("\nUSN:"+self.usn+"\nNAME:"+self.name+"\nSEM:"+self.sem)   
    def pack(self,file):
        global cnt
        pos=file.tell()
        buf=self.usn+"|"+self.name+"|"+self.sem+"|"
        buf+="\n"
        file.write(buf)
        cnt+=1
        rrn.append(pos)
def unpack(pos):
    with open("record.txt","r") as fp:
        fp.seek(pos)
        line=fp.readline()
        fields=line.strip('\n').split("|")[:-1]
        s1=student(fields[0],fields[1],fields[2])
        s1.display_data()
def find_rrn():
    global cnt,pos,rrn
    pos=0
    try:#try is needed since otherwise, if record is empty, it will give an error
        with open("record.txt","r+") as fp:
            line = fp.readline()
            while line:
                rrn.append(pos)
                pos=fp.tell() #returns the location of the next line
                cnt+=1
                line = fp.readline()
    except:
        pass
'''def find_rrni():
    global cnt,pos,rrn
    pos=0
    i=1
    try:
        with open("record.txt","r+") as fp:
            for line in fp:
                rrn.append(pos)
                pos+=len(line)+i
                cnt+=1
                i+=1
                #print(line)
    except:
        pass'''
find_rrn()
while True:
    choice=input("1.Insert a record\n2.Search for a record using RRN\n3.Exit\nEnter your choice")
    if choice=='1':
        usn=input("Enter USN")
        name=input("Enter name")
        sem=input("Enter sem")
        temp=student(usn,name,sem)
        with open("record.txt","a+") as fp:
            temp.pack(fp)
    elif choice=='3':
        break
    elif choice=='2':
        print(cnt)
        rrn_srch=int(input("Enter the RRN to be found"))
        if rrn_srch>cnt or rrn_srch<0:
            print("Invalid RRN")
            continue
        print("Record found")
        pos=rrn[rrn_srch]
        with open("record.txt","r") as fp:
            unpack(pos)
    else:
        print("Invalid Input")
        
        