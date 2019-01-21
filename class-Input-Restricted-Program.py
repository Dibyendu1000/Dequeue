print('''Input Restricted Program''')
#==================================================================================
class Dequeue():
    def __init__(self):
        self.n=0
        self.front=0
        self.rear=-1
        self.list=[]
#=================================================================================
    def Entry(self):
        self.front=0
        self.rear=-1
        self.list=[]
        self.n=int(input('Enter no. of elements:'))
        for i in range(self.n):
            self.list.append('-')
#===================================================================================            
    def Insert(self):
        if self.rear>=self.n-1:
            print('Queue is Full')
        else:
            self.rear+=1
            self.list[self.rear]=int(input('Enter your element:'))
#======================================================================================
    def Delete(self):
        if self.rear==-1:
            print('Queue is Empty')
        elif self.rear==self.front:
            print('Deleted:',self.list[self.front])
            self.rear=-1
            self.front=0
        else:
            ch=input('Want to delete from left or right?(L/R):')
            if ch=='L' or ch=='l':
                print('Deleted:',self.list[self.front])
                self.front+=1
            elif ch=='R' or ch=='r':
                print('Deleted:',self.list[self.rear])
                self.rear-=1
            else:
                print('Invaid Choice !!!!!')
#==========================================================================================
    def Display(self):
        if self.rear==-1 :
            print('Queue is Empty')
        else:
            print('Printing the Queue')
            for i in range(self.front,self.rear+1,+1):
                print(self.list[i], end=' ')
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
