from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class CookieValidator:
    def check_samesite_cookies_with_selenium(self, url):
        """Verify if cookies have SameSite attribute set to Lax or Strict using Selenium."""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(url)
            cookies = driver.get_cookies()
            for cookie in cookies:
                if 'sameSite' in cookie:
                    if cookie['sameSite'].lower() in ['lax', 'strict']:
                        return True
            return False
        finally:
            driver.quit()