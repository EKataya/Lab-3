print('Шифр Цезаря')
alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
#зашифровка сообщения
step=int(input('Шаг для шифрования:'))%26 #создаем переменную с шагом шифровки
line=input('Строка для шифрования на английском языке:').upper() #создаем переменную для сообщения
result='' 
  
for i in line:
    m=alphabet.find(i) #находим место символа в алфавите
    n=m+step #сдвигаем символ
    if i in alphabet:
        result+=alphabet[n] 
    else:
        resuit += i #задаем значение в результат
print('Зашифрованное слово: ',result)

#расшифровка сообщения
step=int(input('Шаг для шифрования:'))%26
line = input("Строка для расшифровки на английском языке: ").upper()
result = ''
for i in line:
    m = alphabet.find(i)
    n = m - step
    if i in alphabet:
        result += alphabet[n]
    else:
        result += i
print ('Расшифрованное слово:', result)
 

       




