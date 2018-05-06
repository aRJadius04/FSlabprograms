s=[]
class student:
    def __init__(self,usn,name,sem):
        self.usn=usn
        self.name=name
        self.sem=sem
    def display_data(self):
        print("\nUSN:"+self.usn+"\nNAME:"+self.name+"\nSEM:"+self.sem)   
    def pack(self,file):
        buf=self.usn+"|"+self.name+"|"+self.sem+"|"
        buf+="\n"
        file.write(buf)
def unpack():
    with open("Out3.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n').split("|")[:-1]#[:-1] is needed to not include last | char
            s.append(student(fields[0],fields[1],fields[2]))          
while True:
    choice=input("1.Insert a record\n2.Search and Modify a record\n3.Exit\nEnter your choice")
    if choice=='1':
        usn=input("Enter USN")
        name=input("Enter name")
        sem=input("Enter sem")
        temp=student(usn,name,sem)
        with open("Out3.txt","a+") as fp:
            temp.pack(fp)
    elif choice=='3':
        break
    elif choice=='2':
        s=[]
        unpack()
        usn_srch=input("Enter the usn to search and modify")
        for x in s:
            if usn_srch==x.usn:
                print("Record found")
                ch=input("Select the field to modify\n1.Name\n2.Sem")
                if ch=='1':
                    newname=input("Enter the new name")
                    x.name=newname
                elif ch=='2':
                    newsem=input("Enter the new sem")
                    x.sem=newsem
        with open("Out3.txt","w+") as fp:
#            fp.seek(0)
#            fp.truncate()
            for x in s:
                x.pack(fp)
    else:
        print("Invalid Input")
        
        
               
        

       