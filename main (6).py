


def fact_rec(n): 
  if n==1:
    return 1 
  return n*fact_rec(n-1)
num=5
  
print("Factorial of",num,"is",fact_rec(num))