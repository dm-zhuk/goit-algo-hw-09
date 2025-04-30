import time


# Greedy
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            if count > 0:
                result[coin] = count
    return result


# DP
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [[] for _ in range(amount + 1)]
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]
    result = {}
    for coin in coin_used[amount]:
        result[coin] = result.get(coin, 0) + 1
    return result


# Test amounts
amounts = [113, 199, 999, 10000]

# Measure execution time
for amount in amounts:
    print(f"\nTesting amount: {amount}")

    # Greedy
    start_time = time.time()
    find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    print(f"Greedy Time: {greedy_time:.6f} seconds")

    # DP
    start_time = time.time()
    find_min_coins(amount)
    dp_time = time.time() - start_time
    print(f"DP Time: {dp_time:.6f} seconds")
