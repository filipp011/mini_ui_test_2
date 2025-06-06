import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
# Найди поле "Email" и заполни его
driver.find_element(By.ID, "email").send_keys("Nis_22@gmail.com")

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, "password").send_keys("558852")

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

# Добавь явное ожидание для загрузки списка карточек контента
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Запомни title последней карточки
title_before = driver.find_element(By.XPATH, ".//li[@class='places__item card']//h2[@class='card__title']").text

# Кликни по кнопке добавления нового контента
driver.find_element(By.XPATH, ".//button[@class='profile__add-button']").click()

# сгенерируй новое место и введи его в поле названия
new_title = "Дагестан"
driver.find_element(By.ID, "place-name").send_keys(new_title)

# В поле ссылки на изображение введи ссылку
url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenium.jpeg"
driver.find_element(By.ID, "place-link").send_keys(url)

# Сохрани контент
driver.find_element(By.XPATH,"./html/body/div/div/div[2]/div/form/button[2]").click()

# Дождись появления кнопки удаления карточки
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']")))

# Проверь, что на карточке отображается верное название
title_after = driver.find_element(By.XPATH, "//h2[@class='card__title']").text
assert title_after == new_title

# Запомни количество карточек до удаления
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# Удали карточку
driver.find_element(By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']").click()

# Дождись, что title последней карточки равен title_before
WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element(
    (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))

# Проверь, что количество карточек стало на одну меньше
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_before - cards_after == 1

driver.quit()