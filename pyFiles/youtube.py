from myFunctions import *
from logicWindows import *

from pytube import YouTube
from pytube import Playlist
import os


def YouTubeDownload(path, yt_filt):
    Log("YouTubeDownload", None)
    g_files = []                    #save all files inside a path in a list
    g_maxFiles = 0                  #number of files saves inside folder (used to 'for g_files in path': do something)
    g_path = str(path)              #raw path (the place when the video/song will be stored)

    g_link = ''                     #youtube link
    g_typeOfLink = ''               #Playlist, Podcast, Audiobook, Song or Video
    g_qualityOfVideo = ''           #Max, Min, 4k, 1080p, 720p, 480p, 360p, 240p, 144p
    g_audioOutput = ''              #Default, MP3, AAC, WAV
    g_videoOutput = ''              #Default, MP4, MKV, AVI
    g_onlyAudio = ''                #Only_audio
    g_audioSplit = ''               #Also_split
    g_forceWideMode = ''            #Force_16_9



    #===============  DICTIONARY HELP ===================#     
    #'link'            :  _choosed_link, 
    #'linkType'        :  _choosed_linkType,
    #'videoQuality'    :  _choosed_video_quality,
    #'audioOutput'     :  _choosed_audio_output,
    #'videoOutput'     :  _choosed_video_output,
    #'onlyAudio'       :  _choosed_only_audio,
    #'splitAudioToo'   :  _choosed_split_too,
    #'forceWideScreen' :  _choosed_force_wideScreen
    #_____________________________________________________#

    g_link           = str(yt_filt['link'])                     #youtube link
    g_typeOfLink     = str(yt_filt['linkType'])                 #Playlist, Podcast, Audiobook, Song or Video
    g_qualityOfVideo = str(yt_filt['videoQuality'])             #Max, Min, 4k, 1080p, 720p, 480p, 360p, 240p, 144p
    g_audioOutput    = str(yt_filt['audioOutput'])              #Default, MP3, AAC, WAV
    g_videoOutput    = str(yt_filt['videoOutput'])              #Default, MP4, MKV, AVI
    g_onlyAudio      = str(yt_filt['onlyAudio'])                #Only_audio, Also_split
    g_audioSplit     = str(yt_filt['splitAudioToo'])            #Also_split
    g_forceWideMode  = str(yt_filt['forceWideScreen'])          #Force_16_9



    #------------------      O.N.L.Y  P.R.I.N.T     ---------------------#
    print('\n')
    print('*********************************************************')
    print('Path:                ',  g_path)
    print('Numer of Files:      ',  g_maxFiles)
    print('Files list:          ',  g_files)

    print('YouTube Link:        ',  g_link)  
    print('Type of Link:        ',  g_typeOfLink)
    print('QualityVideo:        ',  g_qualityOfVideo)
    print('g_audioOutput:       ',  g_audioOutput)
    print('g_videoOutput:       ',  g_videoOutput)
    print('g_onlyAudio:         ',  g_onlyAudio)
    print('g_audioSplit:        ',  g_audioSplit)
    print('g_forceWideScreen:   ',  g_forceWideMode)

    print('Global List:         ',  yt_filt)
    print("*********************************************************")
    print("\n")
    #--------------------------------------------------------------------#







    #=============================================================================#
    #==============    Y O U      T U B  E      D O W N L O A D E R    ===========#
    #=============================================================================#
    os.chdir(g_path)
    Log("Choosing the path", g_path)

    video = YouTube(str(g_link))
    video.streams.filter(adaptive=True)
    
    if g_typeOfLink == '-PLAYLIST-':
        Log("Playlist", None)
        p = Playlist(str(g_link))
        for video in p.videos:
            print(video.title)
            video.streams.get_highest_resolution().download()
    else:
        Log("Is not a playlist", g_typeOfLink)
        video = YouTube(str(g_link))
        print(video.title)
        #video.streams.get_highest_resolution().download()
        #video.streams.get_by_resolution('144').download()



    