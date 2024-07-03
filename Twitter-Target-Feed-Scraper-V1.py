from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

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
sleep(8.5)  # Wait for the login page to load

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("your_username")  # Add your username

next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()

# Wait for the password input to be present
sleep(3)
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("your_password")  # Add your password
log_in = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
log_in.click()

# Wait for the main page to load and search box to be present
sleep(10)
search_box = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(target_account)
search_box.send_keys(Keys.ENTER)

sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

# The next step requires some work. So follow this instruction carefully:
# Step 1: Go to the people tab, right click on the name of the target account and inspect element
# Step 2: This code is scraping ANI news, so upon inspecting that it shows you a bunch of code and then the text "ANI". 
# Step 3: Right click that code and copy XPATH and paste it below. The code will look like this //*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]
# Stpe 4: Ensure you use " " and ' ' carefully

sleep(3)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()

sleep(8)

Usernames = []
TimeStamps = []
Tweets = []
Replys = []
Retweets = []
Likes = []
Links = []

# Limit of tweets to collect
tweet_limit = 1000

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
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            sleep(3)
        else:
            break
except Exception as e:
    print(f"Script encountered an error: {e}")
finally:
    # Save the collected data regardless of the outcome
    print(len(Usernames), len(TimeStamps), len(Tweets), len(Replys), len(Retweets), len(Likes), len(Links))

    # Create DataFrame and save to Excel
    df = pd.DataFrame(zip(Usernames, TimeStamps, Tweets, Replys, Retweets, Likes, Links), columns=['Usernames', 'TimeStamps', 'Tweets', 'Replys', 'Retweets', 'Likes', 'Links'])

    # Save the DataFrame to an Excel file on the desktop
    output_path = "/Users/XYZ/Desktop/Scraper2-test/ANI_tweets.xlsx"
    df.to_excel(output_path, index=False)

    # Open the Excel file
    import os
    os.system(f'open "{output_path}"')

    # Close the driver
    driver.quit()