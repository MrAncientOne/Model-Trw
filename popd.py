
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import random


def popu():
    places=[]
    pop_dict=[]
    with open("file.txt", "r") as f:
        places=str(f.read()).split()

    places=random.choices(places,k=20)
    driver = webdriver.Firefox()
    
    for i in range(20):
        
        driver.get("https://www.maps.ie/population/")
        #driver.get(driver.getCurrentURL());
        element = driver.find_element(By.ID, "search_address") 
        element.send_keys(f"{places[i]} Chennai")
        time.sleep(7)
        element.send_keys(Keys.DOWN)
        time.sleep(5)
        element.send_keys(Keys.ENTER)
        time.sleep(5)

        radius=driver.find_element(By.ID, "fixed_radius")
        time.sleep(5)
        radius.send_keys(Keys.DOWN)
        time.sleep(5)
        radius.send_keys(Keys.ENTER)
        time.sleep(5)
        pop=driver.find_element(By.ID, "pop-count")
        pop_dict.append([places[i],(pop.text).replace('.','')])
    #print(pop_dict)
    print([pop_dict,places])
    return ([pop_dict,places])


if __name__ == "__main__":
    print(popu())

    