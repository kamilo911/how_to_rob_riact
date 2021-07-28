def maximum_value(maximum_weight, items):
    '''
    Based on pseodo-code given in this article
    https://en.wikipedia.org/wiki/Knapsack_problem#Dynamic_programming_in-advance_algorithm

    Parameters
    ----------
    maximum_weight : dict.
    items : int
       
    Returns
    -------
    int
    '''        
    w= [i["weight"] for i in items] #Weights (stored in array w)
    v= [i["value"] for i in items] #Values (stored in array v)
    #The array "v" and array "w" are assumed to store all relevant values starting at index 1.
    w.insert(0, 666) #adding irrelevant value at the beginning
    v.insert(0, 666) #adding irrelevant value at the beginning
    n = len(items) #Number of distinct items (n)
    m = [[0 for y in range(maximum_weight+1)] for x in range(n+1)]
    
    
    for i in range(1, n+1):
        for j in range(maximum_weight+1):
            if w[i] > j:
                m[i][j] = m[i-1][j]
            else:
                m[i][j]= max([m[i-1][j], m[i-1][j-w[i]] + v[i]])
    
    return m[n][maximum_weight]
