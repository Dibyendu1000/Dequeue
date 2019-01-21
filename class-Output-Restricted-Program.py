print('''Output Restricted Program''')
#======================================================================================
class Dequeue():
    def __init__(self):
        self.list=[]
        self.n=0
        self.front=-1
        self.rear=0;self.dels=0
#=====================================================================================
    def Entry(self):
        self.list=[]
        self.front=-1
        self.rear=0;self.dels=0
        self.n=int(input('Enter the no. of element:'))
        self.rear=self.n
        for i in range(self.n):
            self.list.append('-')
#=====================================================================================
    def Insert(self):
        sub=self.rear-self.front
        print('diff:',sub)
        if sub==1:
            print('Queue is Full')
        elif sub==2:
            self.front+=1
            self.list[self.front]=int(input('Enter your element:'))
        else:
            ch=input('Want to insert from left or right?(L/R):')
            if ch=='L' or ch=='l':
                self.front+=1
                self.list[self.front]=int(input('Enter your element:'))
            elif ch=='r' or ch=='R':
                self.rear-=1
                self.list[self.rear]=int(input('Enter your element:'))
            else:
                print('Invalid choice!!!!!')
#=======================================================================================
    def Delete(self):
        if self.dels>self.n-1:
            print('Queue is Empty')
            self.front=-1
            self.rear=self.n
        else:
            print('Deleted:',self.list[self.dels])
            self.dels+=1
#========================================================================================
    def Display(self):
        if self.dels>self.n-1:
            print('Queue is Empty')
            self.front=-1
            self.rear=self.n
            self.dels=0
        else: 
            print('Printing the Queue')
            for i in range(self.dels,self.n,+1):
                print(self.list[i],end=' ')
#=========================================================================================
    def Choose(self):
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
                self.Insert()
            elif ch==3:
                self.Delete()
            elif ch==4:
                self.Display()
            else:
                break
#========================__MAIN__==============================================================
ob=Dequeue()
ob.Choose()

            
