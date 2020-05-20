import logging

from helpers.BaseTest import Base_Test, getLogger


class Window_Helper(Base_Test):
    def __init__(self, driver):
        self.driver = driver

    log = getLogger(logging.INFO)

    def get_alert(self):
        return self.driver.switch_to.alert

    def get_alert_message(self):
        return self.get_alert().text

    def switch_windows(self, window_id):
        self.driver.switch_to.window(window_id)

    def switchto_parent(self):
        parent_window = self.driver.window_handles[0]
        self.switch_windows(parent_window)
        self.log.info("Now control back to parent browser")
        parentwindow_title = self.driver.title
        self.log.info("Title of the parent page is: " + parentwindow_title)
        assert parentwindow_title == 'Practice Page'

    def switchto_child(self, window_title):
        childwindow = self.driver.window_handles[1]
        self.switch_windows(childwindow)
        self.log.info("Now control in child browser")
        childwindow_title = self.driver.title
        self.log.info("Title of the child page is: " + childwindow_title)
        assert childwindow_title == window_title
        self.driver.close()
        self.log.info("Child browser is closed")
        self.switchto_parent()

    def switch_frame(self, frame_index):
        self.driver.switch_to.frame(frame_index)

    def switch_defaultframe(self):
        return self.driver.switch_to.default_content()