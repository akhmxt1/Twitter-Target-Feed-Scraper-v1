# Twitter Target Feed Scraper using Selenium

If you have used my [Twitter-Search-Results-Scraper-v1](https://github.com/akhmxt1/Twitter-Search-Results-Scraper-v1?tab=readme-ov-file), this follows almost the same logic under the hood. However, there is some variation that you need to consider. I have left detailed instructions within the code to make things easy. This script will open Chrome, log into Twitter, search for the target account (in my case ANI news), go to the "People" tab, select the account, scroll down the feed, and save the tweets in an Excel sheet. 

**Requirement:** Basic knowledge of Python. Don't hesitate to play around, if you don't play you won't learn.

**NOTE:** If the Chrome driver/Selenium Web Driver reaches a point where it keeps "retrying" but can't move further, just close the Chrome window and it will save the progress. Twitter has severely limited the ability to scroll things even manually.

**Addendum:** Before you proceed, please make sure to use a throwaway account while using this script. Also, do not enable two-factor authentication (2FA) as this code was not written to take that into consideration. Moreover, TOTPs change every minute.

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation & Setup

To run this project, you need to have Python installed along with the necessary libraries. Follow these steps to set up your environment:

### Clone the repository

```bash
git clone https://github.com/akhmxt1/Twitter-Search-Results-Scraper.git
```

### Navigate to the project directory

Navigate to the directory where the project files are located. This ensures that all subsequent commands are run in the correct context and affect the correct files.

```bash
cd Twitter-Search-Results-Scraper
```

### Install dependencies

Install the necessary libraries specified in the requirements file.

```bash
pip install selenium
pip install pandas
```

### Download ChromeDriver

Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the specified path, for example: `/Users/XYZ/Desktop/chrome-driver/chromedriver-mac-arm64/chromedriver`.

**Note:** Ensure your ChromeDriver version matches the version of Chrome you have on your device.

### Set up Chrome options and specify the path to Chromedriver

Initialize the WebDriver:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver_path = "/Users/XYZ/Desktop/chrome-driver/chromedriver-mac-arm64/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
```

**Note:** Each line of code has comments to simplify the process. The README is here to help you set things up and explain the basic rules of usage.

## Features

- Automates login to Twitter
- Searches for specific account and collect tweets
- Saves collected data in an Excel file

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

## Contact

Check my [website](https://kalimahmed.com).

---
