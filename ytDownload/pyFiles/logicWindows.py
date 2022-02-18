from os import link
import PySimpleGUI as sg

from trace import *
from windows import *
from myFunctions import *
from youtube import *



def MainLogic():
    g_path =  ''                    #store the path
    g_youtube_filter = {}           #dictionary

    win_main, win_openFolder, win_openFile = MainWindow(), None, None
    while True:
        window, events, values = sg.read_all_windows()
        #progress_bar = win_main.find_element('progress_bar')          #drawWindows.py
        #window[key].Update(value)

        # ----------------------------------------------------
        # ===========     MAIN File WINDOW    ================
        # ----------------------------------------------------
        #options events
        #events_and_values = Check_Events_and_Values(events, values)
        #print(events_and_values)
        if window == win_main:
            g_youtube_filter = Check_Events_and_Values(events, values)
            Log('\nevents_and_values\n', g_youtube_filter)
            

        #---------------------#
        #--- type of link  ---#
        #---------------------#
        #   if 'Link_Type' == '-PODCAST-' or 'Link_Type' == '-SONG-' or 'Link_Type' == '-AUDIOBOOK-':
        #       Video_Quality = Min
        #       Video_Output  = Defv
        #       Video_WideScr = Off
        #       GreyedOut()     
        #---------------------#
        

        #---------------------#
        #-- checkbox check ---#
        #---------------------#
        #   if '-ONLY_AUDIO-' == Enabled:
        #       Video_Quality = Min
        #       Video_Output  = Defv
        #       Video_WideScr = Off
        #       GreyedOut()
        #
        #   
        #   if 'SPLIT_TOO' == Enabled:
        #       SplitAudio()
        #---------------------#


        #------------
        # CLOSE event
        if window == win_main and events == sg.WIN_CLOSED:
            Log(None, "Linha 27 - if window == win_mainWindow and events == sg.WIN_CLOSED: ")
            break
        

        #------------
        # START event
        if window == win_main and events == 'START':
            Log(None, "Linha 32 - if window == win_mainWindow and events == 'START': ")    
            if g_youtube_filter['link'] is not "":    
                win_openFolder = OpenFolder()
                win_main.hide()

        # ----------------------------------------------------



        # ----------------------------------------------------
        # ===========     OPEN Folder WINDOW    ==============
        # ----------------------------------------------------
        #------------
        # close event
        if window == win_openFolder and events == sg.WINDOW_CLOSED:
            Log(None, "Linha 51 - if window == win_openFolder and events == sg.WINDOW_CLOSED: ")
            win_main.un_hide()
            win_openFolder.close()

        #-------------
        # cancel event
        if window == win_openFolder and events == 'Cancel':
            Log(None,"Linha 58 - if window == win_openFolder and events == 'Cancel': ")
            win_main.un_hide()
            win_openFolder.close()

        #---------
        # ok event
        if window == win_openFolder and events == 'OK':
            Log(None, "Linha 65 - if window == win_openFolder and events == 'OK': ")
            #fullData = values['_FILES_'].split(';')
            g_path = values['_FILES_']
            g_path = str(g_path)

            Log('Path ', g_path)           
            win_openFolder.close()
            win_main.un_hide()



        #-------------------------------------------------------------#
        #------------ IF EVERYTHING IS IN PLACE...   -----------------#
        if g_youtube_filter['link'] is not "" and g_path is not "":

          #-------------------------------------------#
          #===== INVOKE THE YOUTUBE A.P.I ============#
            YouTubeDownload(g_path, g_youtube_filter)
          #___________________________________________#

        #-------------------------------------------------------------#