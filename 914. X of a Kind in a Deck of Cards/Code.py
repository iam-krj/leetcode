from collections import Counter
def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)
    
class Solution(object):
    def hasGroupsSizeX(self, deck):
        c = Counter(deck)
        ans = c[deck[0]]
        for num in set(deck):
            if c[num]!=ans:
                big, small = max(c[num], ans), min(c[num], ans)
                g = gcd(big, small)
                if g==1:
                    return False
                ans = g
        return ans>1