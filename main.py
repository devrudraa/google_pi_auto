# importing modules
from time import sleep
from selenium import webdriver # To open browser
from selenium.webdriver.chrome.options import Options # For some internal uses
from selenium.webdriver.common.by import By # For targetting the elements of webpage
from selenium.webdriver.common.keys import Keys # For pressing some keys on the web

# I made some variable and it has some values which are keys from the module
KEYS = {
    '0': Keys.NUMPAD0,
    '1': Keys.NUMPAD1,
    '2': Keys.NUMPAD2,
    '3': Keys.NUMPAD3,
    '4': Keys.NUMPAD4,
    '5': Keys.NUMPAD5,
    '6': Keys.NUMPAD6,
    '7': Keys.NUMPAD7,
    '8': Keys.NUMPAD8,
    '9': Keys.NUMPAD9,
    '.': Keys.DECIMAL
}

#  Contructor for options
_option = Options()

# This will not let the window close even after the work is done
_option.add_experimental_option("detach", True)

# Giving the options to the chrome window
_driver = webdriver.Chrome(options=_option)

# URL of the webpage
_driver.get("https://www.google.com/search?q=value+of+pi&oq=value+of+pi")

# This will open the window in full screen mode
_driver.fullscreen_window()
# This will wait 10sec before accessing any element 
# Just in case if it is not loaded fully
_driver.implicitly_wait(10)

# Clicking the Start Game Button
start_Btn = _driver.find_element(By.CLASS_NAME, "t6VgP")
start_Btn.click()


# Targetting some element of the webpage to make it work
stage = _driver.find_element(By.CSS_SELECTOR, "span[jsname='CGmiC']")
pi_value = _driver.find_element(By.CSS_SELECTOR, "span[jsname='VssY5c']")
pi_inp = _driver.find_element(By.CSS_SELECTOR, "div[jsname='jhotKb']")

# This will keep checking for the updated value
# You can make it to run for a specefic number of times also
while True:
    sleep(1)

    # I am keeping track of when the site is done showing all the digits as it says 1/5 like this 
    # If you have visited the site you knwo what am I talking about
    if 'Hi-Score' not in stage.text:
        
        # It splits the score  list from 1/2 to 1 and 2
        score_list = stage.text.split('/')

        # It checks if the both number is equal it means it is done showing all the digits and now it is our turn to re enter the digits
        if score_list[0].strip() == score_list[1].strip():

            # It stores all the digits which we have to type
            target_text = pi_value.text
            # It loops over all the digits 
            for pi_nums in str(target_text):
                # and sends key strokes according to the stored number 
                pi_inp.send_keys(KEYS[str(pi_nums)])

'''
    And there you go you have a bot which plays a simple PI game for you
    so it will keep going untill google stops sending more responce

    You can make more changes in it, it is just a simple bot which I made just to have some fun with it 
    and it was fun so hope you learned someting mew today (MAYBE) if you have any suggestions please let me know 
'''


