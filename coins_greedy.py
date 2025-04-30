"""
Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.
"""


def find_coins_greedy(amount):
    # Coin denominations, sorted
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    # Iterate over each coin denomination
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            if count > 0:
                result[coin] = count

    return result


# Test the greedy O(n) function
print(find_coins_greedy(113))
print(find_coins_greedy(199))
print(find_coins_greedy(999))
print(find_coins_greedy(10000))
