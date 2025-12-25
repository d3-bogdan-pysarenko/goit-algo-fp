import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls=100000):
    # Можливі суми від 2 до 12
    sums_count = {i: 0 for i in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1

    # Обчислення ймовірностей
    probabilities = {s: count / num_rolls for s, count in sums_count.items()}
    
    return sums_count, probabilities

# Налаштування кількості ітерацій
n = 100000
counts, probs = simulate_dice_rolls(n)

# Виведення результатів у консоль (таблиця)
print(f"{'Сума':<10} | {'Кількість':<12} | {'Ймовірність (%)'}")
print("-" * 40)
for s in range(2, 13):
    print(f"{s:<10} | {counts[s]:<12} | {probs[s]*100:.2f}%")

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.bar(probs.keys(), probs.values(), color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title(f'Ймовірності сум при киданні 2-х кубиків ({n} ітерацій)')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()