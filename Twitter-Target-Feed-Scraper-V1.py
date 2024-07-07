from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import random

# Set up Chrome options
chrome_options = Options()

# Specify the path to the Chromedriver executable
driver_path = "/Users/XYZ/Desktop/chrome-driver/chromedriver-mac-arm64/chromedriver"
service = Service(driver_path)

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the login page
driver.get("https://x.com/login")

# User you wish to search, save it in a variable
target_account = """ @ANI """

# Set up login
sleep(random.uniform(7, 10))  # Wait for the login page to load

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("your_username")  # Add your username

next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

# Wait for the password input to be present
sleep(random.uniform(2.5, 4.5))
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("your_password")  # Add your password
log_in = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
log_in.click()

# Wait for the main page to load and search box to be present
sleep(random.uniform(8, 12))
search_box = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(target_account)
search_box.send_keys(Keys.ENTER)

sleep(random.uniform(2.5, 4.5))
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()

sleep(random.uniform(2.5, 4.5))
profile = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()

sleep(random.uniform(7, 10))

Usernames = []
TimeStamps = []
Tweets = []
Replys = []
Retweets = []
Likes = []
Links = []

# Limit of tweets to collect
tweet_limit = 5000

def human_like_scroll(driver, scroll_limit):
    current_scrolls = 0
    while current_scrolls < scroll_limit:
        scroll_height = random.uniform(300, 600)
        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
        sleep(random.uniform(1, 3))
        current_scrolls += 1

try:
    # Collect tweets
    while len(Tweets) < tweet_limit:
        articles = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
        for article in articles:
            if len(Tweets) >= tweet_limit:
                break
            try:
                Username = article.find_element(By.XPATH, ".//span[contains(@class, 'css-1jxf684') and contains(text(), '@')]").text
                TimeStamp = article.find_element(By.XPATH, ".//time").get_attribute('datetime')
                Tweet = article.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
                Reply = article.find_element(By.XPATH, ".//button[@data-testid='reply']").text
                Retweet = article.find_element(By.XPATH, ".//button[@data-testid='retweet']").text
                Like = article.find_element(By.XPATH, ".//button[@data-testid='like']").text
                Link = article.find_element(By.XPATH, ".//a[contains(@href, '/status/')]").get_attribute('href')
                
                Usernames.append(Username)
                TimeStamps.append(TimeStamp)
                Tweets.append(Tweet)
                Replys.append(Reply)
                Retweets.append(Retweet)
                Likes.append(Like)
                Links.append(Link)
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        if len(Tweets) < tweet_limit:
            human_like_scroll(driver, scroll_limit=random.randint(1, 3))
        else:
            break
except Exception as e:
    print(f"Script encountered an error: {e}")
finally:
    # Save the collected data regardless of the outcome
    print(len(Usernames), len(TimeStamps), len(Tweets), len(Replys), len(Retweets), len(Likes), len(Links))

    # Create DataFrame and save to Excel
    df = pd.DataFrame(zip(Usernames, TimeStamps, Tweets, Replys, Retweets, Likes, Links), columns=['Usernames', 'TimeStamps', 'Tweets', 'Replies', 'Retweets', 'Likes', 'Links'])

    # Save the DataFrame to an Excel file on the desktop
    output_path = "/Users/XYZ/Desktop/Scraper2-test/ANI_tweets.xlsx"
    df.to_excel(output_path, index=False)

    # Open the Excel file
    import os
    os.system(f'open "{output_path}"')

    # Close the driver
    driver.quit()