from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_olx_car_covers():
    url = "https://www.olx.in/items/q-car-cover"

    # Headless Chrome setup
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Wait for JS to load

    items = driver.find_elements(By.CSS_SELECTOR, 'li.EIR5N')  # OLX uses this class for items

    data = []
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, 'span._2tW1I').text
            price = item.find_element(By.CSS_SELECTOR, 'span._89yzn').text
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            data.append({"Title": title, "Price": price, "Link": link})
        except Exception as e:
            print("Error parsing item:", e)

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("olx_car_covers.csv", index=False)
    print("Saved results to olx_car_covers.csv")

if __name__ == "__main__":
    scrape_olx_car_covers()
