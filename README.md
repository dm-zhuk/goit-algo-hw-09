# Greedy Algorithms and Dynamic Programming

## Coin Change Algorithms

This GoIT educational project implements two algorithms for the coin change solution: a greedy algorithm (**find_coins_greedy**) and a dynamic programming algorithm (**find_min_coins**). Both algorithms take an amount and return a dictionary of coin denominations and their counts to form the amount. The comparison focuses on time complexity, performance with large amounts, and situational advantages.

## Overview

- **Greedy Algorithm**: Selects the largest coin denomination at each step to form the target amount.
- **Dynamic Programming (DP)**: Computes the minimum number of coins needed by building solutions for all amounts up to the target.

## Time Complexity Analysis

- **Greedy**: The algorithm iterates through the coin denominations once, making it **O(n)**, where `n` is the number of denominations (e.g., 6 for [50, 25, 10, 5, 2, 1]). It’s fast and efficient but sometimes may lead to a non-optimal result, especially on a long run.
- **DP**: The algorithm fills a table of size `amount` for each denomination, resulting in **O(amount \* n)**. This is slower, especially for large amounts, but guarantees the minimum number of coins.

## Performance with Large Amounts (> 10K)

- **Greedy**:

  - _Fast_: Constant time per denomination makes it ideal for large amounts with standard denominations like **[50, 25, 10, 5, 2, 1]**.
  - Good enough when speed is critical and denominations are given to work with greedy.

- **DP**:
  - _Slower_: Performance degrades with large amounts due to the O(amount \* n) complexity, requiring more memory for computing.
  - _Reliable_: Always finds the minimum number of coins, making it robust for any coins denomination set.
  - Preferred when precision is critical.

## Conclusion

The **greedy algorithm** is faster and suitable for standard coin denominations, making it efficient for large amounts in specific cases.
The **DP algorithm**: O(amount \* n) complexity, slower for large amounts due to the nested loop over amount and denominations.
For general use or non-standard enominations, prefer DP; for speed with standard denominations, use greedy.

## Backup data

### Testing amount: 113

- Greedy Average Time (over 1000 runs): 0.000001 seconds
- DP Time: 0.000123 seconds

### Testing amount: 199

- Greedy Time: 0.000_003 seconds
- DP Time: 0.000_204 seconds

### Testing amount: 999

- Greedy Time: 0.000_003 seconds
- DP Time: 0.001_256 seconds

### Testing amount: 10000

- Greedy Time: 0.000_003 seconds
- DP Time: 0.020_638 seconds
