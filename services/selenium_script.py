from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from selenium_cookie import load_cookies, save_cookies

EMAIL = ""
PASSWORD = ""


def setup_driver():
    """
    Sets up and returns the Chrome WebDriver.
    """
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def click_user_menu(driver):
    """
    Clicks on the user menu button to open the user menu.
    """
    try:
        # Wait until the user menu button is clickable and then click it
        user_menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.tv-header__user-menu-button--anonymous"))
        )
        user_menu_button.click()
    except Exception as e:
        print(f"Error clicking user menu button: {e}")


def click_sign_in_button(driver):
    """
    Clicks on the "Sign in" button within the opened user menu.
    """
    try:
        # Wait until the "Sign in" button is clickable and then click it
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-name='header-user-menu-sign-in']"))
        )
        sign_in_button.click()
    except Exception as e:
        print(f"Error clicking sign in button: {e}")


def click_email_button(driver):
    """
    Clicks on the email button on the login page.

    :param driver: The Selenium WebDriver.
    """
    try:
        # Wait until the email button is clickable and then click it
        email_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "Email"))
        )
        email_button.click()
    except Exception as e:
        print(f"Error clicking email button: {e}")


def get_account_type():
    """
    Prompts the user for their account type and returns it.
    """
    account_type = input(
        "Do you have a Google account or a User/Password account? Enter 'Google' or 'User/Password': ").strip()
    while account_type.lower() not in ['google', 'user/password']:
        print("Invalid input. Please enter 'Google' or 'User/Password'.")
        account_type = input(
            "Do you have a Google account or a User/Password account? Enter 'Google' or 'User/Password': ").strip()
    return account_type


def perform_user_password_login(driver):
    """
    Navigates to the login page and performs login using User/Password.

    :param driver: The Selenium WebDriver.
    """
    click_user_menu(driver)
    click_sign_in_button(driver)
    click_email_button(driver)

    email = EMAIL
    password = PASSWORD

    try:
        # Wait for the email input to be clickable
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "id_username"))
        )

        # Clear the input field and type the email address
        email_input.clear()
        email_input.send_keys(email)

        # Wait for the password input to be clickable
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "id_password"))
        )

        # Clear the input field and type the password
        password_input.clear()
        password_input.send_keys(password)

        # Find and click the sign in button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.submitButton-LQwxK8Bm"))
        )
        sign_in_button.click()

        # Add a wait time to observe actions or wait for the next page
        time.sleep(15)

    except Exception as e:
        print(f"Error during User/Password login: {e}")


def add_symbols(driver, symbols):
    """
    Clicks on the add symbol button and inputs a list of symbols.

    :param driver: The Selenium WebDriver.
    :param symbols: A list of symbols to add.
    """
    try:
        # Find and click the add symbol button
        add_symbol_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'div[data-name="add-symbol-button"]'))
        )
        add_symbol_button.click()
        print("Add symbol button clicked.")

        # Wait for the search input to appear and be clickable
        search_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[data-role="search"]'))
        )

        for symbol in symbols:
            # Clear the search input, enter the symbol, and press Enter
            search_input.clear()
            search_input.send_keys(symbol)
            search_input.send_keys(Keys.RETURN)
            print(f"Symbol {symbol} entered.")
            # Wait for the result to be processed before adding the next symbol
            time.sleep(1)

        print("All symbols have been added.")

    except Exception as e:
        print(f"Error adding symbols: {e}")


def main():
    driver = setup_driver()
    # Navigate to the webpage where you intend to use the cookies
    driver.get("https://www.tradingview.com/")
    # Wait for the site to fully load before loading cookies
    driver.implicitly_wait(10)  # wait for a maximum of 10 seconds
    # Load cookies from the file if they exist
    load_cookies(driver)
    # Refresh the page to make sure cookies are applied
    driver.refresh()
    time.sleep(5)
    # Define the list of symbols to add
    STOCKS = ["QQQ", "BTC", "SPY", "NVDA", "AAPL",
              "TSLA", "AMZN", "GOOGL", "MSFT", "AMD"]
    # Perform the action to add symbols
    add_symbols(driver, STOCKS)
    driver.quit()


if __name__ == "__main__":
    main()
