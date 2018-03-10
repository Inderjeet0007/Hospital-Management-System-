import pickle
import os
import time

print'\t\t\t\tWELCOME TO CITY HOSPITAL'
print'\n\t\t\t\tToday\'s Date is :'
print (time.strftime("\n\t\t\t\t\t%d/%m/%Y"))
print '\n\t\t\t\tThe Time You Entered This Page Was :'
print (time.strftime("\n\t\t\t\t\t%H:%M:%S"))
print'\n\n'

class admin:
    def __init__(self):
        self.id0=0
        self.name=''
        self.gender=None
        self.salary=0
        self.timings=0
        
    def storedata0(self):
        self.id0=input('Enter ID :')
        self.name=raw_input('Enter Name:')
        self.gender=raw_input('Enter the Gender : ')
        self.salary=raw_input('Enter the salary : ')
        self.timings=raw_input('Enter the timings : ')
        print '\nData is stored\n'
    def display0 (self):        
        print self.id0,'\t\t',self.name,'\t\t',self.gender,'\t\t',self.salary,'\t\t',self.timings

def create0():
    f=open ('admin.dat','wb')
    n=input('Enter the no. of doctors : ')
    a=admin()
    for i in range (n):
        a.storedata1()
        pickle.dump(a,f)
    f.close()

def append0():

    f=open('admin.dat','wb')
    n=input("Enter the no. of doctors:")
    a=admin()
    for i in range(n):
        a.storedata1()
        pickle.dump(a,f)
    f.close()

def insert0():
    f1=open('admin.dat','w+b')
    f2=open('newfile1.dat','ab')
                        
    a1=admin()
    a1.storedata0()
    end=0                
    try:
        while True:
            a= pickle.load(f1)
            if a1.id0<=a.id:
                pickle.dump(a,f2)
            else :
                end=1
                break
        pickle.dump(a1,f2)
        f1.seek(0)
        while True:
            a= pickle.load(f1)
            if a.id>a1.id0:
                pickle.dump(a,f2)
      
    except EOFError:
        if end==0:
            pickle.dump(a1,f2)
        f1.close()
        f2.close()
    
    os.remove('admin.dat')
    os.rename('newfile1.dat','admin.dat')

def delete0():
    id=input("Enter the id of doctors whose details  to be deleted: ")
    
    f1=open('admin.dat','rb')
    f2=open('newfile1.dat','ab')
    status=0
    
    try:
        while True:
            a= pickle.load(f1)
            if a.id0!=id:
                pickle.dump(a,f2)
            else :
                status=1
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove('admin.dat')
    os.rename('newfile1.dat','admin.dat')
    if status==1:
        print 'record deleted'
    else:
        print 'record not found'

def modify0():
    id=input("Enter the id whose details to be modified : ")
    
    f1=open('admin.dat','rb')
    f2=open('newfile1.dat','ab')
    a=admin()
    status=0

    try:
        while True:
            a= pickle.load(f1)
            if a.id0==id:
                status=1
                a.storedata0()
            pickle.dump(a,f2)
    except EOFError:
        f1.close()
        f2.close()
    
    os.remove('admin.dat')
    os.rename('newfile1.dat','admin.dat')
    if status ==1:
        print 'file modified'
    else:
        print 'record not found '


def search0():
    id=input("Enter the id whose details to be searched : ")
    
    f1=open('admin.dat','rb')
    status=0

    try:
        while True:
            a= pickle.load(f1)
            if a.id0==id:
                status=1
                print 'Id You Have Entered is -', a.id
                print 'Name is  -',a.name
            
    except EOFError:
        f1.close()
    if status==0:
        print 'Recod  Was Not Found'

def display9():
    print'\t\t\t\t\tSTAFF INFO:'
    print 'ID\t\tNAME\t\tGENDER\t\t\tSALARY\t\t\tTIMINGS'
    a=admin()
    f=open("admin.dat","rb")
    
    try:
        while True:
            a= pickle.load(f)
            a.display0()
    except EOFError:
        f.close()
        
