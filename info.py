from pytube import YouTube 


def video_Info(yt):
    print("Title : ",yt.title)
    print("Total Length : ",yt.length," Seconds")
    print("Total Views : ",yt.views)
    print("Is Age Restricted : ",yt.age_restricted)
    print("Thumbnail Url : ",yt.thumbnail_url)
    print('Streams:',yt.streams.filter(progressive=True, file_extension='mp4'))

def vidDownload(yt):
    print('Fetching Streams...')
    yt = yt.streams.get_highest_resolution()
    print(yt)
    print("\n\nDownloading...")
    try:
       
        yt.download()
    except:
        print("An error has occurred")
    print("Downloaded successfully")
    
link = input("Enter the link : ")
yt = YouTube(link)

choice = input('Select: \n1. Video Info \n2. Video Download\n')
if choice == '1':
    video_Info(yt)
elif choice == '2':
    vidDownload(yt)