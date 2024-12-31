# CSRF Detection System
This project is a CSRF (Cross-Site Request Forgery) Detection System that automates the analysis of web applications for CSRF vulnerabilities and evaluates the security measures in place.

## Features
-> Extracts forms from web pages.

-> Identifies CSRF tokens and validates their length.

-> Checks for token uniqueness across multiple requests.

-> Validates SameSite cookie attributes for security (using Selenium).

-> Determines if a site is vulnerable or safe based on CSRF and cookie evaluations.

## Requirements
To run this project, you need the following Python libraries:
```
requests
beautifulsoup4
selenium
webdriver-manager
```
Install them using:
```
pip install -r requirements.txt
```

## Usage
Clone this repository:
```
git clone https://github.com/mdashik123456/CSRF-Detection-System.git
cd csrf-detection-system
```
Ensure all dependencies are installed:
```
pip install -r requirements.txt
```
Run the script:
``` python main.py ```
Enter the URL of the website to analyze when prompted.


```
.
├── main.py               # Main script to run the CSRF detection
├── requirements.txt      # Dependencies required for the project
└── README.md             # Project documentation
```

## How It Works
Form Extraction: The script fetches and parses the HTML of the target webpage to extract all forms.

CSRF Token Detection: Identifies potential CSRF tokens in the forms by searching for input fields with names containing "csrf".

Token Validation: Verifies that the tokens are at least 32 characters long.

Token Uniqueness Check: Sends multiple requests to the same webpage to check if the CSRF token changes between requests.

Cookie Security Validation: Uses Selenium to check for SameSite attributes in cookies.

Security Evaluation: Based on the findings, the script determines if the site is safe or vulnerable.

## Example of Output
```
Enter the URL of the website to check: https://example.com
Site is safe.
```

## Dependencies

Requests: For making HTTP requests to the target website.

BeautifulSoup4: For parsing HTML and extracting forms and tokens.

Selenium: For simulating browser interactions to extract cookie attributes.

WebDriver Manager: For managing the Selenium WebDriver binaries.

## Notes

Ensure you have the Chrome browser installed, as the script uses the Chrome WebDriver.

Adjust the script if necessary for compatibility with other browsers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.