class doctor:
    def __init__(self):
        self.id=0
        self.name=''
        self.gender=0
        self.fee=0
        self.timings=0
        
    def storedata1(self):
        self.id=input('Enter ID :')
        self.name=raw_input('Enter Name:')
        self.gender=raw_input('Enter the Gender : ')
        self.fee=raw_input('Enter the fees : ')
        self.timings=raw_input('Enter the timings : ')
        print '\nData is stored\n'
    def display2 (self):
        print self.id,'\t\t',self.name,'\t\t',self.gender,'\t\t',self.fee,'\t\t',self.timings



def create1():
    f=open ('doctor.dat','ab')
    n=input('Enter the no. of doctors : ')
    d=doctor()
    for i in range (n):
        d.storedata1()
        pickle.dump(d,f)
    f.close()

def append1():

    f=open('doctor.dat','ab')
    n=input("Enter the no. of doctors:")
    d=doctor()
    for i in range(n):
        d.storedata1()
        pickle.dump(d,f)
    f.close()

def insert1():
    f1=open('doctor.dat','rb')
    f2=open('newfile1.dat','ab')
                        
    d1=doctor()
    d1.storedata1()
    end=0                
    try:
        while True:
            d= pickle.load(f1)
            if d1.id<=d.id:
                pickle.dump(d,f2)
            else :
                end=1
                break
        pickle.dump(d1,f2)
        f1.seek(0)
        while True:
            d= pickle.load(f1)
            if d.id>d1.id:
                pickle.dump(d,f2)
      
    except EOFError:
        if end==0:
            pickle.dump(d1,f2)
        f1.close()
        f2.close()
    
    os.remove('doctor.dat')
    os.rename('newfile1.dat','doctor.dat')

def delete1():
    id=input("Enter the id of doctors whose details  to be deleted: ")
    
    f1=open('doctor.dat','rb')
    f2=open('newfile1.dat','ab')
    status=0
    
    try:
        while True:
            d= pickle.load(f1)
            if d.id!=id:
                pickle.dump(d,f2)
            else :
                status=1
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove('doctor.dat')
    os.rename('newfile1.dat','doctor.dat')
    if status==1:
        print 'record deleted'
    else:
        print 'record not found'

def modify1():
    id=input("Enter the id whose details to be modified : ")
    
    f1=open('doctor.dat','rb')
    f2=open('newfile1.dat','ab')
    d=doctor()
    status=0

    try:
        while True:
            d= pickle.load(f1)
            if d.id==id:
                status=1
                d.storedata1()
            pickle.dump(d,f2)
    except EOFError:
        f1.close()
        f2.close()
    
    os.remove('doctor.dat')
    os.rename('newfile1.dat','doctor.dat')
    if status ==1:
        print 'file modified'
    else:
        print 'record not found '


def search1():
    global id
    id=input("Enter the id whose details to be searched : ")
    
    f1=open('doctor.dat','rb')
    status=0

    try:
        while True:
            d= pickle.load(f1)
            if d.id==id:
                status=1
                global name
                print 'Id You Have Entered is -', d.id
                print 'Name is  -',d.name
                print 'Fee is -',d.fee
            
    except EOFError:
        f1.close()
    if status==0:
        print 'Recod  Was Not Found'

def display1():

    print 'ID\t\tNAME\t\t\tGENDER\t\t\tFEE\t\t\tTIMINGS'
    d=doctor()
    f=open("doctor.dat","rb")
    
    try:
        while True:
            d= pickle.load(f)
            d.display2()
    except EOFError:
        f.close()
        
        
        
