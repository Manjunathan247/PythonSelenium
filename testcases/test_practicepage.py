
from helpers.BaseTest import Base_Test
from helpers.Read_Json_Helper import data_read
from pageobjects.HomePage import Home_Page


class Test_PracticePage(Base_Test):

    def test_homepage(self):
        homepage = Home_Page(self.driver)
        homepage.radio_button(data_read('radiobutton_value'))
        homepage.suggestion_dropdown(data_read('suggestion_dropdown_value'))
        homepage.static_dropdown(data_read('static_dropdown_value'))
        homepage.check_box(data_read('check_box_values')[0])
        homepage.check_box(data_read('check_box_values')[1])
        homepage.alert_handle_accept(data_read('username'))
        homepage.alert_handle_cancel(data_read('username'))
        homepage.openwindow_action(data_read('openwindow_action_title'))
        homepage.open_tab(data_read('open_tab_title'))
        homepage.table_handle(data_read('course_name'))
        homepage.elementdisplayed(data_read('username'))
        homepage.mousehover_action()
        homepage.frame_handle()

