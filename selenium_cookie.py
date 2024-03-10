import os
import pickle

def load_cookies(driver, location='cookies.pkl'):
    """
    Loads cookies from a file into the WebDriver to maintain the session.

    :param driver: The Selenium WebDriver.
    :param location: File location from where to load cookies.
    """
    if os.path.exists(location):
        try:
            with open(location, 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    # Check if the cookie 'domain' matches the current domain
                    if "domain" in cookie and "tradingview.com" in cookie["domain"]:
                        driver.add_cookie(cookie)
            print("Cookies loaded into WebDriver.")
        except EOFError:
            # Handle empty or corrupted file
            print("Cookie file is empty or corrupted. Deleting file.")
            os.remove(location)
        except Exception as e:
            # Handle any other exceptions
            print(f"Error loading cookies: {e}")

        
def save_cookies(driver, location='cookies.pkl'):
    """
    Saves the current session cookies to a file.
    
    :param driver: The Selenium WebDriver.
    :param location: File location to save cookies.
    """
    with open(location, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
    print("Cookies saved to file.")