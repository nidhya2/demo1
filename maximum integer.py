


brightness_4

# in arr[] of size n  
  

# in arr[] of size n 
def largest(arr,n): 
  
    max = arr[0] 
  
   
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  

arr = [10, 324, 45, 90, 9808] 
n = len(arr) 
Ans = largest(arr,n) 
print ("Largest in given array is",Ans) 
  
