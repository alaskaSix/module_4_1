#Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции
# divide из модулей fake_math и true_math, назвав их разными именами на своё
# усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
#Запустите эти функции в модуле module_4_1, передав первым аргументом
#произвольное число отличное от 0, вторым аргументом - 0
#Выведи результаты вызовов этих функций на экран(в консоль).
from fake_math import divide as fm
from true_math import divide as tm
result1 = fm(69, 3)
result2 = fm(3, 0)
result3 = tm(49, 7)
result4 = tm(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)