import time
import webdriver
import By
import ChromeDriverManager


def write_file():
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://www.reddit.com/r/TheOnion/")
    time.sleep(1)

    elem = browser.find_element(By.TAG_NAME, "Body")

    no_of_pagedowns = 300

    posts = []

    f = open("headlines.txt", 'w', encoding='utf-8')

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0)
        no_of_pagedowns -= 1
        print(no_of_pagedowns)
        post_elems = browser.find_elements(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
        for post in post_elems:
            if post.text not in posts and post.text != "About Community" and post.text != "Related " \
                    "Communities" and post.text != "Moderators" and post.text != "":
                posts.append(post.text)
                f.write(post.text + "\n")

    f.close()
