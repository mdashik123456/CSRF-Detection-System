# CSRF Detection System
This project is a CSRF (Cross-Site Request Forgery) Detection System that automates the analysis of web applications for CSRF vulnerabilities and evaluates the security measures in place.

## Features
-> Extracts forms from web pages.

-> Identifies CSRF tokens and validates their length.

-> Checks for token uniqueness across multiple requests.

-> Validates SameSite cookie attributes for security (using Selenium).

-> Determines if a site is vulnerable or safe based on CSRF and cookie evaluations.

```
requests
beautifulsoup4
selenium
webdriver-manager
```
