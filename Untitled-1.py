import os
#эта функция очищает экран
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def select_task():
    task = input("виберіть задавдання: 1-6 ")
    match task:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case "6":
            task6()
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
def task1():
    clear()
    try:
        n1 = int(input("введіть початкову ціну: "))
        n2 = int(input("введіть процент знижки: "))
    except ValueError:
        print("помилка! введіть ціле число.")
        task1()
    print("ціна зі знижкою: ", n1 - (n1 * n2 / 100))
def task2():
    clear() 
    try:
        dollars = float(input("введіть суму в доларах: "))
        exchange_rate = float(input("введіть курс обміну на євро: "))
        if exchange_rate == 0:
            raise Exception("Курс обміну не може дорівнювати нулю")
        euros = dollars * exchange_rate
        print(f"сума в євро: {euros}")
    except ValueError:
        print("помилка! введіть число.")
    except Exception as e:
        print(e)
    finally:
        print("операція завершена")
def task3():
    clear()
    try:
        a = str(input("введіть рядок чисел через пробіл: "))
        numbers = list(map(float, a.split()))
        n = 0
        for i in range(len(numbers)):
            if numbers[i] < 0:
                raise Exception("число не може бути від'ємним")
            n += numbers[i]
        print("середнє арифметичне: ", n / len(numbers))
    except ValueError:
        print("помилка! введіть число.")
    except Exception as e:
        print(e)
    finally:
        print("завершення обчислень")
def task4():
    n = 1000
    while True:
        clear()
        print("введіть операцію:")
        print("1 - просмотр баланса на рахунку")
        print("2 - поповнення рахунку")
        print("3 - зняття коштів")
        try:
            operation = int(input("виберіть операцію: "))
            if operation == 1:
                clear()
                print(f"баланс на рахунку: {n}")
            elif operation == 2:
                clear()
                amount = float(input("введіть суму для поповнення: "))
                if amount < 0:
                    raise Exception("сума не може бути від'ємною")
                n += amount
                print(f"новий баланс: {n}")
            elif operation == 3:
                clear()
                amount = float(input("введіть суму для зняття: "))
                if amount % 10 != 0:
                    raise Exception("сума повинна бути кратною 10")
                if amount < 0:
                    raise Exception("сума не може бути від'ємною")
                if amount > n:
                    raise Exception("недостатньо коштів на рахунку")
                n -= amount
                print(f"новий баланс: {n}")
            else:
                print("невірний вибір операції")
        except ValueError:
            print("помилка! введіть число.")
        except Exception as e:
            print(e)
        finally:
            if input ("хотите продолжить? (y/n) ") == "n":
                break
def task5():
    clear()
    try:
        order_number = input("введіть номер замовлення: ")
        if not order_number.startswith("ORD"):
            raise Exception("Неправильний формат номера замовлення")
        if not order_number[3:].isdigit():
            raise Exception("Неправильний формат номера замовлення")
        print("номер замовлення правильний")
    except Exception as e:
        print(e)
    finally:
        print("завершення перевірки")
def task6():
    clear()
    try:
        a = str(input("введіть рядок чисел через пробіл: "))
        numbers = []
        for i in a.split():
            try:
                num = float(i)
                numbers.append(num)
            except ValueError:
                print(f"попередження: '{i}' не є числом і буде пропущено")
        if len(numbers) == 0:
            raise ZeroDivisionError("список чисел порожній, обчислення неможливе")
        total = sum(numbers)
        average = total / len(numbers)
        print(f"сума: {total}, середнє: {average}")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("завершення обробки даних")
while True:
    select_task()