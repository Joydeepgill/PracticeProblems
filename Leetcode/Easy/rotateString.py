def rotateString(s, goal): 
    ''' 
        Keep shifting the string one by one to check if that new string is equal to 
        the target string goal. Stop shifting and return true when s == goal, otherwise 
        keep shifting to the right by 1; when youve shifted such that it returns back to 
        original string then return False.   
    '''  

    if s == goal:
        return False 
    else: 
        
