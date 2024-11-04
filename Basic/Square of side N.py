def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    # op = []
    # for i in range(n):
    #     op.append(n*"*")
        
    op = [n*"*" for i in range(n)]
    return op
        
    
