from pytubefix import Playlist
from pytubefix.cli import on_progress


class Lista:
    """

    """

    def __init__(self, url, title):
        """

        :param url:
        """
        self.title = title
        self.url = url

    def downloadAll(self):
        """

        :return:
        """
        try:
            pl = Playlist(self.url)

            for video in pl.videos:
                ys = video.streams.get_audio_only()
                ys.download(output_path=f"downloads/{self.title}", mp3=True)
            return "Playlist descargada correctamente"

        except:
            return "URL no valida"
