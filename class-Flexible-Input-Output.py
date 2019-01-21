print('Queue with no Restrictions')
#===============================
class Flexible:
    def __init__(self):
        self.ir=0
        self.il=-1
        self.dl=0
        self.dr=0
        self.list=[]
        self.n=0
#=============================================================
    def reset(self):
        self.ir=self.n
        self.il=-1
        self.dl=0
        self.dr=self.n-1
#==============================================================
    def Entry(self):
        self.list=[]
        self.n=int(input('Enter no. of elements:'))
        self.reset()
        for i in range(self.n):
            self.list.append('-')
#==================================================================
    def insert(self):
        sub=self.ir-self.il
        if sub==1:
            print('-'*10)
            print('Queue is Full')
        elif sub==2:
            self.il+=1
            self.list[self.il]=int(input('Enter your element:'))
        else:
            ch=input('Want to insert from left or right?(L/R):')
            if ch=='r' or ch=='R':
                self.ir-=1
                self.list[self.ir]=int(input('Enter your element:'))
            elif ch=='l' or ch=='L':
                self.il+=1
                self.list[self.il]=int(input('Enter your element:'))
            else:
                print('-'*10)
                print('Invalid Choice !!!!!')
#==========================================================================
    def delete(self):
        if self.ir==self.n and self.il==-1:
            print('Queue is Empty')
        elif self.dr==self.dl:
            print('Deleted:',self.list[self.dr])
            self.reset()
        else:
            ch=input('Want to delete from left or right?(L/R):')
            if ch=='l' or ch=='L':
                print('Deleted:',self.list[self.dl])
                self.dl+=1
            elif ch=='r' or ch=='R':
                print('Deleted:',self.list[self.dr])
                self.dr-=1
            else:
                print('-'*10)
                print('Invalid Choice!!!!!!')
#=============================================================================
    def display(self):
        if self.dr==self.dl:
            print('Printing the Queue.....')
            print(self.list[self.dr])
        elif self.ir==self.n and self.il==-1:
            print('Queue is Empty')
        else:
            ch=input('Want to display from left or right?(R/L):')
            if ch=='l' or ch=='L':
                print ('Displaying the Queue from left.....')
                for i in range(self.dl,self.dr+1,+1):
                    print (self.list[i],end=' ')
            elif ch=='r' or ch=='R':
                print('Displaying the Queue from right....')
                for i in range(self.dr,self.dl-1,-1):
                    print (self.list[i],end=' ')
            else:
                print('Invalid Choice!!!!!!')
#=====================================================================================
    def choose(self):
        while True:
            print('\n1.Entry')
            print('2.Insert')
            print('3.Delete')
            print('4.Display')
            print('5.Exit')
            ch=int(input('Enter your choice:'))
            if ch==1:
                self.Entry()
            elif ch==2:
                self.insert()
            elif ch==3:
                self.delete()
            elif ch==4:
                self.display()
            else:
                break
ob=Flexible()
ob.choose()
                         
