# ============================================================
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ============================================================

"""
Problem Summary:
You are given an array prices where prices[i] is the price
of a stock on the ith day.

You must:
- Buy on one day
- Sell on a future day
- Maximize profit

If no profit is possible, return 0.
"""

"""
Approach (Greedy / Single Pass Optimization):

Key Idea:
- Track the minimum price seen so far.
- For each day, calculate potential profit:
      current_price - minimum_price_so_far
- Update maximum profit if this profit is larger.
- Continue scanning the array once.

Why This Works:
- We always buy at the lowest price before selling.
- We ensure buying happens before selling.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")   # Stores minimum price seen so far
        max_profit = 0             # Stores maximum profit

        for price in prices:
            
            # Update minimum price
            min_price = min(min_price, price)
            
            # Calculate profit if sold today
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit


"""
Time Complexity: O(n)
- We traverse the array only once.

Space Complexity: O(1)
- We use only two variables (min_price, max_profit).

Pattern:
- Greedy
- Running Minimum
- Similar thinking to Kadane’s Algorithm

Interview Tip:
If interviewer asks:
"Why not use two loops?"
Because that would give O(n²) time.
This optimized solution runs in O(n).
"""
