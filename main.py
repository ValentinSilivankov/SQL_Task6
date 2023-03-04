import sqlalchemy
from sqlalchemy.orm import sessionmaker
from dsn import DSN
from models import create_tables, Book, Publisher, Sale, Shop, Stock


engine = sqlalchemy.create_engine(DSN)
create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()


publ_1 = Publisher(name='Пушкин')
publ_2 = Publisher(name='Чехов')
publ_3 = Publisher(name='Толстой')

session.add_all([publ_1, publ_2, publ_3])
session.commit()

book_1 = Book(title='Капитанская дочь', publisher=publ_1)
book_2 = Book(title='Руслан и Людмида', publisher=publ_1)
book_3 = Book(title='Война и Мир', publisher=publ_3)
book_4 = Book(title='Вишневый сад', publisher=publ_2)

session.add_all([book_1, book_2, book_3, book_4])
session.commit()

shop_1 = Shop(name='Буквоед')
shop_2 = Shop(name='Книги и Книжечки')

session.add_all([shop_1, shop_2])
session.commit()

stock_1 = Stock(id_book=1, id_shop=1, count=1)
stock_2 = Stock(id_book=2, id_shop=1, count=1)
stock_3 = Stock(id_book=3, id_shop=2, count=1)
stock_4 = Stock(id_book=4, id_shop=2, count=1)

session.add_all([stock_1, stock_2, stock_3, stock_4])
session.commit()

sale_1 = Sale(price=300, date_sale='11.09.2021', id_stock=1, count=1)
sale_2 = Sale(price=200, date_sale='11.09.2021', id_stock=2, count=1)
sale_3 = Sale(price=100, date_sale='11.09.2021', id_stock=3, count=1)
sale_4 = Sale(price=150, date_sale='11.09.2021', id_stock=4, count=1)

session.add_all([sale_1, sale_2, sale_3, sale_4])
session.commit()

if __name__ == "__main__":

    search = str(input('Введите 1 для поиска по id издателя. Введите 2 для поиска по имени издателя: '))

    if search == '1':
        req = str(input('Введите id издателя: '))
        res = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale).\
        join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.id == req)
        for book, shop, price, count, date in res:
            print(f'{book: <30} | {shop: <10} | {price*count: <8} | {date}')
    elif search == '2':
        req = str(input('Введите имя издателя: '))
        res = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale).\
        join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.name == req)
        for book, shop, price, count, date in res:
            print(f'{book: <30} | {shop: <10} | {price*count: <8} | {date}')
    else:
        print('Введены некорректные данные, либо издатель не существует')


session.close()