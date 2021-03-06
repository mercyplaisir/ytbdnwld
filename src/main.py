import os
import sys
import subprocess
import datetime

"""
Arguments:
            1.The youtube playlist link
            2.The video format 
"""


mainDirectory = '/home/mercy'
musicDestination = f'{mainDirectory}/Music'
videoDestination = f'{mainDirectory}/Videos'



ytbLink = sys.argv[1]

def createDailyFolder(folderDestination):
    dateToday = str(datetime.datetime.now()).split(" ")[0]

    if dateToday not in os.listdir(folderDestination):
        newFolder = f'{folderDestination}/{dateToday}'
        os.mkdir(newFolder)
        print("created a folder ",newFolder)
        return newFolder
    elif dateToday in os.listdir(folderDestination):
        return f'{folderDestination}/{dateToday}'

def CreatePlaylistFolder(folderDestination):
    
    idPlaylist = [int(i.split('playlist')[1]) for i in os.listdir(folderDestination) if 'playlist' in i]
    idPlaylist.sort()
    if len(idPlaylist)>0:
        nextId = idPlaylist[len(idPlaylist)-1]+1
        newPlaylistFolder = f'{folderDestination}/playlist{nextId}'
        os.mkdir(newPlaylistFolder)
        print(">>>Created a folder ",newPlaylistFolder)
        return newPlaylistFolder
    else:
        os.mkdir(f'{folderDestination}/playlist1')

        print(f'created  a folder {folderDestination}/playlist1')
        return f'{folderDestination}/playlist1'
    print(2)
#=================================================================================================


def downloadPlaylistVideo(url,destinationFolder = videoDestination):
    #youtube-dl --max-filesize 50M <playlist_url>
    print("download Video only from playlist")
    newDailyFolder=createDailyFolder(destinationFolder)
    playlistFolder = CreatePlaylistFolder(newDailyFolder)

    os.system(f"youtube-dl --yes-playlist --format mp4 -o '{playlistFolder}/%(title)s.%(ext)s' '{url}'") #--max-filesize 50MiB    

def downloadPlaylistAudio(url,destinationFolder = musicDestination):
    #youtube-dl --yes-playlist --extract-audio <playlist_url>

    newDailyFolder=createDailyFolder(destinationFolder)#create a today Folder
    playlistFolder = CreatePlaylistFolder(newDailyFolder)#create a playlist Folder
    print(f"Stored to {playlistFolder} ")

    print("download audio only from playlist")
    os.system(f'youtube-dl --yes-playlist -o "{playlistFolder}/%(title)s.%(ext)s" --extract-audio "{url}"')

def downloadAudio(url,destinationFolder = musicDestination):
    #youtube-dl -x https://www.youtube.com/watch?v=7E-cwdnsiow
    folderDestination = createDailyFolder(destinationFolder)#create a folder of today's date
    print(f"downloading Audio\n Stored to {folderDestination}")


    os.system(f'youtube-dl -x --audio-format m4a -o \"{folderDestination}/%(title)s.%(ext)s\" "{url}"')


def downloadVideo(url,destinationFolder = videoDestination):
    #youtube-dl -f 22 https://www.youtube.com/watch?v=7E-cwdnsiow
    folderDestination = createDailyFolder(destinationFolder)#create a folder of today's date
    print(f"downloading Video \n Stored to {folderDestination}")
    os.system(f'youtube-dl --format mp4 -o \"{folderDestination}/%(title)s.%(ext)s\" "{url}"')#--max-filesize 50M



def ChooseType():
    response=[1,2]
    try:
        decision = int(input("entrez \"1\" pour Video OU \"2\" pour AUDIO : "))
        assert decision in response
        return decision
    except Exception as e:
        ChooseType()



#main




if 'youtube.com/playlist' in ytbLink:
    print("c'est un playlist\n")
    isPlaylist=True
else:
    print("c'est une video\n")
    isPlaylist=False




decision = ChooseType()


try:
    if decision==1 :#video
        if isPlaylist:
            downloadPlaylistVideo(ytbLink)
        elif not isPlaylist:
            downloadVideo(ytbLink)
    if decision==2:#audio
        if isPlaylist:
            downloadPlaylistAudio(ytbLink)
        elif not isPlaylist:
            downloadAudio(ytbLink)

    print("Download Finished")
except Exception as e:
    print(e)
