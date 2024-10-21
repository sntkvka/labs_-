salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for i in range (0, months):
    diff_ = spend-salary
    money_capital += diff_
    spend *= 1 + increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")