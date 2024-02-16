

def add(x,y, verbose=False):
    """_summary_

    Args:
        x (float): variable 1
        y (float): variable 1
        verbose (bool, optional): prints. Defaults to False.

    Returns:
        suma (float): add
    """
    suma = x+y
    if verbose is True:
        print("{} + {} =  {}".format(x,y,suma))
    
    return suma