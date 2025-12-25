def greedy_algorithm(items, budget):
    ratios = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratios.append((name, ratio, info["cost"], info["calories"]))

    ratios.sort(key=lambda x: x[1], reverse=True)

    selected_items = []
    total_calories = 0
    remaining_budget = budget

    for name, ratio, cost, calories in ratios:
        if remaining_budget >= cost:
            selected_items.append(name)
            total_calories += calories
            remaining_budget -= cost

    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i-1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name = item_names[i-1]
            selected_items.append(name)
            w -= items[name]["cost"]

    return selected_items, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

#-----------------------------------------------------------------------------
# Checking time


greedy_result, greedy_calories = greedy_algorithm(items, budget)
dp_result, dp_calories = dynamic_programming(items, budget)

print(f"Budget: {budget}")
print("-" * 30)
print("Greedy algorithm:")
print(f"Food: {greedy_result}")
print(f"Callories: {greedy_calories}")
print("-" * 30)
print("Dymanic programming:")
print(f"Food: {dp_result}")
print(f"Callories: {dp_calories}")