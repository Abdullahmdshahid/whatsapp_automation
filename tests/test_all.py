import time
from selenium.webdriver.common.keys import Keys
from tests.base_test import BaseTestClass
from pages.index import Index
from pages.sample import SampleData


class Test(BaseTestClass):

    def test_tc_001(self):
        a = self.log()
        index = Index(self.chrome_webdriver)
        index.search_contact().send_keys(SampleData.NUMBER, Keys.ENTER)
        a.info("Display searched contact")
        time.sleep(5)

    def test_tc_002(self):
        a = self.log()
        index = Index(self.chrome_webdriver)
        index.search_contact().send_keys(SampleData.NUMBER, Keys.ENTER)
        index.sent_message().send_keys(SampleData.DEMO_TEXT, Keys.ENTER)
        a.info("Successfully send message")
        time.sleep(5)

    def test_tc_003(self):
        a = self.log()
        index = Index(self.chrome_webdriver)
        index.search_contact().send_keys(SampleData.NUMBER, Keys.ENTER)

        index.sent_message().send_keys(SampleData.DEMO_TEXT, Keys.ENTER)

        last_sent = self.chrome_webdriver.find_elements_by_xpath('//span[@data-testid="msg-dblcheck"]')
        last_sent_reverse = last_sent[-1]
        last_sent_aria_label_value = last_sent_reverse.get_attribute('aria-label')

        if last_sent_aria_label_value == ' Read ' or last_sent_aria_label_value == ' Delivered ':
            SampleData.sh1.cell(row=2, column=2, value='sent')
            SampleData.exl.save(SampleData.exl_save)
        a.info("Successfully write result on excel")
        time.sleep(5)

    def test_tc_004(self):
        a = self.log()

        last_seen = self.chrome_webdriver.find_elements_by_xpath('//span[@data-testid="msg-dblcheck"]')
        last_seen_reverse = last_seen[-1]
        aria_label_dblcheck = last_seen_reverse.get_attribute('aria-label')

        if aria_label_dblcheck == ' Read ':
            SampleData.sh1.cell(row=2, column=3, value='Seen')
            SampleData.exl.save(SampleData.exl_save)
        else:
            SampleData.sh1.cell(row=2, column=3, value='Not Seen')
            SampleData.exl.save(SampleData.exl_save)
        a.info('Successfully write message status on excel')
        time.sleep(5)

    def test_tc_005(self):
        a = self.log()
        index = Index(self.chrome_webdriver)
        index.menu_button().click()
        index.logout_button().click()
        a.info("Successfully logout from whatsapp")