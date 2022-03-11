class Solution(object):
    def maxProfit(self, prices):
     min_till_now = 10000;
     best_rate=0;
     for price in prices:
         if  min_till_now > price:
            min_till_now= price
         elif  best_rate < price - min_till_now:
            best_rate = price - min_till_now
     return best_rate
        