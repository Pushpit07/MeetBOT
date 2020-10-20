from selenium import webdriver
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pause; import os; import re
import time; from datetime import datetime
import colorama; from termcolor import colored
from dotenv import load_dotenv

load_dotenv()
colorama.init()

###################################################################
#                        Meets                      Y   M  D  H  m  s
MEETS = {"1 http://meet.google.com/gqs-skwg-fjw": "2020 10 20 12 35 00",
         # "2 https://meet.google.com/meetURL2": "2020 12 31 23 59 59",
         # Add more Meet URLs (if any) using the same format as above
         }
DURATION = 60 # Duration of each Meet in minutes
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
BROWSER_DRIVER = os.getenv("BROWSER_DRIVER")

#                   Google Chrome
#           Linux: "ChromeDrivers/linux64/chromedriver"
#             Mac: "ChromeDrivers/mac64/chromedriver"
#         Windows: "ChromeDrivers/win32/chromedriver.exe"

###################################################################

# All required interactive elements' locators (text fields, buttons, etc.)
emailFieldPath = "identifierId"
emailNextButtonPath = "identifierNext"
passwordFieldPath = "password"
passwordNextButtonPath = "passwordNext"
joinButtonPath = "//span[contains(text(), 'Join')]"
endButtonPath = "[aria-label='Leave call']"               
                                                                                   
BANNER1 = colored('''
                     ██████   ██████                    █████    ███████████     ███████    ███████████
                    ░░██████ ██████                    ░░███    ░░███░░░░░███  ███░░░░░███ ░█░░░███░░░█
                     ░███░█████░███   ██████   ██████  ███████   ░███    ░███ ███     ░░███░   ░███  ░ 
                     ░███░░███ ░███  ███░░███ ███░░███░░░███░    ░██████████ ░███      ░███    ░███    
                     ░███ ░░░  ░███ ░███████ ░███████   ░███     ░███░░░░░███░███      ░███    ░███    
                     ░███      ░███ ░███░░░  ░███░░░    ░███ ███ ░███    ░███░░███     ███     ░███    
                     █████     █████░░██████ ░░██████   ░░█████  ███████████  ░░░███████░      █████   
                    ░░░░░     ░░░░░  ░░░░░░   ░░░░░░     ░░░░░  ░░░░░░░░░░░     ░░░░░░░       ░░░░░    
                                                                                   ''', 'yellow')
BANNER2 = colored('''                                         MeetBOT: The Google Meet Bot''', 'green', attrs=['blink'])
BANNER3 = colored('''                                        ---------------------------------''', 'green', attrs=['blink'])


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


def timeStamp():
    timeNow = str(datetime.now())
    timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeNow)
    return(timeRegEx[0])

def initBrowser():
    print("\nInitializing browser...", end="")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--window-size=800,800")
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                    "profile.default_content_setting_values.media_stream_camera": 2,
                                                    "profile.default_content_setting_values.notifications": 2
                                                    })
    driver = webdriver.Chrome(executable_path=BROWSER_DRIVER, options=chromeOptions)
    return driver


def login():
    print("Logging into Google account...", end="")
    driver.get('https://accounts.google.com/signin')

    emailField = wait.until(when.element_to_be_clickable((by.ID, emailFieldPath)))
    time.sleep(1)
    emailField.send_keys(EMAIL)

    emailNextButton = wait.until(when.element_to_be_clickable((by.ID, emailNextButtonPath)))
    emailNextButton.click()

    passwordField = wait.until(when.element_to_be_clickable((by.NAME, passwordFieldPath)))
    time.sleep(1)
    passwordField.send_keys(PASSWORD)

    passwordNextButton = wait.until(when.element_to_be_clickable((by.ID, passwordNextButtonPath)))
    passwordNextButton.click()
    time.sleep(3)
    print(colored(" Success!", "green"))


def attendMeet():
    print(f"\n\nNavigating to Google Meet #{meetIndex}...", end="")
    driver.get(URL[2:])
    print(colored(" Success!", "green"))
    print(f"Entering Google Meet #{meetIndex}...", end="")

    joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButtonPath)))
    time.sleep(1)
    action.send_keys(Keys.ESCAPE).perform()
    time.sleep(1)
    joinButton.click()

    print(colored(" Success!", "green"))
    time.sleep(1)
    print(colored(f"Now attending Google Meet #{meetIndex} @{timeStamp()}", "green"), end="")

    try:
        joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButtonPath)))   # For another prompt that pops up for Meets being recorded
        time.sleep(1)
        joinButton.click()
    except:
        pass


def endMeet():
    endButton = driver.find_element_by_css_selector(endButtonPath)
    endButton.click()
    print(colored(f"\nSuccessfully ended Google Meet #{meetIndex} @{timeStamp()}\n", "red"), end="")


def genericError():
    # clrscr()
    print(colored(" Failed!", "red"), end="")
    print("\n\nPossible fixes:\n")
    print("1 Make sure you have downloaded the latest version of MeetNinja from the GitHub page (every new iteration brings fixes and new capabilities)")
    print("2.1 Check your inputs and run MeetNinja again (make sure there are no leading zeros in the Meet start times)")
    print("2.2 And / Or make sure you have chosen the correct webdriver file respective of your web browser and operating system")
    print("3. Make sure the generated web browser is not \"Minimized\" while MeetNinja is working")
    print("4.1. Make sure the webdriver file is of the latest stable build (https://chromedriver.chromium.org/ or https://github.com/mozilla/geckodriver/releases)")
    print("4.2. And / Or make sure your chosen web browser is updated to the latest version")
    print("4.3. And / Or make sure the webdriver file is at least of the same version as your chosen web browser (or lower)")
    print("5. Make sure the small \"time.sleep()\" delays (in seconds) in the functions are comfortable for your internet speed")
    print("6. Make sure your internet connection is stable throughout the process")
    print("\nPress Enter to exit.")
    input()
    try:
        driver.quit()
    except:
        pass


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


def hibernate():
    print("\nHibernating in 10 seconds. Press Ctrl + C to abort.")
    time.sleep(13)
    _ = os.system('shutdown /h /f')


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:
        DURATION *= 60
        driver = initBrowser()
        wait = webdriver.support.ui.WebDriverWait(driver, 5)
        action = ActionChains(driver)
        for meetIndex, (URL, startTime) in enumerate(MEETS.items(), start=1):
            startTime = list(map(int, startTime.split()))
            if (meetIndex <= 1):
                print(colored(f"Waiting until first Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...", "yellow"), end="")
            else:
                print(colored(f"\n\nWaiting until next Meet start time [{startTime[-3]:02}:{startTime[-2]:02}:{startTime[-1]:02}]...", "yellow"), end="")
            pause.until(datetime(*startTime))
            print(colored(" Started!", "green"))
            if (meetIndex <= 1):
                login()
            attendMeet()
            time.sleep(DURATION)
            endMeet()
        print("\n\nAll Meets completed successfully.")
        # hibernate()
        # Uncomment above to hibernate after a 10 second countdown upon completion of all Meets (Ctrl + C to abort hibernation)
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()

    except KeyboardInterrupt:
        # clrscr()
        print("\n\nCTRL ^C\n\nAs you wish master\n")
        print("Press Enter to exit.")
        input()
        print("\nCleaning up and exiting...", end="")
        driver.quit()
    except:
        # print(e)
        # Uncomment above to display error traceback (use when reporting issues)
        genericError()
