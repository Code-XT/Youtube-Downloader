
from pytube import YouTube 


def video_Info(yt):
    print("Title : ",yt.title)
    print("Total Length : ",yt.length," Seconds")
    print("Total Views : ",yt.views)
    print("Is Age Restricted : ",yt.age_restricted)
    print("Thumbnail Url : ",yt.thumbnail_url)
    print('Stream Details :', yt.fmt_streams)
    
link = input("Enter the link : ")
yt = YouTube(link)


video_Info(yt)