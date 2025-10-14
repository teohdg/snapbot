import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def close_brave():
    try:
        subprocess.run("taskkill /f /im brave.exe", shell=True)
    except Exception as e:
        print(f"error: {e}")

def init_driver():
    options = Options()
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(r"--user-data-dir=C:\Users\****USERNAMER****\AppData\Local\BraveSoftware\Brave-Browser\User Data")
    options.add_argument(r"--profile-directory=Profile *****PROFILE##*****")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--no-first-run")
    service = Service(ChromeDriverManager(driver_version="141.0.7390").install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def take_photo():
    driver = init_driver()
    driver.get("https://www.snapchat.com/web")
    time.sleep(5)

    xpaths = [
        '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]',
        '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]',
        '//*[@id="snap-preview-container"]/div[2]/button[2]',
        '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div/div[2]/button',
        '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div/ul/li[1]/div/button',
        '//*[@id="root"]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/button'
    ]

    for xpath in xpaths:
        try:
            elem = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            elem.click()
            time.sleep(2)
        except Exception as e:
            print(f"couldnt click {xpath}: {e}")

    driver.quit()

if __name__ == "__main__":
    close_brave()
    take_photo()
