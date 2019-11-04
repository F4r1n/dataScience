from selenium import webdriver
from selenium import common
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r"F:\Programmieren\Python\chromedriver.exe")
driver.get("https://www.zalando.de/levisr-ex-boyfriend-trucker-jeansjacke-soft-as-butter-mid-le221g02u-k11.html");
driver.implicitly_wait(5)
element = '/html/body/div[4]/div/x-fragment-details/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div[1]/div/div/div/div/button'
driver.find_element_by_xpath("/html/body/div[4]/div/x-fragment-pdp/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/button").click()
driver.implicitly_wait(5)

while True:
    button = driver.find_element_by_xpath(element)
    try:
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()
        button.click()
    except common.exceptions.StaleElementReferenceException as identifier:
        break

reviews = driver.find_elements_by_class_name(
    "h-container.h-container--slide__inner.h-align-left")

with open("reviews.txt", "a+", encoding="utf-8") as file:
    for message in reviews:
        file.write(message.text + "\n")

driver.close()
