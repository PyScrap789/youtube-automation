from selenium import webdriver
from selenium.webdriver.common.by import By

def screenshot_post(url, post_count, limit):
    driver = webdriver.Firefox()

    driver.maximize_window()

    driver.get(f"https://reddit.com{url}")
    driver.find_element(By.TAG_NAME, "shreddit-post").screenshot(f'posts/{post_count}/post_screenshot.png')

    driver.quit()