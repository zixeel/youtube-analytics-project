from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

api_key: str = os.getenv('API_you_tube_key')


class Video:
    def __init__(self,video_id: str) -> None:
        self.video_id = video_id
        video_response = self.get_service().videos().list(part='snippet,statistics,'
                                                               'contentDetails,topicDetails',
                                                          id=video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/watch?v={video_id}"
        self.like_count = video_response['items'][0]['statistics']['likeCount']
        self.view_count = video_response['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls) -> build:
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def __str__(self) -> str:
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self) -> str:
        return f'{self.title}'

