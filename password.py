def main():

    password = input('Введите пароль: ')
    while not get_password(password):
        print('Этот пароль недоступен')
        password = input('Введите новый пароль: ')
    print('Это допустимый пароль')

def get_password(password):

    len_correct = False
    upper_correct = False
    lower_correct = False
    digit_correct = False
    if len(password)>=7:
        len_correct = True
    for ch in password:
        if ch.islower():
            lower_correct = True
        if ch.isupper():
            upper_correct = True
        if ch.isdigit():
            digit_correct = True
    if len_correct and upper_correct and lower_correct and digit_correct:
        valid = True
    else:
        valid = False
    return valid
main()