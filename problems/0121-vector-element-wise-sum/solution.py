def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:

    
    if len(a) == len(b):
        total_sum=[]
        for i in range(len(a)) :
            total_sum.append(a[i]+b[i])
    else:
        return -1
       

    return total_sum

         
