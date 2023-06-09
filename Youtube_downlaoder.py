# Importing the libraries
from pytube import YouTube

# Defining download_video() function
def download_video(url, resolution):
    try:
        yt = YouTube(url)
        videos = yt.streams.filter(progressive=True, file_extension='mp4')
        filtered_videos = [video for video in videos if resolution.lower() in str(video.resolution).lower()]
        
        if filtered_videos:
            video = filtered_videos[0]
            print(f"Downloading '{yt.title}'...(Resolution: {video.resolution})")
            video.download()
            print("Download completed!!")
        else:
            print(f"Video with resolution {resolution} not found!")
    
    except Exception as e:
        print("Error: ", e)


# Prompt the user to enter the video url and quality
video_url = input("Enter the YouTube video url: ")
video_resolution = input("Enter the video resolution (e.g. 720p, 480p, 360p, 240p, 144p): ")

# Calling the download_video() function
download_video(video_url, video_resolution)