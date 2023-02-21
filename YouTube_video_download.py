#import pytube library to download the video
import pytube

#Ask for the URl of the video
url = input("Enter the URL : ")

#Specify the storage path of video
path ="E:"

#video downloading code
pytube.YouTube(url).streams.get_highest_resolution().download(path)