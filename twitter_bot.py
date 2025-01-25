from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def twitter_task(tweet_url):
    driver = webdriver.Chrome()

    try:
        print("[INFO] Memulai tugas Twitter.")
        driver.get("https://twitter.com/login")
        
        # Tunggu sampai elemen username tersedia
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@name='session[username_or_email]']"))
        )

        # Input username
        driver.find_element(By.XPATH, "//*[@name='session[username_or_email]']").send_keys("krmnlim")
        
        # Tunggu sampai elemen password tersedia
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@name='session[password]']"))
        )
        
        # Input password
        driver.find_element(By.XPATH, "//*[@name='session[password]']").send_keys("karmin123@")
        
        # Klik tombol login
        login_button = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/button/div"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, login_button))
        )
        driver.find_element(By.XPATH, login_button).click()

        print("[INFO] Berhasil login sebagai krmnlim.")
        time.sleep(5)

        # Akses URL tweet
        driver.get(tweet_url)
        print(f"[INFO] Membuka URL tweet: {tweet_url}.")
        time.sleep(3)

        # Klik tombol retweet
        retweet_button = "//*[@id='id__baxe9tuemra']/div[2]/button/div/div[2]/span/span/span"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, retweet_button))
        )
        driver.find_element("xpath", retweet_button).click()
        time.sleep(1)
        driver.find_element("xpath", "//div[@data-testid='retweetConfirm']").click()

        # Klik tombol like
        like_button = "//*[@id='id__baxe9tuemra']/div[3]/button/div/div[2]/span/span/span"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, like_button))
        )
        driver.find_element("xpath", like_button).click()

        print("[INFO] Tugas Twitter selesai.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
    finally:
        driver.quit()
        print("[INFO] Menutup driver.")

# =================== MAIN FUNCTION ===================
if __name__ == "__main__":
    TWEET_URL = "https://x.com/NewTread_/status/1882458950790205638"  # URL tweet yang diberikan
    print("[INFO] Memulai tugas Twitter.")
    twitter_task(TWEET_URL)
    print("[INFO] Tugas Twitter selesai.")
