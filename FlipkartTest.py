from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys


# Path to ChromeDriver executable
chrome_driver_path = "/Users/mahimaquadras/Documents/Flipkart-Automation/chrome-mac-x64"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    driver.get('https://www.flipkart.com/')
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("Samsung Galaxy S10")
    search_bar.send_keys(Keys.RETURN)

    # Wait for result to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "TB_InB")))

    # Click on Mobiles 
    driver.find_element(By.LINK_TEXT, "Mobiles").click()

    
    # Applying filters i.e Samsung and Flip Assured
    import time
    samsung_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-2-12 > div > div:nth-child(1) > div > section:nth-child(4) > div._3FPh42 > div > div > div > label > div._3879cV")))
    samsung_filter.click()

    time.sleep(2)
    flipkart_assured = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-2-12 > div > div:nth-child(1) > div > section._2hbLCH._24gLJx > label > div._3879cV > div")))
    flipkart_assured.click()

# Sort by price high to low
    price_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#container > div > div._36fx1h._6t1WkM._3HqJxg > div > div:nth-child(2) > div._1YokD2._2GoDe3.col-12-12 > div > div > div._5THWM1 > div:nth-child(5)")))
    price_filter.click()

# Wait for sorted results to load
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#container > div > div._36fx1h._6t1WkM._3HqJxg > div > div:nth-child(2)")))

# Get product details
    product_names = driver.find_elements(By.CLASS_NAME, "_4rR01T")
    display_prices = driver.find_elements(By.CLASS_NAME, "_30jeq3")
    product_links = driver.find_elements(By.XPATH, "//a[@class='_1fQZEK']")

# Print the list of parameters
    for i in range(len(product_names)):
        print("Product Name:", product_names[i].text)
        print("Display Price:", display_prices[i].text)
        print("Link to Product Details Page:", product_links[i].get_attribute("href"))
        print("\n")


    with open("product_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Display Price", "Link to Product Details Page"])
        for i in range(len(product_names)):
            writer.writerow([product_names[i].text, display_prices[i].text, product_links[i].get_attribute("href")])

    


finally:
    # Stop the driver
    driver.quit()