class patient:

    def __init__(self):
        self.id1=0
        self.name1=''
        self.age=None
        self.phone=0
        self.grnder=None
    def storedata(self):
        self.id1=input('Enter ID :')
        self.name1=raw_input('Enter Name & year of registration :')
        self.age=input('Enter Age : ')
        self.phone=input('Enter Patient Telephone number:-')
        self.gender=raw_input('Enter the Gender (M/F) : ')
       
        print 'Data is stored'
    def display (self):
        print self.id1,'\t\t',self.name1,'\t\t',self.age,'\t\t',self.phone,'\t\t',self.gender,'\t\t'
global name1
def create():
    f=open ('patient.dat','ab')
    n=input('Enter the no. of patients : ')
    p=patient()
    for i in range (n):
        p.storedata()
        pickle.dump(p,f)
    f.close()

def append():

    f=open('patient.dat','ab')
    n=input("Enter the no. of patients:")
    p=patient()
    for i in range(n):
        p.storedata()
        pickle.dump(p,f)
    f.close()

def insert():
    f1=open('patient.dat','rb')
    f2=open('newfile.dat','ab')
                        
    p1=patient()
    p1.storedata()
    end=0                
    try:
        while True:
            p= pickle.load(f1)
            if p.id<=p1.id1:
                pickle.dump(p,f2)
            else :
                end=1
                break
        pickle.dump(p1,f2)
        f1.seek(0)
        while True:
            p= pickle.load(f1)
            if p.id>p1.id1:
                pickle.dump(p,f2)
      
    except EOFError:
        if end==0:
            pickle.dump(p1,f2)
        f1.close()
        f2.close()
    
    os.remove('patient.dat')
    os.rename('newfile.dat','patient.dat')

def delete():
    id=input("Enter the id of patient whose details  to be deleted: ")
    
    f1=open('patient.dat','rb')
    f2=open('newfile.dat','ab')
    status=0
    
    try:
        while True:
            p= pickle.load(f1)
            if p.id1!=id:
                pickle.dump(p,f2)
            else :
                status=1
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove('patient.dat')
    os.rename('newfile.dat','patient.dat')
    if status==1:
        print 'record deleted'
    else:
        print 'record not found'

def modify():
    id=input("Enter the id whose details to be modified : ")
    
    f1=open('patient.dat','rb')
    f2=open('newfile.dat','ab')
    p=patient()
    status=0

    try:
        while True:
            p= pickle.load(f1)
            if p.id1==id:
                status=1
                p.storedata()
            pickle.dump(p,f2)
    except EOFError:
        f1.close()
        f2.close()
    
    os.remove('patient.dat')
    os.rename('newfile.dat','patient.dat')
    if status ==1:
        print 'file modified'
    else:
        print 'record not found '


def search():
    id=input("Enter the id of the patient details has to be searched : ")
    global id1
    f1=open('patient.dat','rb')
    status=0

    try:
        while True:
            p= pickle.load(f1)
            if p.id1==id:
                status=1
                print 'Id You Have Entered is -', p.id1
                print 'Name is & year of registration  -',p.name1
            
    except EOFError:
        f1.close()
    if status==0:
        print 'Recod  Was Not Found'

def display():

    print 'ID\t\tNAME & YEAR\t\tAGE\t\tPHONE\t\t\tGENDER'
    p=patient()
    f=open("patient.dat","rb")
    
    try:
        while True:
            p= pickle.load(f)
            p.display()
    except EOFError:
        f.close()
        
    
def test ():
    search()
    global pat_phone
     
    pat_phone=input('Enter Patients Phone Number :\n')
    f1=open("patient.dat","rb")
    status=0

    try:
       while True:
           c= pickle.load(f1)
           if c.phone==pat_phone:
               status=1
               print 'Telephone:', c.phone
               print '\n'
               print 'Name :', c.name1
               print '\n'
               print 'Age :', c.age
               print '\n'
               print 'Gender :', c.gender
               print '\n'
               
    except EOFError:
        f1.close()
    if status==0:
        print 'Patient not found'
    else:
        pass
    print'1-CT scan'
    print'2-blood test'
    test=input('Enter the choice :\n')
    global fee
    global t1
    if test==1:
        t1=250
    elif test==2:
        t1=500
    global total
    fee=input('enter the doctors fee : ')
    total=t1+fee
    print 'Total Amount to be paid =\n',total
    t=input('Press 1 to print bill\n')
    if t==1:
    
        bill()
    else:
        pass
