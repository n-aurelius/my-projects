def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd") 

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False           
    
main()    

# now we have created a code that tells us whether a number is odd or even