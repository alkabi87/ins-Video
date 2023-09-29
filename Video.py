import pytube
print('Download video from python')
url = input ('Enter video url : ')
pytube.YouTube(url).streams.get_highest_resolution( ).download('Desktop')
