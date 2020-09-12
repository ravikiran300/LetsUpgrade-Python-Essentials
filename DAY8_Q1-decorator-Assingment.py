def getInput(calculate_arg_fun):
    
    def wrap_function():
    
        a = int(input("\nEnter First Number - "))
        
        b = int(input("\nEnter Second Number - "))
        
        calculate_arg_fun(a,b)   
    
    return wrap_function


@getInput

def EvenFinder(start, last):
    
    print("\nThe Even numbers in the range",start,"to",last,"is :\n")

    for n in range(start, last + 1): 
      
        if n % 2 == 0: 
            
            print(n, end = " ")

EvenFinder()


