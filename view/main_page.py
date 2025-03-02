from __future__ import annotations

import customtkinter as ctk
from config.config import *


class MainFrame(ctk.CTkFrame):
    def __init__(self, main_page: MainPage, *args, **kwargs):
        """
        Создает фрейм главной страницы, включая виджеты, расположенные на ней
        :param main_page: главная страница
        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        """
        super().__init__(*args, **kwargs)
        self.__main_page = main_page
        self.__main_label = None
        self.__config_labels()
        self.__config_btn()


    def __config_labels(self) -> None:
        """
        Создает главный лейбл страницы, его параметры и стили
        :return: None
        """
        self.__main_label = ctk.CTkLabel(self, text=mlt, font=mlf)
        self.__main_label.place(relx=0.15, rely=0.1)


    def __config_btn(self) -> None:
        """
        Создает кнопки страницы, их параметры и стили
        :return: None
        """
        self.__password_btn = ctk.CTkButton(self, width=btn_wh, height=btn_ht, corner_radius=btn_cr, fg_color=btn_fgc,
                                            text_color=btn_tc, text=pwb_t, hover_color=btn_hc, font=btn_f)
        self.__password_btn.place(relx=0.19, rely=0.25)
        self.__password_btn.configure()

        self.__gravity_btn = ctk.CTkButton(self, width=btn_wh, height=btn_ht, corner_radius=btn_cr, fg_color=btn_fgc,
                                            text_color=btn_tc, text=gv_t, hover_color=btn_hc, font=btn_f)
        self.__gravity_btn.place(relx=0.19, rely=0.4)
        self.__gravity_btn.configure()

        self.__fines_btn = ctk.CTkButton(self, width=btn_wh, height=btn_ht, corner_radius=btn_cr, fg_color=btn_fgc,
                                            text_color=btn_tc, text=fin_t, hover_color=btn_hc, font=btn_f)
        self.__fines_btn.place(relx=0.19, rely=0.55)
        self.__fines_btn.configure()

        self.__currency_translation_btn = ctk.CTkButton(self, width=btn_wh, height=btn_ht, corner_radius=btn_cr, fg_color=btn_fgc,
                                            text_color=btn_tc, text=curt_t, hover_color=btn_hc, font=btn_f)
        self.__currency_translation_btn.place(relx=0.19, rely=0.7)
        self.__currency_translation_btn.configure()


        self.__exit_btn = ctk.CTkButton(self, width=ex_wh, height=ex_ht, corner_radius=ex_cr, fg_color=ex_fgc,
                                            text_color=ex_tc, text=ex_t, hover_color=ex_hc, font=ex_f)
        self.__exit_btn.place(relx=0.3, rely=0.84)
        self.__exit_btn.configure(command=self.__main_page.on_exit_click())


class MainPage(ctk.CTk):
    def __init__(self):
        """
        Создает главную страницу приложения, ее параметры и стили, а так же формирует главный фрейм страницы
        """
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_exit_click)
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

    def on_exit_click(self) -> None:
        """
        Закрывает главное окно приложения
        :return:
        """
        self.destroy()

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