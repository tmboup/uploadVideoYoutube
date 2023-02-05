from pytube import YouTube,Playlist

def download(lien) :
    if("playlist" in lien):
        print("C'est un plyalist !!")
        play = Playlist(lien)
        print(f"Downloading playlist: {play.title}")
        for video in play.videos:
            print(f"Downloading video : {video.title}")
            video.streams.first().download()
        print(f"Telechargement {play.title} reussi")                  
        

    elif("watch" in lien) :
        print("c'est un simple video")
        yt = YouTube(lien)
        yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
    else:
        print("Ceci n'est pas un lien de youtube")


lien = input("donnez le lien de telechargement : ")

download(lien)