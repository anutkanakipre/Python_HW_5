# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# https://habr.com/ru/post/141827/

# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

# С помощью алгоритма сжатия данных кодирования длин серий (RLE), примененного к приведенной выше гипотетической строке сканирования, 
# ее можно представить как 12W1B12W3B24W1B14W

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        
        if char != prev_char:
            
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        #если символ это цифра 
        if char.isdigit():
            # мы добавляем ее в наш счетчик цифр
            count += char
        else:
            # значит тут не цифра 
            # и нам надо этот символ расшифровать умножением на счетчик
            # в финальный результат
            decode += char * int(count)
            count = ''
    return decode

with open('encode.txt', 'r') as file:
    decoded = file.read()

with open('decode.txt', 'w') as file:
    encoded = rle_encode(decoded)
    finaldecoded = rle_decode(encoded)
    file.write(encoded)

print('Модуль сжатия: \t' + rle_encode(decoded))
print('Модуль восстановения данных: \t' + finaldecoded)