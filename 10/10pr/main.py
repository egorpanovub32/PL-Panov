#4.1
m = []
with open('./Панов Е. А._УБ-32_vvod.txt', 'r') as f:
    for i in f:
        bez = i.replace('[','').replace(']','').replace("'",'').replace(',','')
        ch = [int(num) for num in bez.split()]
        m.append(ch)


s = []
for ch in range(len(m)):
    s.append(sum(m[ch]))
print("Строка с наибольшей суммой: ", m[s.index(max(s))])
print("Сумма элементов: ", max(s))
print("Строка с наименьшей суммой: ", m[s.index(min(s))])
print("Сумма элементов: ", min(s))


with open('./Панов Е. А._УБ-32_vivod.txt','w') as f:
    f.write("Stroka s naibolshei summoi: {}\n".format(m[s.index(max(s))]))
    f.write("Summa elementov: {}\n".format(max(s)))
    f.write("Stroka s naimenshei summoi: {}\n".format(m[s.index(min(s))]))
    f.write("Summa elementov: {}\n".format(min(s)))