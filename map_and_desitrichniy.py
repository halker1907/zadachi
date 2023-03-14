food = input().split()
prices = input().split()
prices = list(map(int, prices))
for i in range(len(prices)):
    if food[i] == "Молоко":
        prices[i] = prices[i] // 10 * 10
print(prices)