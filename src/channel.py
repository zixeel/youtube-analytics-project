import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_you_tube_key')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.ch_name = channel['items'][0]['snippet']['title']
        self.ch_describe = channel['items'][0]['snippet']['description']
        self.ch_url = f"https://www.youtube.com/{channel['items'][0]['snippet']['customUrl']}"
        self.ch_followers = channel['items'][0]['statistics']['subscriberCount']
        self.ch_vids_amount = channel['items'][0]['statistics']['videoCount']
        self.ch_vives_amount = channel['items'][0]['statistics']['viewCount']



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        dict_ch = {
            'ch_name': self.ch_name,
            'ch_describe': self.ch_describe,
            'ch_url': self.ch_url,
            'ch_followers': self.ch_followers,
            'ch_vids_amount':self.ch_vids_amount,
            'ch_vives_amount':self.ch_vives_amount}

        with open(file_name, 'w', encoding='UTF-8',) as f:
            json.dump(dict_ch, f, ensure_ascii=False, indent=2)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def __str__(self):
        return f"{self.ch_name}({self.ch_url})"

    def __add__(self, other):
        return int(self.ch_followers) + int(other.ch_followers)

    def __sub__(self, other):
        return int(self.ch_followers) - int(other.ch_followers)

    def __eq__(self, other):
        return self.ch_followers == other.ch_followers

    def __lt__(self, other):
        return self.ch_followers < other.ch_followers

    def __gt__(self, other):
        return self.ch_followers > other.ch_followers

    def __le__(self, other):
        return self.ch_followers <= other.ch_followers

    def __ge__(self, other):
        return self.ch_followers >= other.ch_followers


