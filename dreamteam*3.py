
#1
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = self.Guns()
    def __str__(self):
        return (f"Солдат {self.name} к бою готов!")

    def fire(self):
        return 'тиги-тигитиш'

    class Guns:
        def __init__(self):
            self.model = 'ak-47'
            self.bullet_count = 0

        def add_bullet(self, count):
            self.bullet_count += count

        def shoot(self):
            if self.bullet_count <= 0:
                print('на нуле, заряди пушку!')
            elif self.bullet_count == 30:
                print('пушка заряжена')
            else:
                print('достаточно пуль')

            self.bullet_count -= 1
            print(f"{self.model} осталось : , {self.bullet_count}")


class Act_of_Shooting(Soldier.Guns):
    def __init__(self):
        super().__init__()

ryan = Soldier('Райан')
print(ryan.__str__())
print(ryan.fire())
start = Act_of_Shooting()
start.add_bullet(30)
start.shoot()

# 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

furniture = {'Спальня':4,
            'Гардероб':2,
            'Стол':1.5,
            }

class Home:
    home_type = "Villa"
    total_area = 120


    def __init__(self, furniture):
        self.furniture = furniture

    def list_furn_name(self):
        mebels = []

        for k in furniture:
            mebels.append(k)

        minus1 = furniture['Спальня']
        minus2 = furniture['Гардероб']
        minus3 = furniture['Стол']
        res = minus1+minus2+minus3
        print(f"тип дома - {Home.home_type},\nобщая площадь - {Home.total_area}м2, \nоставшаяся площадь - {Home.total_area-res}м2, \nсписок названий мебели - {mebels}")

villa = Home(furniture)
adder = villa.list_furn_name()

# 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def get_info(self):
        return f"name: {self.name}, age : {self.age},major : {self.major} "

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")

Steve = Steve.get_info()
Johnny = Johnny.get_info()
Penny = Penny.get_info()
print(Steve)
print(Johnny)
print(Penny)

# 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

amount = float(input('Введите сумму:'))
def dollarize(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(amount)

print(dollarize(amount))

import moneyfmt
cash = moneyfmt.Moneyfmt(987976.98876)
print(cash)
cash.update(10000.98547)
print(cash)
cash.update(-0.3)
print(cash.repr())

# 5
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle

import random

class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} в {}".format(self.val, self.suit))


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        card_v = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        for s in ['Черви', 'Бубны', 'Трефы', 'Пики']:
            for v in card_v:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name1):
        self.name1 = name1

        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()
bob = Player("Con")
bob.draw(deck)
bob.showHand()

# 6
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv

from bs4 import BeautifulSoup
from selenium import webdriver
import time, csv
from selenium.webdriver.common.by import By


path_to_driver = '/Users/sanjar/Desktop/parsing_lalafo/chromedriver'
url = 'https://lalafo.kg/kyrgyzstan/nedvizhimost'

class Parser:
    def __init__(self, path_to_driver, url):
        self.__driver = webdriver.Chrome(executable_path=path_to_driver)
        self.__driver.get(url)
        self.__tabs = []
        print('Подождите, идёт загрузка страницы...')
        time.sleep(3)


    def write_data(self):
        self.__items = None
        self.__btn = self.__driver.find_elements(By.CLASS_NAME, 'paginator-item')
        for i in range(1, len(self.__btn)):
            self.__driver.execute_script("window.scrollTo(600, window.scrollY + 1000)")
            soup = BeautifulSoup(self.__driver.page_source, 'html.parser')
            self.__items = soup.find_all('div', 'AdTileHorizontal')

            for item in self.__items:
                type_of_aprt = item.find('p', 'AdTileHorizontalDescription').text
                if 'Посуточная аренда' in type_of_aprt:
                    self.__tabs.append({
                        'Название' : item.find('a', 'AdTileHorizontalTitle').get_text(strip=True),
                        'Цена' : item.find('p', 'AdTileHorizontalPrice').get_text(strip=True),
                        'Фото' : item.find('img').get('src'),
                        'Адрес' : item.find('p', 'city-wrap').text,
                        'Дата' :  item.find('span', 'AdTileHorizontalDate').text,
                        'Ссылка' : 'https://lalafo.kg' + item.find('a', 'AdTileHorizontalTitle').get('href')
                    })

            self.__btn[i].click()


        if self.__tabs:
            with open('main.csv', 'w') as csv_file:
                for i in self.__tabs:
                    writer = csv.writer(csv_file)
                    writer.writerow([f"Название: {i['Название']}\n Цена: {i['Цена']}\n Фото: {i['Фото']}\n Адрес: {i['Адрес']}\n Дата: {i['Дата']}\n Ссылка: {i['Ссылка']}\n"])
        else:
            print('Парсер не успел спарсить данные по условию попробуйте еще раз!')
        print('Программа завершена!')
        self.__driver.close()


v1 = Parser(path_to_driver, url)
v1.write_data()

