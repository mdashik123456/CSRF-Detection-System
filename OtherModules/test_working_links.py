import requests

class TestWorkingLinks:
    def is_link_working(self, link):
        """Checks if a link is working by sending a HEAD request."""
        try:
            response = requests.head(link, timeout=5)
            if response.status_code < 400:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False