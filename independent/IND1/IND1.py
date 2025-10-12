import math

def task1():
    print("Давайте познайомимося! Дайте відповідь на кілька запитань:")
    print()

    surname_name = input("Ваші прізвище, ім'я, по батькові: ")
    age = input("Скільки Вам років? ")
    residence = input("Де Ви живете? ")
    education = input("Де Ви навчаєтесь? ")
    group_number = input("Номер Вашої групи: ")
    order_number = input("Який Ваш порядковий номер у списку групи? ")

    print("\n" + "=" * 50)
    print("Далі ще питання з таблиці нижче")
    print("=" * 50)

    print(f"Ваше ім'я: {surname_name}")
    print(f"Ваш вік: {age}")
    print(f"Ви живете в: {residence}")
    print(f"Ви навчаєтесь в: {education}")
    print(f"Номер моєї групи: {group_number}")
    print(f"Мій порядковий номер у списку групи: {order_number} \n")

    questions = [
        "Як справи?",
        "Як Ви себе почуваєте?",
        "Коли будете вдома?",
        "Яку оцінку отримав на ЗНО по українській мові?",
        "Сьогодні сонячно?",
        "Коли нарешті карантин?",
        "Як звати Вашого друга?",
        "Ви думаєте вступати у магістратуру?",
        "Якого кольору Ваш зошит?",
        "Який Ваш настрій сьогодні?"
    ]

    print("Відповідайте на питання:")
    for i, question in enumerate(questions):
        input(f"{i}. {question} ")

    print("\nДякую за відповіді!")


def calculate_z(x, t):
    """
    Функція для обчислення Z за формулою:
    Z = (9π + 10cos(x)) / √(t - |sin(t)|) * e^x

    Args:
        x (float): значення змінної x
        t (float): значення змінної t

    Returns:
        float: результат обчислення Z
    """
    try:
        numerator = 9 * math.pi + 10 * math.cos(x)

        denominator_inside = t - abs(math.sin(t))

        if denominator_inside <= 0:
            raise ValueError(f"Вираз під коренем має бути > 0, а отримано: {denominator_inside}")

        denominator = math.sqrt(denominator_inside)

        exp_x = math.exp(x)

        z = (numerator / denominator) * exp_x

        return z

    except ValueError as ve:
        print(f"Помилка значення: {ve}")
        return None
    except Exception as e:
        print(f"Помилка обчислення: {e}")
        return None


def task2():
    print("Програма для розрахунку Z")
    print("Формула: Z = (9π + 10cos(x)) / √(t - |sin(t)|) * e^x")
    print("=" * 60)

    try:
        print("Введіть дані:")
        x = float(input("Введіть значення x: "))
        t = float(input("Введіть значення t: "))

        result = calculate_z(x, t)

        if result is not None:
            print("\nРезультат:")
            print(f"x = {x}")
            print(f"t = {t}")
            print(f"Z = {result:.6f}")

            print("\nПроміжні обчислення:")
            print(f"9π = {9 * math.pi:.6f}")
            print(f"cos(x) = {math.cos(x):.6f}")
            print(f"9π + 10cos(x) = {9 * math.pi + 10 * math.cos(x):.6f}")
            print(f"|sin(t)| = {abs(math.sin(t)):.6f}")
            print(f"t - |sin(t)| = {t - abs(math.sin(t)):.6f}")
            print(f"√(t - |sin(t)|) = {math.sqrt(t - abs(math.sin(t))):.6f}")
            print(f"e^x = {math.exp(x):.6f}")

    except ValueError:
        print("Помилка: Введіть правильне числове значення!")
    except KeyboardInterrupt:
        print("\nПрограму перервано користувачем.")
    except Exception as e:
        print(f"Неочікувана помилка: {e}")


def example_calculation():
    print("\n" + "=" * 60)
    print("Приклад розрахунку:")
    print("Останні цифри групи = 1, тому t = 1")

    test_values = [0, 1, -1, 2]

    for x_val in test_values:
        print(f"\nДля x = {x_val}, t = 1:")
        result = calculate_z(x_val, 1)
        if result is not None:
            print(f"Z = {result:.6f}")\

def calculate_f(x):
    """
    Функція для обчислення кусочно-заданої функції:

    f(x) = { 0.5 - ⁴√|x|,     якщо x ≥ 0
           { sin²(x²) / |x+1|, якщо x < 0

    Args:
        x (float): значення змінної x

    Returns:
        float: результат обчислення f(x)
    """
    try:
        if x >= 0:
            # Для x ≥ 0: f(x) = 0.5 - ⁴√|x|
            # ⁴√|x| = |x|^(1/4) = x^(1/4) оскільки x ≥ 0
            fourth_root = abs(x) ** (1 / 4)
            result = 0.5 - fourth_root
            return result
        else:
            # Для x < 0: f(x) = sin²(x²) / |x+1|
            sin_squared = (math.sin(x ** 2)) ** 2
            denominator = abs(x + 1)

            # Перевіряємо, щоб знаменник не дорівнював нулю
            if denominator == 0:
                raise ValueError("Ділення на нуль: x + 1 = 0, тобто x = -1")

            result = sin_squared / denominator
            return result

    except ValueError as ve:
        print(f"Помилка значення: {ve}")
        return None
    except Exception as e:
        print(f"Помилка обчислення: {e}")
        return None


