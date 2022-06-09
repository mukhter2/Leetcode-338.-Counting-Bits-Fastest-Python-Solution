# Leetcode 338. Counting Bits (Fastest and Easy to understand solution)
## Problem Statement
Link: https://leetcode.com/problems/counting-bits/
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
## Example
### Example 1:
Input: n = 2
Output: [0,1,1]

#### Explanation:
0 --> 0
1 --> 1
2 --> 10
### Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
#### Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
## Constraints:
0 <= n <= 105
## Methodology:
Step 1: Create a list and append from 0 to N
Step 2: during append, if value is greater than 1, then append the sum of the remainder and result of the value if divided by 2
Step 3: return the list
