from calculator import Calculator

def calc_memu():
    stop_work = False
    while(stop_work != True):
        print("Какую операцию вы хотите произвести?")
        print("1-Сложение(+); \n2-Вычитание(-); \n3-Умножение(*); \n4-Деление(/); \n5-Выход ?")
        user_input = int(input())
        if(user_input == 1 ):
            c = input_value()
            print(f"Результат равен: {c.__add__()}")
            print('')
        elif(user_input == 2):
            c = input_value()
            print(f"Результат равен: {c.__sub__()}")
            print('')
        elif(user_input == 3):
            c = input_value()
            print(f"Результат равен: {c.__mul__()}")
            print('')
        elif(user_input == 4): 
            c = input_value()
            if (c.arg2!=0):
                print(f"Результат равен: {c.__div__()}")
            else: print("Деление на 0 невозможно")    
            print('')
        elif(user_input == 5):
            print("Завершение работы")
            stop_work = True
        else:
            print("ВВедено некорректное значение")

def input_value():
    print("ввведите первый аргумент")
    arg1 = int(input())
    print("ввведите второй аргумент")
    arg2 = int(input())
    c= Calculator(arg1, arg2)
    return c
    