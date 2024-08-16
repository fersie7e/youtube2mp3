from pytubefix import YouTube
from pytubefix.cli import on_progress


class Video:
    """

    """

    def __init__(self, url):
        """

        :param url:
        """
        self.url = url

    def download(self):
        """

        :return:
        """
        try:
            yt = YouTube(self.url, on_progress_callback=on_progress)
            print(yt.title)

            ys = yt.streams.get_audio_only()
            ys.download(output_path='downloads/', mp3=True)

            return f"Descarga correcta- {yt.title}"
        except:
            return "URL no valida"
