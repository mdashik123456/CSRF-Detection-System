from OtherModules.site_security_checker import SiteSecurityChecker

if __name__ == "__main__":
    url = input("Enter the URL of the website to check: ")
    checker = SiteSecurityChecker(url)
    result = checker.check_site_security()
    print(result)