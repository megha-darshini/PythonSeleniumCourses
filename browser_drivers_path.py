from selenium import webdriver
#xattr -d com.apple.quarantine <name-of-executable>

#option1(selenium 3)
#driver = webdriver.Chrome(executable_path='/Users/mneelaka/PycharmProjects/chromedriver')
driver = webdriver.Chrome()
driver.get("https://google.com")