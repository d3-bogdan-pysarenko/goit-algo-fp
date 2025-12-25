def greedy_algorithm(items, budget):
    ratios = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratios.append((name, ratio, info["cost"], info["calories"]))

    ratios.sort(key=lambda x: x[1], reverse=True)

    selected_items = []
    total_calories = 0
    spent_budget = 0
    remaining_budget = budget

    for name, ratio, cost, calories in ratios:
        if remaining_budget >= cost:
            selected_items.append(name)
            total_calories += calories
            spent_budget += cost
            remaining_budget -= cost

    return {
        "items": selected_items,
        "calories": total_calories,
        "spent": spent_budget,
        "remaining": remaining_budget
    }


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
    total_spent = 0
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name = item_names[i-1]
            selected_items.append(name)
            total_spent += items[name]["cost"]
            w -= items[name]["cost"]

    return {
        "items": selected_items,
        "calories": dp[n][budget],
        "spent": total_spent,
        "remaining": budget - total_spent
    }



#-----------------------------------------------------------------------------
# Checking time

def print_results(title, res):
    print(f"--- {title} ---")
    print(f"Food: {', '.join(res['items'])}")
    print(f"Callories: {res['calories']}")
    print(f"Spent money: {res['spent']}")
    print(f"Money left: {res['remaining']}\n")

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

user_budget = 100

greedy_res = greedy_algorithm(items, user_budget)
dp_res = dynamic_programming(items, user_budget)

print(f"Initial money: {user_budget}\n")
print_results("Greedy Algorithm", greedy_res)
print_results("DynamicProgramming", dp_res)