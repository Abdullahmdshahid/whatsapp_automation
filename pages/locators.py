from selenium.webdriver.common.by import By


class IndexLocator():
    #SEARCH BOX TEST CASE 1

    SEARCH_FIELD = (By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')

    #MASSAGE BOX TEST CASE 2

    MESSAGE_FIELD = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')


    #MENU BUTTON TEST CASE 5

    MENU = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    LOGOUT = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]')
