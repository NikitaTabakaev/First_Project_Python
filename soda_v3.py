# Купюры банкомата и их количество
count_banknote = {5000: 10, 2000: 10, 1000: 10, 500: 10, 200: 10,
                  100: 10, 50: 10, 10: 10, 5: 10, 2: 10,
                  1: 10}
# Купюры
coins_and_banknote = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

# Вид и цена товара
price_and_name_soda = {"Квас": 20, "Кола": 45, "Спрайт": 33, "Вода": 11, "Божественный": 2672}

choose_soda = input("Выберите напиток: ").title()

# Деньги клиента
money = 0

while money < price_and_name_soda[choose_soda]:
    money += int(input("Вставьте купюру: "))
    if money >= price_and_name_soda[choose_soda]:
        break
    print(f"Не достаточно средств, нехватает {abs(money - price_and_name_soda[choose_soda])}")


# Сдача
change = money - price_and_name_soda[choose_soda]
if money == price_and_name_soda[choose_soda]:
    print(f"Сдача 0 РУБЛЕЙ")
else:
    print(f"Сдача {change} РУБЛЕЙ")
    for cash in coins_and_banknote:
        if count_banknote[cash] == 0:
            continue
        while cash <= change and count_banknote[cash] > 0:
            change -= cash
            count_banknote[cash] -= 1
            print(cash)