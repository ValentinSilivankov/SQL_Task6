login = input('Введите логин: ')
password = input('Введите пароль: ')
db = input('Введите Базу данных: ')
DSN = f'postgresql://{login}:{password}@localhost:5432/{db}'