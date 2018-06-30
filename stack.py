global stack;

##size and push do not need function

def empty():
    stackLen = len(stack);

    if stackLen == 0:
        return 1;
    else:
        return 0;

def pop():
    if empty():
        print(-1);

    else:
        popNum = stack.pop();
        print(popNum);
        return popNum;
    
def top():
    if empty():
        print(-1);
        return -1;
    else:
        print(stack[len(stack)-1]);
        return stack[len(stack)-1];

def size():
    stackSize = len(stack);
    print(stackSize);
    return stackSize;
        
if __name__ == "__main__":
    stack = [];
    
    N = int(input());

    for n in range(0, N):
        order = input();
        checkPush = order[0:4];

        if checkPush != "push":
            if order == "pop":
                pop();
            elif order == "size":
                size();
            elif order == "empty":
                print(empty());
            elif order == "top":
                top();
            else:
                print("wrong order!");
                    
            
        elif checkPush == "push":
            order, orderNum  = order.split(" ");
                       
            if orderNum != None:
                stack.append(orderNum);
            else:
                print("you should put number!");
            
        
        
            
        
