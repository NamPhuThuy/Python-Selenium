from selenium import webdriver
import time
from random import randint

driver = webdriver.Chrome()

for i in range (12):

    # Open the form
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeP9y2uJk3wRj2ZCFm7DX9IkOKP6wqPpXf-E9AMzVirojWa7Q/viewform")
    time.sleep(1)

    # Fill the textField
    text = 'What ups'
    textField = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    textField.send_keys(text)

    # Tick the checkbox
    n = randint(1, 3)
    checkBoxField = driver.find_element('xpath', f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[{n}]')
    checkBoxField.click()
    time.sleep(1)

    #Dropdown Box
    dropDownBox = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    dropDownBox.click()
    time.sleep(1)
    n = randint(3, 5)
    dropDownBoxOption = driver.find_element('xpath', f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[{n}]')
    dropDownBoxOption.click()

    '''
    //*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]
    //*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[4]
    //*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[5]
    '''

    # time.sleep(2)

    submitButton = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submitButton.click()

    # ensure that the program terminates correctly
driver.close()

'''
def selection():
    n = randint(1,3)
    if n == 1:
        ans1 = driver.find_element("xpath",'//*[@id="i5"]/div[3]/div')
        ans1.click()
    elif n == 2:
        ans1 = driver.find_element("xpath",'//*[@id="i8"]/div[3]/div')
        ans1.click()
    else:
        ans1 = driver.find_element("xpath",'//*[@id="i11"]/div[3]/div')
        ans1.click()


def fill_form():
    # data = pd.read_csv('data.csv')
    for i in range(1000):
        print(i)
        time.sleep(0.5)

        selection()

        # name = data.iloc[i]['name']
        name = "something"
        inputName = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')

        inputName.send_keys(name)

        submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()

        back = driver.find_element("xpath",'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        back.click()

fill_form()
driver.close()
'''

# n
# 2 can(n): 2, 3,
#
# for ()
#
# if (n == 1) return 0
# return 1