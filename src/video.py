video_id = 'gaoc9MPZ4bw'
video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
# printj(video_response)
video_title: str = video_response['items'][0]['snippet']['title']
view_count: int = video_response['items'][0]['statistics']['viewCount']
like_count: int = video_response['items'][0]['statistics']['likeCount']
comment_count: int = video_response['items'][0]['statistics']['commentCount']