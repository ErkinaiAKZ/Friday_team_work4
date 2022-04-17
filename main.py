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
