from __future__ import annotations

import customtkinter as ctk
from config.config_main_page import *
from service.processing import Processing as pg

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent_page: MainPage, *args, **kwargs):
        """
        Создает фрейм главной страницы, включая виджеты, расположенные на ней
        :param main_page: главная страница
        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        """
        super().__init__(*args, **kwargs)
        self.__parent_page = parent_page
        self.__config_labels()
        self.__config_btn()
        self.__config_combobox()


    def __config_labels(self) -> None:
        """
        Создает главный лейбл страницы, его параметры и стили
        :return: None
        """
        self.__main_label = ctk.CTkLabel(self, text=mlt, font=mlf)
        self.__main_label.place(relx=0.11, rely=0.1)


    def __config_combobox(self):
        self.__combobox = ctk.CTkComboBox(self, width=cb_wh, height=cb_ht, values=val, font=cb_f, justify=cb_jf, dropdown_font=cb_f)
        self.__combobox.place(relx=0.125, rely=0.25)



    def __config_btn(self) -> None:
        """
        Создает кнопки страницы, их параметры и стили
        :return: None
        """
        self.__confirm_btn = ctk.CTkButton(self, width=cf_wh, height=cf_ht, corner_radius=cf_cr, fg_color=cf_fgc,
                                            text_color=cf_tc, text=cf_t, hover_color=cf_hc, font=cf_f)
        self.__confirm_btn.place(relx=0.725, rely=0.25)
        self.__confirm_btn.configure()

        self.__exit_btn = ctk.CTkButton(self, width=ex_wh, height=ex_ht, corner_radius=ex_cr, fg_color=ex_fgc,
                                            text_color=ex_tc, text=ex_t, hover_color=ex_hc, font=ex_f)
        self.__exit_btn.place(relx=0.2, rely=0.75)
        self.__exit_btn.configure(command=pg.on_exit_click)



class MainPage(ctk.CTk):
    def __init__(self):
        """
        Создает главную страницу приложения, ее параметры и стили, а так же формирует главный фрейм страницы
        """
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", pg.on_exit_click)
        self.__config_window()
        self.__config_frame()

    def __config_frame(self) -> None:
        """
        Создает фрейм страницы, его параметры и стили
        :return: None
        """
        self.__main_frame = MainFrame(self, master=self, width=mf_wh, height=mf_ht)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(prop)


    def __config_window(self) -> None:
        """
        Определяет параметры и стили главной страницы приложения
        :return: None
        """
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    @classmethod
    def run(cls) -> None:
        """
        Запускает главное окно приложения
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()


main = MainPage.run()