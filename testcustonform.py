import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

def test_input1():
    service = Service('D:\webdriver\chromedriver-win64\chromedriver.exe')
    service.start()
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1/customerphp/customer.php")
    
    name = driver.find_element(By.ID, "firstName")
    last = driver.find_element(By.ID, "lastName")
    age = driver.find_element(By.ID, "age")
    drp_title = Select(driver.find_element(By.ID, "title"))
    drp_title.select_by_index(0)
    
    name.send_keys("johnjohn")
    last.send_keys("canonc")
    age.send_keys("2")
    
    submit = driver.find_element(By.ID, "submit")
    submit.click()
    
    time.sleep(1)  # Add a short delay to ensure the page loads completely
    
    result = driver.find_element(By.ID, "firstName").text
    assert result == "First Name: johnjohn"
    
    
    driver.close()
    service.stop()

    

# Running the test
if __name__ == "__main__":
    test_input1()
