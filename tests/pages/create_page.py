from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.page import Page, Component


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def portal_headline(self):
        return PortalHeadline(self.driver)

    @property
    def banner_form(self):
        return BannerForm(self.driver)

    @property
    def base_setting(self):
        return BaseSetting(self.driver)

    @property
    def sex(self):
        return Sex(self.driver)

    @property
    def region(self):
        return Region(self.driver)

    @property
    def save(self):
        return Save(self.driver)

    pass


class PortalHeadline(Component):
    EMAIL = '#PH_user-email'
    EXIT = '#PH_logoutLink'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 3).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )

    def get_exit(self):
        return WebDriverWait(self.driver, 30, 3).until(
            lambda d: d.find_element_by_css_selector(self.EXIT)
        )

    pass


class BannerForm(Component):
    BANNER_TITLE = 'li.banner-form__row:nth-child(2) > input:nth-child(2)'
    BANNER_TITLE_PREVIEW = '.banner-preview__title'
    BANNER_TEXT_AREA = 'textarea.banner-form__input'
    BANNER_TEXT_AREA_PREVIEW = '.banner-preview__text'
    BANNER_URL = 'li.banner-form__row:nth-child(4) > span:nth-child(2) > input:nth-child(1)'
    BANNER_URL_PREVIEW = ''
    BANNER_IMG = '.banner-form__img-file'
    BANNER_SAVE_IMG = '.banner-form__img-file'
    BANNER_PREVIEW_IMG = 'span.banner-preview__img'
    BANNER_SAVE = '.banner-form__save-button'

    def set_banner_title(self, title):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_TITLE)
        )
        element.clear()
        element.send_keys(title)

    def preview_banner_title(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_TITLE_PREVIEW)
        )
        return element.text

    def set_banner_text(self, text):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_TEXT_AREA)
        )
        element.clear()
        element.send_keys(text)

    def preview_banner_text(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_TEXT_AREA_PREVIEW)
        )
        return element.text

    def set_banner_url(self, url):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_URL)
        )
        element.send_keys(url)

    def set_banner_image(self, path):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_IMG)
        )
        element.send_keys(path)

    def wait_banner_image(self):
        WebDriverWait(self.driver, 30, 3).until(
            self.preview_image
        )

    def preview_image(self, el):
        if el.find_element_by_css_selector(self.BANNER_PREVIEW_IMG).value_of_css_property("display") == 'block':
            return el

    def wait_until_visible_then_click(self, element):
        element = WebDriverWait(self.driver, 30, 3).until(
            expected_conditions.visibility_of(element))
        element.click()

    def banner_save(self):
        self.wait_banner_image()

        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.BANNER_SAVE)
        )
        element.click()

    pass


class BaseSetting(Component):
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    PRODUCT_TYPE = '#product-type-5212'
    SETTING_PAD = 'div.base-setting__pads-item:nth-child(3) > label:nth-child(2)'
    CONTROL_PAD = '.base-setting__pads-item__label'

    def set_campaign_name(self, name):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        element.clear()
        element.send_keys(name)

    def get_campaign_name(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        return element.get_attribute('value')

    def set_product_type(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def set_setting_pad(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SETTING_PAD)
        )
        element.click()

    def get_control_pad(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.CONTROL_PAD)
        )
        return element.text

    pass


class Sex(Component):
    SEX = '.campaign-setting__wrapper_sex > span:nth-child(1)'
    SEX_MEN = '#sex-M'
    SEX_WOMEN = '#sex-F'

    def get_sex(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SEX)
        )
        return element.text

    def wait_until_visible_then_click(self, element):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            expected_conditions.visibility_of(element))
        element.click()

    def click_on_sex(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SEX)
        )
        element.click()
        # self.wait_until_visible_then_click(element)

    def click_on_men(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SEX_MEN)
        )
        self.wait_until_visible_then_click(element)

    def click_on_women(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SEX_WOMEN)
        )
        self.wait_until_visible_then_click(element)

    pass


class Region(Component):
    RUSSIA = '#view9650'
    NORTH_AMERICA = '#view9654'
    SELECTED = '.campaign-setting__chosen-box__item__name'
    CUBA = '#view16275'
    CANADA = '#view16273'
    NORTH_AMERICA_DROPDOWN = '#regions100005 > span:nth-child(1)'
    CANADA_DROPDOWN = '#regions242 > span:nth-child(1)'
    UKON = '#regions395 > label:nth-child(3)'
    USA_DROPDOWN = '#regions200 > span:nth-child(1)'
    ALASKA = '#regions294 > label:nth-child(3)'
    NUMBER_AMERICA = 'li.campaign-setting__chosen-box__item:nth-child(1) > span:nth-child(2)'
    NUMBER_CANADA = 'li.campaign-setting__chosen-box__item:nth-child(2) > span:nth-child(2)'
    NUMBER_USA = 'li.campaign-setting__chosen-box__item:nth-child(3) > span:nth-child(2)'

    def click_checkbox(self, checkbox):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(checkbox)
        )
        element.click()

    def click_dropdown(self, region):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(region)
        )
        element.click()

    def get_number_of_regions(self, region):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(region)
        )
        return element.text

    def get_selected_region(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SELECTED)
        )
        return element.text

    def get_children_regions_remain(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda d: d.find_element_by_css_selector(self.CHILDREN_REGIONS)
        )
        return element.text

    pass


class Save(Component):
    SAVE_BUTTON = '.main-button__label'

    def click_save_button(self):
        element = WebDriverWait(self.driver, 30, 3).until(
            lambda el: el.find_element_by_css_selector(self.SAVE_BUTTON)
        )
        element.click()
    pass