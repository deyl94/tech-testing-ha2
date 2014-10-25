# coding=utf-8
import os
import random
import string
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.auth_page import AuthPage
from tests.pages.create_page import CreatePage
from tests.pages.campaign_page import ControlCampaignPage


class SelectionOptionsTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.USERNAME = 'tech-testing-ha2-27@bk.ru'
        self.PASSWORD = os.environ['TTHA2PASSWORD']
        self.DOMAIN = '@bk.ru'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def tearDown(self):
        self.driver.quit()

    def test_right_user(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        self.assertEqual(self.USERNAME, create_page.portal_headline.get_email())

    def test_set_product_and_pad(self):
        CAMPAIGN_NAME = u'Ололошники'

        create_page = CreatePage(self.driver)
        create_page.open()

        base_settings = create_page.base_setting
        base_settings.set_campaign_name(CAMPAIGN_NAME)
        base_settings.set_product_type()
        base_settings.set_setting_pad()

    def test_input_banner_form(self):
        BANNER_TITLE = u'ololo'
        BANNER_TEXT = u'Грильяж и куртизанки!'
        BANNER_URL = u'http://my.mail.ru/v/42'
        BANNER_IMG = u'/home/roland/tech-tests/tech-testing-ha2/tests/resourses/img/img.jpg'
        create_page = CreatePage(self.driver)
        create_page.open()

        banner_form = create_page.banner_form
        banner_form.set_banner_title(BANNER_TITLE)
        banner_form.set_banner_text(BANNER_TEXT)
        banner_form.set_banner_url(BANNER_URL)
        banner_form.set_banner_image(BANNER_IMG)
        banner_form.banner_save()

        self.assertEqual(BANNER_TITLE, banner_form.preview_banner_title())
        self.assertEqual(BANNER_TEXT, banner_form.preview_banner_text())

    def test_set_of_sex_default(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        sex = create_page.sex
        self.assertEqual(u'Мужчины и женщины', sex.get_sex())

    def test_sex_set_men(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        sex = create_page.sex
        sex.click_on_sex()
        sex.click_on_women()
        self.assertEqual(u'Мужчины', sex.get_sex())

    def test_sex_none(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        sex = create_page.sex
        sex.click_on_sex()
        sex.click_on_women()
        sex.click_on_men()
        self.assertEqual(u'Мужчины', sex.get_sex())

    def test_region_north_america(self):
        NORTH_AMERICA = u'Северная Америка'

        create_page = CreatePage(self.driver)
        create_page.open()

        region = create_page.region
        region.click_checkbox(region.RUSSIA)
        region.click_checkbox(region.NORTH_AMERICA)

        self.assertEqual(NORTH_AMERICA, region.get_selected_region())

    def test_max_tree_region(self):
        NUMBER_AMERICA = u'(15 из 17)'
        NUMBER_CANADA = u'(11 из 12)'
        NUMBER_USA = u'(50 из 51)'

        create_page = CreatePage(self.driver)
        create_page.open()

        region = create_page.region
        region.click_checkbox(region.RUSSIA)
        region.click_checkbox(region.NORTH_AMERICA)
        region.click_dropdown(region.NORTH_AMERICA_DROPDOWN)
        region.click_dropdown(region.CANADA_DROPDOWN)
        region.click_dropdown(region.USA_DROPDOWN)
        region.click_checkbox(region.UKON)
        region.click_checkbox(region.ALASKA)

        self.assertEqual(NUMBER_USA, region.get_number_of_regions(region.NUMBER_USA))
        self.assertEqual(NUMBER_CANADA, region.get_number_of_regions(region.NUMBER_CANADA))
        self.assertEqual(NUMBER_AMERICA, region.get_number_of_regions(region.NUMBER_AMERICA))

    pass


class SaveTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.USERNAME = 'tech-testing-ha2-27@bk.ru'
        self.PASSWORD = os.environ['TTHA2PASSWORD']
        self.DOMAIN = '@bk.ru'

        self.BANNER_TITLE = u'ololo'
        self.BANNER_TEXT = u'Грильяж и куртизанки!'
        self.BANNER_URL = u'http://my.mail.ru/v/42'
        self.CAMPAIGN_NAME = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        self.BANNER_IMG = u'/home/roland/tech-tests/tech-testing-ha2/tests/resourses/img/img.jpg'

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def tearDown(self):
        campaign_page = ControlCampaignPage(self.driver)
        campaign_page.open()
        campaign_page.control_banner.click_on_delete()
        campaign_page.control_campaign.click_on_delete()

        self.driver.quit()

    def test_if_banner_ok(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        region = create_page.region
        region.click_checkbox(region.RUSSIA)
        region.click_checkbox(region.NORTH_AMERICA)

        base_settings = create_page.base_setting
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)
        base_settings.set_product_type()
        base_settings.set_setting_pad()

        banner_form = create_page.banner_form
        banner_form.set_banner_title(self.BANNER_TITLE)
        banner_form.set_banner_text(self.BANNER_TEXT)
        banner_form.set_banner_url(self.BANNER_URL)
        banner_form.set_banner_image(self.BANNER_IMG)
        banner_form.banner_save()

        create_page.save.click_save_button()

        campaign_page = ControlCampaignPage(self.driver)
        campaign_page.open()

        control_campaign = campaign_page.control_campaign

        self.assertEqual(unicode(self.CAMPAIGN_NAME), control_campaign.get_campaign_name())

        banner_control = campaign_page.control_banner
        banner_control.click_on_edit()

        self.assertEqual(self.BANNER_URL, banner_control.get_url())
        self.assertEqual(self.BANNER_TEXT, banner_control.get_text())
        self.assertEqual(self.BANNER_TITLE, banner_control.get_title())

    def test_if_right_selections_full(self):
        PAD = u'Мой Мир: веб-версия'
        SEX = u'Мужчины и женщины'
        REGION = u'Северная Америка'

        create_page = CreatePage(self.driver)
        create_page.open()

        region = create_page.region
        region.click_checkbox(region.RUSSIA)
        region.click_checkbox(region.NORTH_AMERICA)

        base_settings = create_page.base_setting
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)
        base_settings.set_product_type()
        base_settings.set_setting_pad()

        banner_form = create_page.banner_form
        banner_form.set_banner_title(self.BANNER_TITLE)
        banner_form.set_banner_text(self.BANNER_TEXT)
        banner_form.set_banner_url(self.BANNER_URL)
        banner_form.set_banner_image(self.BANNER_IMG)
        banner_form.banner_save()

        create_page.save.click_save_button()

        campaign_page = ControlCampaignPage(self.driver)
        campaign_page.open()

        control_campaign = campaign_page.control_campaign

        control_campaign.click_on_edit()
        self.assertEqual(PAD, base_settings.get_control_pad())
        self.assertEqual(SEX, create_page.sex.get_sex())
        self.assertEqual(REGION, region.get_selected_region())
        self.assertEqual(self.CAMPAIGN_NAME, base_settings.get_campaign_name())

    def test_if_right_selections_some(self):
        PAD = u'Мой Мир: веб-версия'
        SEX = u'Мужчины'
        NUMBER_AMERICA = u'(15 из 17)'
        NUMBER_CANADA = u'(11 из 12)'
        NUMBER_USA = u'(50 из 51)'

        create_page = CreatePage(self.driver)
        create_page.open()

        region = create_page.region
        region.click_checkbox(region.RUSSIA)
        region.click_checkbox(region.NORTH_AMERICA)
        region.click_dropdown(region.NORTH_AMERICA_DROPDOWN)
        region.click_dropdown(region.CANADA_DROPDOWN)
        region.click_dropdown(region.USA_DROPDOWN)
        region.click_checkbox(region.UKON)
        region.click_checkbox(region.ALASKA)

        base_settings = create_page.base_setting
        base_settings.set_campaign_name(self.CAMPAIGN_NAME)
        base_settings.set_product_type()
        base_settings.set_setting_pad()

        banner_form = create_page.banner_form
        banner_form.set_banner_title(self.BANNER_TITLE)
        banner_form.set_banner_text(self.BANNER_TEXT)
        banner_form.set_banner_url(self.BANNER_URL)
        banner_form.set_banner_image(self.BANNER_IMG)
        banner_form.banner_save()

        sex = create_page.sex
        sex.click_on_sex()
        sex.click_on_women()

        create_page.save.click_save_button()

        campaign_page = ControlCampaignPage(self.driver)
        campaign_page.open()

        control_campaign = campaign_page.control_campaign

        control_campaign.click_on_edit()
        self.assertEqual(PAD, base_settings.get_control_pad())
        self.assertEqual(SEX, create_page.sex.get_sex())
        self.assertEqual(self.CAMPAIGN_NAME, base_settings.get_campaign_name())
        self.assertEqual(NUMBER_AMERICA, region.get_number_of_regions(region.NUMBER_AMERICA))
        self.assertEqual(NUMBER_CANADA, region.get_number_of_regions(region.NUMBER_CANADA))
        self.assertEqual(NUMBER_USA, region.get_number_of_regions(region.NUMBER_USA))

    pass
