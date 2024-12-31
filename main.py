import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_forms(url):
    """Extract forms from a given URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('form')

def extract_csrf_token(form):
    """Find CSRF token in a form."""
    for input_tag in form.find_all('input'):
        if 'csrf' in input_tag.get('name', '').lower() or 'token' in input_tag.get('name', '').lower():
            return input_tag.get('value', '')
    return None

def is_token_valid(token):
    """Check if the token has a minimum of 32 characters."""
    return len(token) >= 32

def check_samesite_cookies_with_selenium(url):
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

def is_token_unique(tokens):
    """Check if all tokens in the list are unique."""
    return len(tokens) == len(set(tokens))

def check_site_security(url):
    """Check the security of a site based on CSRF and cookies."""
    forms = get_forms(url)
    if not forms:
        return "Site is vulnerable: No forms found."

    tokens = []
    for form in forms:
        token = extract_csrf_token(form)
        if not token:
            return "Site is vulnerable: No CSRF token found in forms."
        if not is_token_valid(token):
            return "Site is vulnerable: CSRF token is too short."
        tokens.append(token)

    # Send a second request to check token reusability
    response = requests.get(url)
    forms = get_forms(url)
    for form in forms:
        token = extract_csrf_token(form)
        if token:
            tokens.append(token)

    if not is_token_unique(tokens):
        return "Site is vulnerable: CSRF token is reused."

    # Check cookie security with Selenium
    if not check_samesite_cookies_with_selenium(url):
        return "Site is vulnerable: Cookies do not have SameSite attribute set."

    return "Site is safe."

if __name__ == "__main__":
    url = input("Enter the URL of the website to check: ")
    result = check_site_security(url)
    print(result)
