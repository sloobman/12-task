s = '1' * 120# формируем строку из 120 идущих подряд цифр 1
while '666' in s or '111' in s:
    if '666' in s:
        s = s.replace('666', '1', 1)# заменяем ТОЛЬКО первое слева вхождение
    else:
        s = s.replace('111', '6', 1)
print(s)# выводим полученную строку
