from OtherModules.site_security_checker import SiteSecurityChecker
from OtherModules.link_extractor import LinkExtractor
from OtherModules.test_working_links import TestWorkingLinks

if __name__ == "__main__":
    isLinkWork = TestWorkingLinks()
    url = input("Enter the URL of the website to check: ")
    extractor = LinkExtractor(url)
    links = extractor.get_links()
    if links:
        for link in links:
            print("\n<----------------------New Scan--------------------------->")
            print(f"Scanning: {link}")
            if isLinkWork.is_link_working(link):
                checker = SiteSecurityChecker(link)
                result = checker.check_site_security()
                print(result)
            else:
                print("404 Site Not found")
            print("<------------------------------------------------------------>\n")
    else:
        print("No links found or an error occurred.")
    