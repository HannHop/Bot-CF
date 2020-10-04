import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#if __name__ == '__main__':
#   print("I'm a car!")
print("dupor" + time.asctime(time.localtime()))

def task():
    print(time.asctime(time.localtime()) + " working! ")
    driver = webdriver.Chrome()
    driver.get("https://klubowicz.cityfit.pl/classes/clubs/100047")

schedule.every(10).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
