from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


def Search_Input():
    browser.find_element_by_id('search').clear()
    browser.find_element_by_id('search').send_keys(search)


def Find_Region():
    browser.find_element_by_class_name('main-locationWrapper-3C0pT').click()
    browser.find_element_by_class_name('suggest-input-3p8yi').clear()
    browser.find_element_by_class_name('suggest-input-3p8yi').send_keys(region)
    time.sleep(1)
    browser.find_element_by_class_name('suggest-input-3p8yi').send_keys(Keys.ENTER)
    browser.find_element_by_class_name('popup-buttons-NqjQ3').click()



def Parse():
    global nnom, Url_ad
    ads = []
    counter = 0
    print(f'Ссылка запроса: {browser.current_url}')
    elem = browser.find_elements_by_class_name('iva-item-sliderLink-2hFV_')
    for i in range(0, len(elem)):
        ad = []
        ii = i + 1
        nomber = ''
        try:
            elem[i].click()
            nomber = '№' + str(ii)
            browser.switch_to.window(browser.window_handles[1])  # Открытие обьявления
            Url_ad = f'Ссылка объявления: {browser.current_url}'
            product = browser.find_element_by_class_name('title-info-title')  # Имя обьявления
            name_p = f'Название объявления: {product.text}'
            product_date = browser.find_element_by_class_name('title-info-metadata-item-redesign')  # Дата публикации
            first_date = f'Дата публикации: {product_date.text}'
            price = browser.find_element_by_class_name('item-price-wrapper')  # Цена
            Price = f'Цена: {price.text}'
            try:
                seller_info = browser.find_element_by_class_name('seller-info-col')  # Информация о продавце
                seller = f'Информация о продавце: {seller_info.text}'
            except:
                seller_info = browser.find_element_by_class_name('seller-info  js-seller-info')
                seller = f'Информация о продавце: {seller_info.text}'
            product_info = browser.find_element_by_class_name('item-view-block')  # Краткое описание
            product_infor = f'Информация объявления: {product_info.text}'
            addres = browser.find_element_by_class_name('item-address')  # Адресс
            location = f'Адрес: {addres.text}'
            browser.close()  # Закрытие данной вкладки
            browser.switch_to.window(browser.window_handles[0])  # Возвращение на 1 вкладку
            # Создание обьявления
            ad.append(nomber)
            ad.append(Url_ad)
            ad.append(name_p)
            ad.append(first_date)
            ad.append(Price)
            ad.append(seller)
            ad.append(product_infor)
            ad.append(location)
        except:
            counter += 1
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            print(f'ERROR: №{counter}; AD: {nomber}; TIME: {datetime.datetime.now()}; {Url_ad}')
        ads.append(ad)  # Создание обьявлений
        nnom = i
    return ads, nnom


def main(reg, sea):
    global browser, parr, region, search, ppar, paar
    # Запрос
    region = reg
    search = sea
    # Настройки
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Фоновый режим
    browser = webdriver.Chrome(executable_path='D:\\Project\\Browser\\chromedriver.exe', options=options)
    try:
        start_time = datetime.datetime.now()  # Начало выполнения
        print(start_time)
        print('*' * 40)
        browser.get(url='https://www.avito.ru/rossiya')  # Заходит на авито
        browser.implicitly_wait(1)
        Find_Region()
        Search_Input()
        button = browser.find_element_by_class_name('form-part-button-35XEq').click()  # Кнопка найти
        parr = Parse()
        finish_time = datetime.datetime.now()  # Конец выполения
        spent_time = finish_time - start_time  # Затрачено времени
        print('*' * 40)
        print(spent_time)
        print(parr)
        print('*' * 40)
        # обработка списка
        parr1 = parr[0]
        parr2 = [x for x in parr1 if x != []]
        parr = str(parr)
        parr2.append(parr[1])
        print(parr2)
    except Exception as ex:
        print(ex)
        parr2 = ['ERROR', 0]
    finally:
        browser.close()
        browser.quit()
    return parr2
