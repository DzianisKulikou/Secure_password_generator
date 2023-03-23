from random import sample

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

n = int(input('Здравствуйте, сколько паролей вы хотели бы создать? : '))
length = int(input('Сколько символов должно быть в пароле? : '))
symbol1 = input('В пароле можно использовать цифры (01...89)? (да/нет) : ')
symbol2 = input('В пароле можно использовать строчные буквы (ab...yz)? (да/нет) : ')
symbol3 = input('В пароле можно использовать прописные буквы (AB...YZ)? (да/нет) : ')
symbol4 = input('В пароле можно использовать символы (!#$%&*+-=?@^_)? (да/нет) : ')
exception = input('Исключить из пароля неоднозначные символы (il1Lo0O)? (да/нет) : ')

if symbol1.lower() == 'да':
    chars += digits
if symbol2.lower() == 'да':
    chars += lowercase_letters
if symbol3.lower() == 'да':
    chars += uppercase_letters
if symbol4.lower() == 'да':
    chars += punctuation
if exception.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    return sample(chars, length)

for _ in range(n):
    print(''.join(generate_password(length, chars)))

print('Все ваши пароли созданы, досвидания!')

