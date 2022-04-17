# try:
#     исполняем код
# except Exception as e:
#     обработка исключения
# else:
#     код, который будет выполнен, если не возникнет исключения
# finally:
#     код, который будет выполнен всегда
#

# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
#
# try:
#     print(a/b)
# except ZeroDivisionError as er:
#     print(er)
# else:
#     print('Все хорошо')
# finally:
#     print('Это было не просто')

f = open('data')
int_arr_list = []
try:
    for line in f:
        int_arr_list.append(int(line))
except ValueError as e:
    print('я нашел не число!', e)
else:
    print('Все прошло хорошо')
finally:
    f.close()

print(int_arr_list)
