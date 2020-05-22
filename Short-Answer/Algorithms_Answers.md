#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The Big-O notation for this algorithm is O(n) the number of operations scales linearly with the input. when n = 10 this code required 10 operations, n= 100, 100 operations, n=1000, 1000 operations. I ran this code to reach that conclusion:

def sprint(n):
    a = 0
    operations = 0
    while (a < n * n * n):
    a = a + n * n
    operations+=1
    print(operations)


b) Qaudratic time (O(n2)). The Big O notation for this algorithm is qaudratic. The nested for loops hint at this, but when the code is run and n = 10, 40 operations are required. When n = 20 100 operations are required. This ratio tells me that the number of operations are not scaling linearly, or logramithrically, and because the  number of operations are disproportionality increasing this is an instance of qaudratic run time. 


c)

## Exercise II


