class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        st = [0]
        nsee = [0]*n
        for i in range(n-1,-1,-1):
            while st[-1]!=0 and prices[i] < st[-1]:
                st.pop()
            nsee[i] = st[-1]
            st.append(prices[i])
        return [prices[i] - nsee[i] for i in range(n)]