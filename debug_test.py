# Среднее арифмитическое
# list_temp = []
# list_temp = [1,2,5,65,6,32,2,2,2,21,5]
list_temp = [1,2,'5',65,6,32,2,2,2,21,5]
sum = 0
if len(list_temp)>0:
    for el in list_temp:
        sum += float(el)
    print(sum/len(list_temp))
else:
    print('List is empty')
