import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

def screenshot_posts_and_comments(url, post_count, limit):
    driver = webdriver.Firefox()

    driver.maximize_window()

    driver.get(f"https://reddit.com{url}")
    driver.find_element(By.TAG_NAME, "shreddit-post").screenshot(f'posts/{post_count}/post_screenshot.png')

    # if not os.path.exists(f"{post_count}/comments"):
    #     os.makedirs(f"{post_count}/comments")

    # for comment in driver.find_elements(By.TAG_NAME, "shreddit-comment"):
    #     if comment_count >= limit:
    #         break

    #     if comment.get_attribute("author") == "AutoModerator":
    #         continue

    #     comment_shadow_root = comment.shadow_root

    #     # print(comment_shadow_root.find_elements(By.CLASS_NAME, 'contents')[1])

    #     comment.screenshot(os.path.join(f"{post_count}/comments", f"{str(comment_count)}.png"))
    #     comment_count += 1

    driver.quit()