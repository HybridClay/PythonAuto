import webbrowser

# getting the path
# chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"

# Chrome browser path to my profile:    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 1"

#This works too
#chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --profile-directory=Profile 1"

chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --profile-directory='Profile 1'"

# First registers the new browser
webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser(chrome_path))

Google = 'https://www.google.com/'
#webbrowser.get('chrome').open(Google)
webbrowser.open(Google)

RingCentral = 'https://app.ringcentral.com/login'
webbrowser.open_new_tab(RingCentral)

textfree = 'https://messages.textfree.us/login'
webbrowser.open_new_tab(textfree)

ADP = 'https://www.adp.com/'
webbrowser.open_new_tab(ADP)

