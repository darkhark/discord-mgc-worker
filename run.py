import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import configs


def work_for_mgc():
    # Replace this with the URL of the channel you want to send the message to
    channel_url = f"https://discord.com/channels/{configs.SERVER_ID}/{configs.CHANNEL_ID}"

    # Replace this with the message you want to send
    message = "?work"

    # Set up the Chrome webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)

    # Log in to Discord
    driver.get("https://discord.com/login")
    time.sleep(2) # wait for page to load
    driver.find_element("name", "email").send_keys(configs.EMAIL)
    driver.find_element("name", "password").send_keys(configs.PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    time.sleep(5) # wait for login

    # Go to the specified channel
    driver.get(channel_url)
    time.sleep(10) # wait for channel to load

    # Send the message
    driver.find_element(By.CSS_SELECTOR, 'div[data-slate-editor="true"]').send_keys(message)
    driver.find_element(By.CSS_SELECTOR, 'div[data-slate-editor="true"]').send_keys(Keys.RETURN)

    # Close the webdriver
    driver.quit()


if __name__ == "__main__":
    # Start the loop in 1 hour and 25 minutes
    time.sleep(60*60*1 + 60 * 25)

    # Run the function every for hours and random minutes between 1 and 7
    while True:
        work_for_mgc()
        time.sleep(60*60*4 + 60 * random.randint(1, 7))