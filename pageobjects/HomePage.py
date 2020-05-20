import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from helpers.BaseTest import getLogger
from helpers.WindowHelper import Window_Helper


class Home_Page:
    radiobuttons = (By.XPATH, "//div[@id='radio-btn-example']/fieldset/label/input")
    autosuggestion = (By.CSS_SELECTOR, "#autocomplete")
    place = (By.XPATH, "//li[@class='ui-menu-item']")
    staticdropdownlist = (By.CSS_SELECTOR, "#dropdown-class-example")
    checkboxes = (By.XPATH, "//legend[contains(text(),'Checkbox')]/following-sibling::label /input")
    alert_textfield = (By.CSS_SELECTOR, "#name")
    alert_button = (By.CSS_SELECTOR, "#alertbtn")
    alert_confirm_button = (By.CSS_SELECTOR, "#confirmbtn")
    window_button = (By.CSS_SELECTOR, "#openwindow")
    tab_button = (By.CSS_SELECTOR, "#opentab")
    courses = (By.XPATH, "//table[@id='product']/tbody/tr/following-sibling::tr /td[2]")
    elementdisplayed_textfield = (By.CSS_SELECTOR, "#displayed-text")
    hide_button = (By.CSS_SELECTOR, "#hide-textbox")
    show_button = (By.CSS_SELECTOR, "#show-textbox")
    mouse_hover = (By.CSS_SELECTOR, "#mousehover")
    mouse_hover_values = (By.XPATH, "//div[@class='mouse-hover-content']/a")
    iframes = (By.TAG_NAME, "iframe")
    urls = (By.TAG_NAME, "a")

    log = getLogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def radio_button(self, radio_value):
        radiobuttons = self.driver.find_elements(*self.radiobuttons)
        for radiobutton in radiobuttons:
            if radiobutton.get_attribute("value") == radio_value:
                radiobutton.click()
                assert radiobutton.is_selected()
                self.log.info("Clicked on " + radio_value + " button")

    def suggestion_dropdown(self, auto_dropdown_value):
        autosuggestion = self.driver.find_element(*self.autosuggestion)
        autosuggestion.send_keys(auto_dropdown_value)
        place = self.driver.find_element(*self.place)
        place_value = place.text
        if auto_dropdown_value in place_value:
            place.click()
        self.log.info("Selected " + auto_dropdown_value + " from suggestion drop down")
        script = "return document.getElementById('autocomplete').value"
        actual_value = self.driver.execute_script(script)
        expected_value = "Indonesia"
        self.log.info("Value selected from auto suggestion box is:" + actual_value)
        assert actual_value == expected_value

    def static_dropdown(self, dropdown_value):
        staticdropdownlist = self.driver.find_element(*self.staticdropdownlist)
        staticdropdownlist.click()
        options = staticdropdownlist.find_elements_by_tag_name("option")
        for option in options:
            if option.get_attribute("value") == dropdown_value:
                option.click()
        self.log.info("Selected " + dropdown_value + " from static drop down")
        script = "return document.getElementById('dropdown-class-example').value"
        selected_value = self.driver.execute_script(script)
        self.log.info("Value selected from static drop down is :" + selected_value)
        assert selected_value == dropdown_value

    def check_box(self, checkbox_value):
        checkboxes = self.driver.find_elements(*self.checkboxes)
        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == checkbox_value:
                checkbox.click()
                assert checkbox.is_selected()
        self.log.info("Selected " + checkbox_value + " from checkbox example")

    def alert_handle_accept(self, name_value):
        alert_text_field = self.driver.find_element(*self.alert_textfield)
        alert_text_field.send_keys(name_value)
        alert_button = self.driver.find_element(*self.alert_button)
        alert_button.click()
        wh = Window_Helper(self.driver)
        alert_message = wh.get_alert_message()
        assert name_value in alert_message
        self.log.info("Alert message is having " + name_value)
        wh.get_alert().accept()
        self.log.info("Clicked on accept button")

    def alert_handle_cancel(self, name_value):
        alert_text_field = self.driver.find_element(*self.alert_textfield)
        alert_text_field.send_keys(name_value)
        confirm_button = self.driver.find_element(*self.alert_confirm_button)
        confirm_button.click()
        wh = Window_Helper(self.driver)
        alert_message = wh.get_alert_message()
        assert name_value in alert_message
        self.log.info("Alert message is having " + name_value)
        wh.get_alert().dismiss()
        self.log.info("Clicked on dismiss button")

    def openwindow_action(self, open_window_child_name):
        window_button = self.driver.find_element(*self.window_button)
        window_button.click()
        wh = Window_Helper(self.driver)
        self.log.info("Clicked on Open window button")
        wh.switchto_child(open_window_child_name)

    def open_tab(self, tab_child_name):
        tab_button = self.driver.find_element(*self.tab_button)
        tab_button.click()
        wh = Window_Helper(self.driver)
        self.log.info("Clicked on Open tab button")
        wh.switchto_child(tab_child_name)

    def table_handle(self, text_in_course):
        courses = self.driver.find_elements(*self.courses)
        i = 0
        self.log.info("course names having Selenium as substring: ")
        for course in courses:
            course_name = course.text
            if text_in_course.lower() in course_name.lower():
                i += 1
                self.log.info(course_name)
        self.log.info("Number of courses having Selenium as substring is: " + str(i))

    def elementdisplayed(self, name_display):
        element_displayed = self.driver.find_element(*self.elementdisplayed_textfield)
        element_displayed.send_keys(name_display)
        self.log.info("Clicked on hide button")
        self.driver.find_element(*self.hide_button).click()
        assert not element_displayed.is_displayed()
        self.log.info("Text box is not displayed")
        self.driver.find_element(*self.show_button).click()
        self.log.info("Clicked on show button")
        assert element_displayed.is_displayed()
        self.log.info("Text box is displayed")
        script = "return document.getElementById('displayed-text').value"
        valueintextbox = self.driver.execute_script(script)
        assert valueintextbox == name_display

    def mousehover_action(self):
        # self.mouse_hover.location_once_scrolled_into_view
        actions = ActionChains(self.driver)
        mouse_hover_element = self.driver.find_element(*self.mouse_hover)
        actions.move_to_element(mouse_hover_element).perform()
        self.log.info("Mouse on Mousehover button")
        self.log.info("Options displayed when mouserhover on button:")
        values = self.driver.find_elements(*self.mouse_hover_values)
        for value in values:
            option = value.text
            self.log.info(option)

    def frame_handle(self):
        frames = self.driver.find_elements(*self.iframes)
        no_of_iframes = len(frames)
        self.log.info("Number of iframes in page: " + str(no_of_iframes))
        for frame in range(no_of_iframes):
            wh = Window_Helper(self.driver)
            wh.switch_defaultframe()
            wh.switch_frame(frame)
            self.log.info("control switching into iframe")
            urls_element = self.driver.find_elements(*self.urls)
            no_of_urls = len(urls_element)
            self.log.info("Number of urls in frame: " + str(no_of_urls))
            self.log.info("List of urls in frame: ")
            for url in urls_element:
                urltext = url.get_attribute("href")
                if urltext is not None:
                    self.log.info(str(urltext))
            wh.switch_defaultframe()
            self.log.info("Control back to main page")
