# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def main():
    with open('text1.txt', 'r') as data:
        text = data.readline()
    text = ' '.join(list(filter(lambda el: 'абв' not in el.lower(), text.split())))
    print(text)
    
if __name__ == '__main__':
    main()