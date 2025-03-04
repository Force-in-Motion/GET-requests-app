from __future__ import annotations

import customtkinter as ctk
from config.config_password_page import *


class PasswordPageFrame(ctk.CTkFrame):
    def __init__(self, parent_page: PasswordPage, *args, **kwargs):
        """
        Создает фрейм главной страницы, включая виджеты, расположенные на ней
        :param main_page: главная страница
        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        """
        super().__init__(*args, **kwargs)
        self.__parent_page = parent_page
        self.__input = None
        self.__result_label = None
        self.__config_main_label()
        self.__config_input()
        self.__config_btn()


    def __config_main_label(self) -> None:
        """
        Создает лейблы страницы, их параметры и стили
        :return: None
        """
        self.__main_label = ctk.CTkLabel(self, text=ml_t, font=ml_f)
        self.__main_label.place(relx=0.14, rely=0.1)

        self.__result_label = ctk.CTkLabel(self, text=rl_t, font=rl_f, width=rl_wh, height=rl_ht, justify=rl_jf)
        self.__result_label.place(rely=0.7)


    def __config_input(self) -> None:
        self.__input = ctk.CTkEntry(self, width=i_wh, height=i_ht, font=i_f)
        self.__input.place(relx=0.18, rely=0.25)


    def __config_btn(self) -> None:
        self.__btn = ctk.CTkButton(self, width=b_wh, height=b_ht, corner_radius=b_cr, fg_color=b_fgc, text_color=b_tc,
                                   hover_color=b_hc, font=b_f, text=b_t)
        self.__btn.place(relx=0.28, rely=0.45)




class PasswordPage(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        # self.__parent_page = parent_page
        self.__config_window()
        self.__config_frame()


    def __config_window(self):
        self.geometry(geometry)
        self.title(title)
        self.resizable(rzb_wh, rzb_ht)


    def __config_frame(self):
        self.__frame = PasswordPageFrame(self, master=self, width=pf_wh, height=pf_ht)
        self.__frame.pack()
        self.__frame.pack_propagate(prop)


    # def on_cancel_click(self) -> None:
    #     """
    #     Обрабатывает клик по кнопке возврата на предыдущую страницу
    #     """
    #     self.__parent_page.deiconify()
    #
    #     self.destroy()


    @classmethod
    def run(cls) -> None:
        """
        Запускает главное окно приложения
        """
        page = cls()
        page.lift()
        page.attributes('-topmost', True)
        page.mainloop()


main = PasswordPage.run()