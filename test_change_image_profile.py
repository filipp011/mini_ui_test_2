from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

#Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("Nis_22@gmail.com")
driver.find_element(By.ID, "password").send_keys("558852")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Добавь явное ожидание загрузки страницы
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Кликни по изображению профиля
driver.find_element(By.XPATH, ".//div[@class='profile__image']").click()

# Введи ссылку на изображение
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Сохрани новое изображение
driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div/form/button[2]").click()

# Проверь атрибут style для элемента изображения профиля
style = driver.find_element(By.XPATH, ".//div[@class='profile__image']").get_attribute('style')
assert avatar_url in style

driver.quit()