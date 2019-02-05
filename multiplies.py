 
def multiple(m, n): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(n, (m * n)+1, n) 
      
    print(*a) 
  
 
m = 2
n = 4
multiple(m, n) 
