SIZE=5
queue=[0]*SIZE
front=-1
rear=-1
def enqueue(value):
    global front,rear
    if rear==SIZE-1:
        print("queue is FULL!! insertion is not possible")
    else:
        rear+=1
        queue[rear]=value
        if front==-1:
             front=0
        print(value,"inserted successfully")
def dequeue():
    global front,rear
    if front==-1:
        print("queue is EMPTY!!")
    else:
        print("deleted Element:",queue[front])
        front+=1
        if front>rear:
            front-=1
            rear-=1
def isEmpty():
    if front==-1:
        return True
    else:
        return False
def show():
    if isEmpty():
        print("queue is empty")
    else:
        print("queue element are:")
        for i in range(front,rear+1):
            print(queue[i],end=" ")
        print()
def size():
    if front==-1:
       return 0
    else:
        return rear-front+1
while True:
    print("/n---ARRAY IMPLEMENTATION OF QUEUE---")
    print("1.enqueue")
    print("2.Dequeue")
    print("3.IsEmpty")
    print("4.size")
    print("5.show")
    print("6.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=int(input("Enter the value:"))
        enqueue(value)
    elif choice==2:
        dequeue()
    elif choice==3:
        if isEmpty():
            print("queue is EMPTY")
        else:
            print("queue is NON-EMPTY")
    elif choice==4:
        print("size of queue:",size())
    elif choice==5:
        show()
    elif choice==6:
        print("program terminated")
    else:
        print("invalid choice")

