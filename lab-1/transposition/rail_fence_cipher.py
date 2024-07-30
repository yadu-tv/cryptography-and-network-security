def main(): 
    arr = input("Enter the string: ")
    res, temp = [], []
    for s in arr:
        if s.isalpha():
            temp.append(s)
    
    for i in range(0, len(temp), 2):
        res.append(temp[i])
    for i in range(1, len(temp), 2):
        res.append(temp[i])
    
    return res

if __name__=="__main__": 
    print(main()) 
