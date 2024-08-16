from model.lista import Lista


class CtrlPlayList:
    """

    """

    def __init__(self, url, title):
        """

        :param url:
        """
        self.title = title
        self.url = url


    def descargaMp3(self):
        """

        :return:
        """
        pl = Lista(self.url, self.title)
        status = pl.downloadAll()
        return status
