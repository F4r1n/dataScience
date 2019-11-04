from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.zalando.de/levisr-ex-boyfriend-trucker-jeansjacke-soft-as-butter-mid-le221g02u-k11.html");
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="z-pdp-topSection"]/div/div[2]/div[2]/div[2]/button/div/div/div[3]/div[2]/div/svg').click()

while True:
    button = driver.find_element_by_xpath(
        '//*[@id="advisor"]/div/div/div/button/div')
    if button is None:
        break;
    else:
        hover = ActionChains(driver).move_to_element(button)
        hover.perform()
        button.click()