def task3():
    print("Програма для обчислення кусочно-заданої функції f(x)")
    print("                 ⎧ 0.5 - ⁴√|x|,     x ≥ 0")
    print("            f(x) = ⎨")
    print("                 ⎩ sin²(x²)/|x+1|,  x < 0")
    print("=" * 60)

    try:
        x = float(input("Введіть значення x: "))
        result = calculate_f(x)

        if result is not None:
            print("\nРезультат:")
            print(f"x = {x}")

            if x >= 0:
                print("Використана формула: f(x) = 0.5 - ⁴√|x|")
                print(f"⁴√|x| = ⁴√{abs(x)} = {abs(x) ** (1 / 4):.6f}")
                print(f"f({x}) = 0.5 - {abs(x) ** (1 / 4):.6f} = {result:.6f}")
            else:
                print("Використана формула: f(x) = sin²(x²) / |x+1|")
                print(f"x² = {x ** 2:.6f}")
                print(f"sin(x²) = sin({x ** 2:.6f}) = {math.sin(x ** 2):.6f}")
                print(f"sin²(x²) = {(math.sin(x ** 2)) ** 2:.6f}")
                print(f"|x+1| = |{x}+1| = {abs(x + 1):.6f}")
                print(f"f({x}) = {(math.sin(x ** 2)) ** 2:.6f} / {abs(x + 1):.6f} = {result:.6f}")

    except ValueError:
        print("Помилка: Введіть правильне числове значення!")
    except KeyboardInterrupt:
        print("\nПрограму перервано користувачем.")
    except Exception as e:
        print(f"Неочікувана помилка: {e}")


def test_function():
    """Функція для тестування з різними значеннями"""
    print("\n" + "=" * 60)
    print("Тестування функції з різними значеннями:")

    test_values = [0, 1, 4, 16, -0.5, -2, -3]

    for x_val in test_values:
        if x_val == -1:
            print(f"x = {x_val}: Функція не визначена (ділення на нуль)")
            continue

        result = calculate_f(x_val)
        if result is not None:
            condition = "x ≥ 0" if x_val >= 0 else "x < 0"
            print(f"x = {x_val:4.1f} ({condition}): f(x) = {result:8.6f}")


def interactive_mode():
    """Інтерактивний режим для багаторазового обчислення"""
    print("\n" + "=" * 60)
    print("Інтерактивний режим (введіть 'q' для виходу)")

    while True:
        try:
            user_input = input("\nВведіть значення x (або 'q' для виходу): ")
            if user_input.lower() == 'q':
                break

            x = float(user_input)
            result = calculate_f(x)

            if result is not None:
                print(f"f({x}) = {result:.6f}")

        except ValueError:
            print("Помилка: Введіть числове значення або 'q' для виходу!")
        except KeyboardInterrupt:
            break

    print("Дякую за використання програми!")


def task4():
    numbers = []
    for i in range(3):
        num = int(input(f"Введіть {i + 1}-е число: "))
        numbers.append(num)

    N = int(input("Введіть N: "))

    result = [num for num in numbers if 1 <= num <= N]

    if result:
        print(f"Числа, що належать інтервалу [1, {N}]: {result}")
    else:
        print(f"Жодне число не належить інтервалу [1, {N}]")


def task5():
    print("Програма для знаходження мінімального та максимального числа серед трьох")
    print("=" * 70)

    try:
        print("Введіть три числа:")
        num1 = float(input("Перше число: "))
        num2 = float(input("Друге число: "))
        num3 = float(input("Третє число: "))

        numbers = [num1, num2, num3]
        min_num = min(numbers)
        max_num = max(numbers)

        print("\nРезультат:")
        print(f"Введені числа: {num1}, {num2}, {num3}")
        print(f"Мінімальне число: {min_num}")
        print(f"Максимальне число: {max_num}")

    except ValueError:
        print("Помилка: Введіть правильне числове значення!")
    except Exception as e:
        print(f"Неочікувана помилка: {e}")


def main_menu():
    while True:
        print("\n" + "=" * 60)
        print("Виберіть завдання:")
        print("1. Знайомство (task1)")
        print("2. Обчислення Z (task2)")
        print("3. Кусочно-задана функція (task3)")
        print("4. Фільтрація чисел (task4)")
        print("5. Мінімум та максимум серед трьох чисел (task5)")
        print("0. Вихід")
        print("=" * 60)

        choice = input("Ваш вибір: ")

        if choice == '1':
            task1()
        elif choice == '2':
            task2()
            example_calculation()
        elif choice == '3':
            task3()
            test_function()
            interactive_mode()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '0':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
