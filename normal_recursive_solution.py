class Solution:
    def countBits(self, n: int) -> List[int]:
        lstFin=[0]*(n+1)
        if n>0:
            lstFin[1]=1
        def counter(n):
            if n<2:
                if n==1: 
                    return 1
                else:
                    return 0
            else:
                if lstFin[n]>0:
                    return lstFin[n]
                if n%2==1:
                    lstFin[n]+=1
                p=n//2
                lstFin[n]+=counter(p)
        for x in range(0,n+1):
            counter(x)
        return lstFin
         
