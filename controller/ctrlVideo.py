from model.video import Video


class CtrlVideo:
    """

    """

    def __init__(self, url):
        """

        :param url:
        """
        self.url = url


    def descargaMp3(self):
        """

        :return:
        """
        video = Video(self.url)
        status = video.download()
        return status

