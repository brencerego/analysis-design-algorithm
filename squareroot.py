def sqrt(num):
    n = int(num/2)
    for i in range(n,0,-1):
        if i*i == num:
            return i
        elif i*i < num:
            diff = float("inf")
            for x in range(1000):
                temp = i + (x/1000)
                if abs(num - (temp*temp)) < diff:
                    diff = num - (temp*temp)
                    best = temp
            return best   
             
    
    
if __name__ == "__main__":
    n = int(input("Enter A Number:"))
    root = sqrt(n)
    print(f"The Square Root is {root}.")