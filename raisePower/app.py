"""Function to raise power recursively"""
def raise_power(base,exp):

    """Base Case"""
    """Checks to see if Case exp==1"""
    if(exp == 1):
        """Returns base num raise to is num itself"""
        return(base)

    """Recursive Case"""
    """Checks to see if exp is not equal to one"""
    elif(exp != 1):
        
        """Mulitiply base recursively by the function"""
        return(base * raise_power(base, exp-1))


print(raise_power(20,2))

