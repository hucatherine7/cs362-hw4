#Question 1

def calcVolume(x):
    if(not isinstance(x, int)):
        print("\nError, you have not entered an integer")
        return -1
    if x < 0:
        print("\nError, the length cannot be negative")
        return -1
        
    return x*x*x

#print(calcVolume(-3))
