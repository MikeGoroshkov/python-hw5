# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def main():
    with open('original.txt', 'r') as data:
        text = data.readline()
    encoded = rle_encode(text)
    print(encoded)
    with open('encoded.txt', 'w') as data_1:
        data_1.write(encoded)
    decoded = rle_decode(encoded)
    print(decoded)
    with open('decoded.txt', 'w') as data_2:
        data_2.write(decoded)
    
def rle_encode(text):
    code = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            code += f"{count}*{text[i-1]} "
            count = 1
        if i == len(text) - 1:
            code += f"{count}*{text[i]}"
    return code

def rle_decode(ls):
    decode = ''
    for i in ls.split():
        i = i.split("*")
        decode += int(i[0])*i[1]
    return decode
      
        
if __name__ == '__main__':
    main()