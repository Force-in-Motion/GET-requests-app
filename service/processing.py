import sys


class Processing:

    @staticmethod
    def on_exit_click() -> None:
        """
        Закрывает главное окно приложения
        :return:
        """
        sys.exit()