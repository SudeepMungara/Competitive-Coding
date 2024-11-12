def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    op=[]
    for i in range(1,n+1):
        if i==1:
            op.append(str(1))
        else:
            curr = int(op[-1].split(' ')[-1]) if len(op)>1 else int(op[-1])
            tmp = []
            for j in range(1,i+1):
                tmp.append(str(curr+j))
            tmp = ' '.join(tmp)
            op.append(tmp)
    return op
