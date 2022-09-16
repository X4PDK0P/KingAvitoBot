from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
# Запрос
def main(region1, search1):
    global browser, region, search
    region = region1
    search = search1
    # Настройки
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser =  webdriver.Chrome(executable_path = 'D:\\Project\\chromedriver.exe', options=options)
    # start()
    return start()
def Search_Input():
    global search
    search_input = browser.find_element_by_id('search')
    search_input.clear()
    search_input.send_keys(search)
    browser.implicitly_wait(10)
def Find_Region():
    global region
    button_region = browser.find_element_by_class_name('main-locationWrapper-3C0pT').click() # выбрать город клик
    browser.implicitly_wait(10)
    search_region_input = browser.find_element_by_class_name('suggest-input-3p8yi')
    search_region_input.clear()
    search_region_input.send_keys(region)
    browser.implicitly_wait(10)
    search_region_input.send_keys(Keys.ENTER)
    time.sleep(1)
    button = browser.find_element_by_class_name('popup-buttons-NqjQ3').click() # Поиск обьявлений по региону
    browser.implicitly_wait(10)
def Parse():
    ads = []
    print(f'CURrently URL is: {browser.current_url}')
    elem = browser.find_elements_by_class_name('iva-item-sliderLink-2hFV_')
    for i in range(0, len(elem)):
        ii = i + 1
        ads = []
        time.sleep(1)
        elem[i].click()
        print('№' + str(ii))
        print('#' * 40)
        browser.implicitly_wait(10)
        browser.switch_to.window(browser.window_handles[1]) # Открытие обьявления
        browser.implicitly_wait(10)
        ads.append(f'Currently URL is: {browser.current_url}')
        print(f'Currently URL is: {browser.current_url}')
        product = browser.find_element_by_class_name('title-info-title') # Имя обьявления
        ads.append(f'Product is: {product.text}')
        product_date = browser.find_element_by_class_name('title-info-metadata-item-redesign') # Дата публикации
        ads.append(f'Product date is: {product_date.text}')
        price = browser.find_element_by_class_name('item-price-wrapper') # Цена
        ads.append(f'Price is: {price.text}')
        try:
            seller_info = browser.find_element_by_class_name('seller-info-col') # Информация о продавце
            ads.append(f'Seller info is: {seller_info.text}')
        except:
            seller_info = browser.find_element_by_class_name('seller-info  js-seller-info')
            ads.append(f'Seller info is: {seller_info.text}')
        product_info = browser.find_element_by_class_name('item-view-block') # Краткое описание
        ads.append(f'Product info: {product_info.text}')
        addres = browser.find_element_by_class_name('item-address') # Адресс
        ads.append(f'Addres is: {addres.text}')
        print(ads)
        browser.close() # Закрытие данной вкладки
        browser.switch_to.window(browser.window_handles[0]) # Возвращение на 1 вкладку
        return ads
def start():
    global browser
    try:
        start_time = datetime.datetime.now() # Начало выполнения
        print(start_time)
        print('*' * 40)
        browser.get(url='https://www.avito.ru/rossiya') # Заходит на авито
        browser.implicitly_wait(1)
        Find_Region()
        Search_Input()
        button = browser.find_element_by_class_name('index-button-2q4Wv').click() # Кнопка найти
        #Parse()
        finish_time = datetime.datetime.now() # Конец выполения
        spent_time = finish_time - start_time # Затрачено времени
        print('*' * 40)
        print(spent_time)
    except Exception as ex:
        print(ex)
    finally:
        browser.close()
        browser.quit()
    return Parse()