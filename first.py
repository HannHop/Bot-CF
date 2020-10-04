import schedule
import time
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



#if __name__ == '__main__':
#   print("I'm a car!")
from selenium.webdriver.support.wait import WebDriverWait

print("dupor" + time.asctime(time.localtime()))

classes_date = "09.10.2020"
classes_time = "09:00"
classes_name = "JOGA"

def task():
    print(time.asctime(time.localtime()) + " working! ")
    driver = webdriver.Chrome()
    driver.get("https://klubowicz.cityfit.pl/classes/clubs/100047")
#09.10.2020 | 09:00
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'event-details')))
    events = driver.find_elements_by_class_name("event-details")
    dummy = driver.find_element_by_class_name("cf__schedule--header-container")
    print(len(events))

    for event in events:
        event.click()
        bold_elements = driver.find_elements_by_css_selector(".cf__schedule--event--popup .cf_font-b--14")
        if bold_elements[0].text == classes_name and bold_elements[1].text == classes_date + " | " + classes_time:
            print(bold_elements[0].text + " " + bold_elements[1].text)
            driver.find_element_by_css_selector(".cf__schedule--event--popup button").click()
        dummy.click()


schedule.every(30).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
