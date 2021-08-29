import os
import sys
import subprocess

"""
Arguments:
            1.The youtube playlist link
            2.The video format 
"""

ytbLink = sys.argv[1]
#videoFormat = sys.argv[2]
"""
exLink ='https://www.youtube.com/playlist?list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o'

result = subprocess.run(['youtube-dl', '-F', exLink], stdout=subprocess.PIPE)

terminalresult = str(result.stdout)

z = terminalresult.split("[youtube]")

ytbShortLink=[]
for i in range(1,len(z)):
    nn = str(z[i]).split(":")[0].replace(" ", "")
    ytbShortLink.append(nn)

for n in range(len(ytbShortLink)):
    ytbShortLink[n] = 'https://www.youtube.com/watch?v='+ytbShortLink[n]

    subprocess.run(['youtube-dl', '-f','22',ytbShortLink[n]], stdout=subprocess.PIPE)


"""




def downloadPlaylistVideo(url):
    #youtube-dl --max-filesize 50M <playlist_url>
    print("download Video only from playlist")
    subprocess.run(['youtube-dl', '--max-filesize','50M',url], stdout=subprocess.PIPE)    

def downloadPlaylistAudio(url):
    #youtube-dl --yes-playlist --extract-audio <playlist_url>
    print("download audio only from playlist")
    subprocess.run(['youtube-dl', '--yes-playlist','--extract-audio',url], stdout=subprocess.PIPE)    

def downloadAudio(url):
    #youtube-dl -x https://www.youtube.com/watch?v=7E-cwdnsiow
    
    print("downloading Audio")
    subprocess.run(['youtube-dl',"-o", "/home/mercy/Music/%(title)s.%(ext)s", '-x',url], stdout=subprocess.PIPE)  


def downloadVideo(url):
    #youtube-dl -f 22 https://www.youtube.com/watch?v=7E-cwdnsiow
    print("downloading Video")
    subprocess.run(['youtube-dl',"-o", "/home/mercy/Videos/%(title)s.%(ext)s", '--max-filesize','50M',url], stdout=subprocess.PIPE)  



def ChooseType():
    response=[1,2]
    try:
        decision = int(input("entrez \"1\" pour Video OU \"2\" pour AUDIO : "))
        assert decision in response
        return decision
    except Exception as e:
        ChooseType()






if 'youtube.com/playlist' in ytbLink:
    print("c'est un playlist\n")
    isPlaylist=True
else:
    print("c'est une video\n")
    isPlaylist=False

decision = ChooseType()



if decision==1 :
    if isPlaylist:
        downloadPlaylistVideo(ytbLink)
    elif not isPlaylist:
        downloadVideo(ytbLink)
if decision==2:
    if isPlaylist:
        downloadPlaylistAudio(ytbLink)
    elif not isPlaylist:
        downloadAudio(ytbLink)

print("Download Finished")