silver_clock = 96
golden_clock = silver_clock / 16
total_cost = int(input("Введите общую выручку часовых дел мастера: "))
cost_ofsilver = 48
cost_ofgolden = (total_cost - silver_clock * cost_ofsilver) / golden_clock
print(int(cost_ofgolden))
