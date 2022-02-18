import os
from posixpath import split
import PySimpleGUI as sg

from trace import Log
from logicWindows import *


#============================================================#
#=================== Get Path and Files =====================#
def GetPathFiles(data):
    Log(None, "GetPathFiles():")

    # descobrindo a quantidade de elementos da lista
    number_of_files = len(data)
    Log("Nubmer>", number_of_files)

    # Definindo o tamanhno da lista e removendo o primeiro valor da lista (que é o proprio tamanho dela)
    list_of_files = [number_of_files]
    del list_of_files[0]

    # pegando o primeiro elemento ai do vetor de dados
    # procurando, a partir do final da ultima string, a primeira '/'.
    # Ou seja, assim tenho o 'path'
    path = data[0]
    path = path[:path.rfind('/')]
    path = path + '/'
    Log("Path>", path)

    # percorrento a lista
    for file in data:
        # indice da 'barra' + o proximo caracter, até o final da string (:)
        file = file[file.rfind('/')+1:]
        list_of_files.append(str(file))
        Log("List of Files", list_of_files)

    Log("Path:",               path)
    Log("Files:",   number_of_files)
    Log("Files:",     list_of_files)

    return str(path), int(number_of_files), list(list_of_files)
#============================================================#








#============================================================#
#======================    Get Path     =====================#
def GetPath(data):
    Log(None, "GetPath():")

    return str(data)
#============================================================#





#=============================================================#
#======================    Get Values    =====================#
#-- INPUT LINK--#
#---------------#
def Check_Link(events, values):
    if values['-LINK-'] is not None:
        link = str(values['-LINK-'])
        Log('link', link)
        return link
    else:
        link = '        '
        Log('link', link)
        return link

#---------------#


#-- TYPE LINK --#
#---------------#
def Check_Link_Type(events, values):
    if values['-PLAYLIST-'] == True:
        linkType = '-PLAYLIST-'
        Log('linkType', linkType)
        return str(linkType)

    elif values['-PODCAST-'] == True:
        linkType = '-PODCAST-'
        Log('linkType', linkType)
        return str(linkType)

    elif values['-AUDIOBOOK-'] == True:
        linkType = '-AUDIOBOOK-'
        Log('linkType', linkType)
        return str(linkType)

    elif values['-SONG-'] == True:
        linkType = '-SONG-'
        Log('linkType', linkType)
        return str(linkType)

    elif values['-VIDEO-'] == True:
        linkType = '-VIDEO-'
        Log('linkType', linkType)
        return str(linkType)
#---------------#


#-- VIDEO QUALITY --#
#-------------------#
def Check_Video_Quality(events, values):
    if values['-VMAX-'] == True:
        video_quality = '-VMAX-'
        Log('video_quality', video_quality)
        return video_quality

    elif values['-VMIN-'] == True:
        video_quality = '-VMIN-'
        Log('video_quality', video_quality)
        return video_quality
    
    elif values['-4K-'] == True:
        video_quality = '4k'
        Log('video_quality', video_quality)
        return video_quality

    elif values['-1080p-'] == True:
        video_quality = '1080p'
        Log('video_quality', video_quality)
        return video_quality

    elif values['-720p-'] == True:
        video_quality = '720p'
        Log('video_quality', video_quality)
        return video_quality
    
    elif values['-480p-'] == True:
        video_quality = '480p'
        Log('video_quality', video_quality)
        return video_quality
    
    elif values['-360p-'] == True:
        video_quality = '360p'
        Log('video_quality', video_quality)
        return video_quality
    
    elif values['-240p-'] == True:
        video_quality = '240p'
        Log('video_quality', video_quality)
        return video_quality
    
    elif values['-144p-'] == True:
        video_quality = '144p'
        Log('video_quality', video_quality)
        return video_quality
#---------------#



#-- AUDIO OUTPUT --#
#------------------#
def Check_Audio_Output(events, values):
    if values['-DEFA-'] == True:
        audio_output = '-DEFA-'
        Log('audio_output', audio_output)
        return audio_output
    
    elif values['-MP3-'] == True:
        audio_output = 'mp3'
        Log('audio_output', audio_output)
        return audio_output
    
    elif values['-AAC-'] == True:
        audio_output = 'aac'
        Log('audio_output', audio_output)
        return audio_output
    
    elif values['-WAV-'] == True:
        audio_output = 'wav'
        Log('audio_output', audio_output)
        return audio_output
#------------------#


#-- VIDEO OUTPUT --#
#------------------#
def Check_Video_Output(events, values):
    if values['-DEFV-'] == True:
        video_output = '-DEFV-'
        Log('video_output', video_output)
        return video_output
    
    elif values['-MP4-'] == True:
        video_output = 'mp4'
        Log('video_output', video_output)
        return video_output
    
    elif values['-MKV-'] == True:
        video_output = 'mkv'
        Log('video_output', video_output)
        return video_output
    
    elif values['-AVI-'] == True:
        video_output = 'avi'
        Log('video_output', video_output)
        return video_output


#-- Check Only Audio --#
#----------------------#
def Check_Only_Audio(events, values):
    if values['-ONLY_AUDIO-'] is True:
        only_audio = 'True'
        Log('only_audio', only_audio)
        return only_audio
    else:
        only_audio = 'False'
        Log('only_audio', only_audio)
        return only_audio


#-- Check Split Audio --#
#-----------------------#
def Check_Split_Too(events, values):
    if values['-SPLIT_TOO-'] is True:
        split_too = 'True'
        Log('split_too', split_too)
        return split_too
    else:
        split_too = 'False'
        Log('split_too', split_too)
        return split_too


#-- Check WideScreen  --#
#-----------------------#
def Check_Force_WideScreen(events, values):
    if values['-WIDESCREEN-'] is True:
        force_wideScreen = 'True'
        Log('force_wideScreen', force_wideScreen)
        return force_wideScreen
    else:
        force_wideScreen = 'False'
        Log('force_wideScreen', force_wideScreen)
        return force_wideScreen
#=============================================================#





#============================================================#
#================ Check_Events_and_Values ===================#
def Check_Events_and_Values(events, values):
    Log(None, "Check_Events_and_Values():")


    _choosed_link               = str(Check_Link(events, values))
    _choosed_linkType           = str(Check_Link_Type(events, values))
    _choosed_video_quality      = str(Check_Video_Quality(events, values))
    _choosed_audio_output       = str(Check_Audio_Output(events, values))
    _choosed_video_output       = str(Check_Video_Output(events, values))
    _choosed_only_audio         = str(Check_Only_Audio(events, values))
    _choosed_split_too          = str(Check_Split_Too(events, values))
    _choosed_force_wideScreen   = str(Check_Force_WideScreen(events, values))

    

    events_and_values = {
        'link'            :  _choosed_link, 
        'linkType'        :  _choosed_linkType,
        'videoQuality'    :  _choosed_video_quality,
        'audioOutput'     :  _choosed_audio_output,
        'videoOutput'     :  _choosed_video_output,
        'onlyAudio'       :  _choosed_only_audio,
        'splitAudioToo'   :  _choosed_split_too,
        'forceWideScreen' :  _choosed_force_wideScreen
    }
    

    return events_and_values
#============================================================#