def bill():
    print'\n\n****************************************************** BILL ***************************************************************'
    print'\n\t\t\t\t\t\t City Hospital'
    print'\nPatient phone number:',pat_phone,'\n\n','Doctors fee : ',fee,'\n\n','Cost of test : ',t1,'\n\n','Total amount to be paid=',total
    print '\n\t\t\t\t\t\t GET WELL SOON \n'
    print'************************************************ End Of Bill **************************************************************\n\n'
def main():

    while True:
        
        print'==========================MENU=================================================='
        print'1-Doctor'
        print'2-Patient'
        print'3-Administrator'
        print'4-Test'
        print'5-Exit'
        print'================================================================================'

        ch= input ('Enter your choice : ')

        if ch==1:
        
            choice1='Y'
            while choice1.upper()=='Y' :
                 passw=raw_input('enter the password : ')
                 if passw=='doc':
                     print '\n\n1-Append file'
                     print '2-Insert a new doctors record'
                     print '3-Delete a doctors record'
                     print '4-Modify the existing doctors record'        
                     print '5-Display the doctors details'
                     print '6-Search a doctors record'
                     print '7-Back to main menu\n\n'
                     ch1=input('enter your choice : ')
                     if ch1==1:
                         append1()

                     elif ch1==2:
                         insert1()

                     elif ch1==3:
                         delete1()

                     elif ch1==4:
                         modify1()

                     elif ch1==5:
                         display1()

                     elif ch1==6:
                         search1()

                     elif ch1==7 :
                         break
        
                
                     else:
                         print 'You have picked the wrong choice '
                     choice1=raw_input('Do you want to continue? : ')
                
                 else:
                    pass
        

        elif ch==2:        
            choice='Y'
            while choice.upper()=='Y' :
                print '\n\n1-Append file'
                print '2-Insert a new patient record'
                print '3-Delete a patient record'
                print '4-Modify a existing patient record'        
                print '5-Display all patient details'
                print '6-Search a patient record'
                print '7-Back to main menu\n\n'

                ch2=input('enter your choice :')

                if ch2==1:
                    append()
    
                elif ch2==2:
                    insert()

                elif ch2==3:
                    delete()

                elif ch2==4:
                    modify()
    
                elif ch2==5:
                    display()

                elif ch2==6:
                    search()

                elif ch2==7 :
                     break
                    
                choice=raw_input('Do you want to continue? : ')
            

        elif ch==3:
            choice='Y'
            while choice.upper()=='Y' :
                passw=raw_input('enter the password : ')
                if passw=='8.1':                
                    print '\n\n1-Append file'
                    print '2-Insert a new member record'
                    print '3-Delete a members record'
                    print '4-Modify a existing record'        
                    print '5-Display all members details'
                    print '6-Search a record'
                    print '7-Back to main menu\n\n'

                    ch2=input('enter your choice :')

                    if ch2==1:
                        append0()
        
                    elif ch2==2:
                        insert0()

                    elif ch2==3:
                        delete0()

                    elif ch2==4:
                        modify0()
        
                    elif ch2==5:
                        display9()

                    elif ch2==6:
                        search0()

                    elif ch2==7 :
                         break
                        
                    choice=raw_input('Do you want to continue? : ')
                else:
                    'you have entered wrong password'
                    break
        elif ch==4:
            passw=raw_input('enter the password :' )
            if passw=='bill':
                print'\nPASSWORD ACCEPTED \n'
                test()

        else:
            exit()
main()
