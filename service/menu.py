
class HandlerMenu:
    """
    Класс работающий с меню кнопок главной страницы и открывающий другие окна при нажатии на кнопки
    """
    def __init__(self):
        self.__password_page = None
        self.__del_user = None
        self.__statistic = None


    def open_password_page(self, parent_page) -> None:
        """
        Открывает окно запроса случайного пароля с сервера
        :param parent_page: принимает окно, являющееся родительским для открываемого окна
        :return: None
        """
        from view.password_page import PasswordPage

        self.__password_page = PasswordPage(parent_page)


    # def open_del_user_page(self, main_page) -> None:
    #     """
    #     Открывает окно удаления пользователя
    #     :param main_page: Принимает окно, являющееся родительским для открываемого окна
    #     :return: None
    #     """
    #     from src.view.del_user import DelUser
    #
    #     self.__del_user = DelUser(main_page)
    #
    #
    # def open_edit_common_areas(self, main_page) -> None:
    #     """
    #     Открывает окно редактирования списка общедоступных зон
    #     :param main_page: Принимает окно, являющееся родительским для открываемого окна
    #     :return: None
    #     """
    #     from src.view.edit_common_areas import EditCommonAreas
    #
    #     self.__del_user = EditCommonAreas(main_page)
    #
    #
    # def open_statistic_page(self, main_page) -> None:
    #     """
    #     Открывает окно статистики и выводит на него информацию из файла и из временной памяти
    #     :param main_page: Принимает окно, являющееся родительским для открываемого окна
    #     :return: None
    #     """
    #     from src.view.statistic import Statistic
    #
    #     self.__statistic = Statistic(main_page)
    #
    #     data = ds.get_log()
    #
    #     value = Processing.converts_data_to_str(data)
    #
    #     self.__statistic.scroll.set_label_text(value)
