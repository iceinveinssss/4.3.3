from typing import Literal

def simple_interest(principal: float, rate: float, time: int) -> float:
    #Рассчитывает прибыль по формуле простых процентов.
    return principal * rate * time / 100

def bonus_interest(principal: float, rate: float, time: int, bonus_threshold: float, bonus_rate: float) -> float:
    #Рассчитывает прибыль с бонусным начислением.
    interest = simple_interest(principal, rate, time)
    if principal > bonus_threshold:
        interest += interest * bonus_rate / 100
    return interest

def compound_interest(principal: float, rate: float, time: int, periods: int) -> float:
    # Рассчитывает прибыль по формуле сложных процентов.
    return principal * (1 + rate / (100 * periods))**(periods * time) - principal

def select_best_deposit(principal: float, rate: float, time: int, deposit_type: Literal["simple", "bonus", "compound"],
                         bonus_threshold: float = 0, bonus_rate: float = 0, periods: int = 1) -> float:
    # Выбирает лучший вклад по заданным параметрам.
    if deposit_type == "simple":
        return simple_interest(principal, rate, time)
    elif deposit_type == "bonus":
        return bonus_interest(principal, rate, time, bonus_threshold, bonus_rate)
    elif deposit_type == "compound":
        return compound_interest(principal, rate, time, periods)
    else:
        raise ValueError("Неверный тип вклада")

principal = 10000  # Сумма вклада
rate = 5  # Процентная ставка
time = 3  # Срок в годах
bonus_threshold = 15000  # Порог для бонуса
bonus_rate = 2  # Бонусный процент
periods = 4  # Количество периодов в год (для капитализации)

print("Срочный вклад:", select_best_deposit(principal, rate, time, "simple"))
print("Бонусный вклад:", select_best_deposit(principal, rate, time, "bonus", bonus_threshold, bonus_rate))
print("Вклад с капитализацией:", round(select_best_deposit(principal, rate, time, "compound", periods=periods), 2))

