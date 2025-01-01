from OtherModules.form_extractor import FormExtractor
from OtherModules.token_validator import TokenValidator
from OtherModules.cookie_validator import CookieValidator

class SiteSecurityChecker:
    def __init__(self, url):
        self.url = url
        self.form_extractor = FormExtractor()
        self.token_validator = TokenValidator()
        self.cookie_validator = CookieValidator()

    def check_site_security(self):
        """Check the security of a site based on CSRF and cookies."""
        forms = self.form_extractor.get_forms(self.url)
        if not forms:
            return "Site is vulnerable: No forms found."

        tokens = self.form_extractor.extract_csrf_tokens(forms)
        if not any(tokens[key] for key in tokens):
            return "Site is vulnerable: No CSRF tokens found in forms."
        print(tokens)

        valid, invalid_form = self.token_validator.are_all_tokens_valid(tokens)
        if not valid:
            return f"Site is vulnerable: One or more CSRF tokens are too short in {invalid_form}."

        # Send a second request to check token reusability
        forms = self.form_extractor.get_forms(self.url)
        new_tokens = self.form_extractor.extract_csrf_tokens(forms)
        
        if self.token_validator.are_tokens_unique(tokens, new_tokens):
            return "Site is vulnerable: CSRF tokens are reused."

        # Check cookie security with Selenium
        if not self.cookie_validator.check_samesite_cookies_with_selenium(self.url):
            return "Site is vulnerable: Cookies do not have SameSite attribute set."

        return "Site is safe."
