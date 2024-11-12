def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    op = [None]*n
    op[0]=op[-1]=n*"*"
    for i in range(n):
        if op[i]==None:
            string = "*"+' '*(n-2)+'*'
            op[i]=string
    return op
