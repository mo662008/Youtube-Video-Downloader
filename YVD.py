from pytube import YouTube

# Take input link from user
link = input("Please enter video url: ")

# Create object
video = YouTube(link)

# Choose vid Quality res
print("""Please choose video resolution: 
        [1] 144p
        [2] 240p
        [3] 360p
        [4] 480p
        [5] 720p
        [6] 1080p""")

x = input()
try:
    x = int(x)
except:
    print("Only accept digits")

if x == 1:
    if video.streams.get_lowest_resolution():
        video.streams.get_lowest_resolution().download(output_path="c:/")
elif x == 2:
    if video.streams.filter(res="240", progressive=True):
        video.streams.filter(res="240", progressive=True).download(output_path="c:/")
elif x == 3:
    if video.streams.filter(res="360", progressive=True):
        video.streams.filter(res="360", progressive=True).download(output_path="c:/")
elif x == 4:
    if video.streams.filter(res="480", progressive=True):
        video.streams.filter(res="480", progressive=True).download(output_path="c:/")
elif x == 5:
    if video.streams.filter(res="720", progressive=True):
        video.streams.filter(res="720", progressive=True).download(output_path="c:/")
elif x == 6:
    if video.streams.filter(res="1080", progressive=True):
        video.streams.filter(res="1080", progressive=True).download(output_path="c:/")

# Display msg when downloading is done
def finish():
    print("Your video is ready!")

video.register_on_complete_callback(finish())
