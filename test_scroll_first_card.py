from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("Nis_22@gmail.com")
driver.find_element(By.ID, "password").send_keys("558852")
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

# Добавь явное ожидание для загрузки списка карточек контента
WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"[class='places page__section']")))

# Найди карточку контента и сделай скролл до неё
element = driver.find_element(By.XPATH, ".//li[@class='places__item card']")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.quit()