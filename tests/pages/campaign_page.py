from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.page import Page, Component


class ControlCampaignPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def control_campaign(self):
        return ControlCampaign(self.driver)

    @property
    def control_banner(self):
        return ControlBanner(self.driver)

    pass


class ControlCampaign(Component):
    EDIT = '.control__link_edit'
    DELETE = '.control_campaign > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1)'
    CAMPAIGN_NAME = '.campaign-title__name'

    def wait_until_visible_then_click(self, element):
        element = WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.visibility_of(element))
        element.click()

    def click_on_edit(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.EDIT)
        )
        self.wait_until_visible_then_click(element)

    def click_on_delete(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.DELETE)
        )
        self.wait_until_visible_then_click(element)

    def get_campaign_name(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        return element.text

    pass


class ControlBanner(Component):
    EDIT = '.control__preset_edit'
    DELETE = '.control_banner > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1)'
    TITLE = 'div.banner-form:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > input:nth-child(2)'
    TEXT = 'div.banner-form:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > textarea:nth-child(2)'
    URL = 'div.banner-form:nth-child(3) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(2) > input:nth-child(1)'

    def click_on_edit(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.EDIT)
        )
        element.click()

    def click_on_delete(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.DELETE)
        )
        element.click()

    def get_title(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.TITLE)
        )
        return element.get_attribute('value')

    def get_text(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.TEXT)
        )
        return element.get_attribute('value')

    def get_url(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.URL)
        )
        return element.get_attribute('value')

    pass