def lusky_Fucky(tiket_number):
    if (len(str(tiket_number)) != 6) or (type(tiket_number) is not int):
        return 'Введите только 6 цифр!'
    else:
        tiket_number1 = list(str(tiket_number))
        sum1 = int(tiket_number1[0]) + int(tiket_number1[1]) + int(tiket_number1[2])
        sum2 = int(tiket_number1[3]) + int(tiket_number1[4]) + int(tiket_number1[5])
        if sum1 == sum2:
            return 'Билет %s счастливый' %tiket_number
        else:
            return 'Билет %s несчастливый' %tiket_number

number = 547693
print(lusky_Fucky(number))