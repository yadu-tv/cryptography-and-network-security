def split(number):
    return [int(i) for i in str(number)]

def main(): 
    arr = int(input("Enter the full number: "))
    n = int(input("Enter the length of each entry: "))

    res = []
    pointer = 0

    arr = split(arr)
    res.append(arr[len(arr)-1])

    if len(arr) % n != 0:
        return("Not possible")

    for i in range(0, len(arr), n):
        if i != 0:
            res.append(arr[i-1])
        for j in range(n):
            res.append(arr[i+j])
            pointer += 1
        if pointer != len(arr):
            res.append(arr[i+n])
    
    res.append(arr[0])
    return res
  
if __name__=="__main__": 
    print(main()) 
