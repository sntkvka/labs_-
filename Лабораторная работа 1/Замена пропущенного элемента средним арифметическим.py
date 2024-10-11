numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

string_1 = numbers[0:4]
string_2 = numbers[5:]
string_12 = string_1+string_2
total = sum(string_12)
count = len(numbers)
avarage = total/count
incorrect = numbers[4]
correct = avarage
numbers[4] = correct
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers )
