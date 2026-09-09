import secrets 
import string

a = (int(input("Введите длину пароля минимум 8 символов:")))

while a <= 7:
    print("Пароль должен быть минимум 8 символов!")
    a = (int(input("Введите длину пароля минимум 8 символов:")))

if a >= 8:
    penis = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(penis) for i in range(a))
    print("Ваш пароль:", password)