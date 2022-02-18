import PySimpleGUI as sg
from trace import Log


#============================================================#
#=======================  Open Files  =======================#
def OpenFiles():
    Log(None,"OpenFiles():")

    ###Choosing the theme###
    sg.theme('DarkAmber')

    ##Building the layout###
    openFiles_layout = [
        [sg.Input(key='_FILES_'), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]
    ]

    ###Building the window###
    window_openFiles = sg.Window('Select all files', layout=openFiles_layout, finalize=True)
    return window_openFiles
#============================================================#



#============================================================#
#=======================  Open Folder  ======================#
def OpenFolder():
    Log(None,"OpenFiles():")

    ###Choosing the theme###
    sg.theme('DarkAmber')

    ##Building the layout###
    openFolder_layout = [
        [sg.Input(key='_FILES_'), sg.FolderBrowse()], [sg.OK(), sg.Cancel()]
    ]


    ###Building the window###
    window_openFolder = sg.Window('Select folder to store the files', layout=openFolder_layout, finalize=True)
    return window_openFolder
#============================================================#







#============================================================#
#======================== MAIN WINDOW =======================#
def MainWindow():
    Log(None,"MainWindow():")

    ###Choosing the theme###
    sg.theme('Topanga')

    ##===============================Building the layout======================================###
    #--insert the playlist or video link--#
    input_link_column =[[sg.Text('LINK', font=('Arial, 12'), justification='left'), sg.InputText(size=(63, 1), key='-LINK-')]]
    
    #--select the correspondent link type--#
    options_type_column = [
        [sg.Radio('Playlist',  'link_type', default=False, key='-PLAYLIST-', font=('Helvetica, 12')),
         sg.Radio('Podcast',   'link_type', default=False, key='-PODCAST-',  font=('Helvetica, 12')),
         sg.Radio('Audiobook', 'link_type', default=False, key='-AUDIOBOOK-', font=('Helvetica, 12')),
         sg.Radio('Song',      'link_type', default=False, key='-SONG-',     font=('Helvetica, 12')),
         sg.Radio('Video',     'link_type', default=True,  key='-VIDEO-',    font=('Helvetica, 12'))
        ]
    ] 

    #-- video quality output --#
    options_qualityVideo_column = [
        [sg.Radio('Max',   'video_quality',  default=True,  key='-VMAX-',  font=('Helvetiva, 12'))],
        [sg.Radio('Min',   'video_quality',  default=False, key='-VMIN-',  font=('Helvetica, 12'))],
        [sg.Radio('4K',    'video_quality',  default=False, key='-4K-',    font=('Helvetica, 12'))],
        [sg.Radio('1080p', 'video_quality',  default=False, key='-1080p-', font=('Helvetica, 12'))],
        [sg.Radio('720p',  'video_quality',  default=False, key='-720p-',  font=('Helvetica, 12'))],
        [sg.Radio('480p',  'video_quality',  default=False, key='-480p-',  font=('Helvetica, 12'))],
        [sg.Radio('360p',  'video_quality',  default=False, key='-360p-',  font=('Helvetica, 12'))],
        [sg.Radio('240p',  'video_quality',  default=False, key='-240p-',  font=('Helvetica, 12'))],
        [sg.Radio('144p',  'video_quality',  default=False, key='-144p-',  font=('Helvetica, 12'))],
    ]

    #-- audio type output --#
    options_formatAudio_column = [
        [sg.Radio('Default', 'audio_output',  default=True,  key='-DEFA-',  font=('Helvetica, 12'))],
        [sg.Radio('MP3',     'audio_output',  default=False, key='-MP3-',   font=('Helvetiva, 12'))],
        [sg.Radio('AAC',     'audio_output',  default=False, key='-AAC-',   font=('Helvetica, 12'))],
        [sg.Radio('WAV',     'audio_output',  default=False, key='-WAV-',   font=('Helvetica, 12'))]
    ]

    #-- video type output --#
    options_formatVideo_column = [
        [sg.Radio('Default', 'video_output',  default=True,   key='-DEFV-',  font=('Helvetiva, 12'))],
        [sg.Radio('MP4',     'video_output',  default=False,  key='-MP4-',   font=('Helvetiva, 12'))],
        [sg.Radio('MKV',     'video_output',  default=False,  key='-MKV-',   font=('Helvetica, 12'))],
        [sg.Radio('AVI',     'video_output',  default=False,  key='-AVI-',   font=('Helvetica, 12'))]
    ]

    #-- ONLY AUDIO --#
    options_onlyAudio_column = [
        [sg.Checkbox('Only audio',  default=False, key='-ONLY_AUDIO-',  font=('Helvetiva, 12'))],
        [sg.Checkbox('Also split',  default=True,  key='-SPLIT_TOO-',   font=('Helvetica, 12'))]
    ]

    #-- BOTH AUDIO + VIDEOAUDIO --#
    options_audioToo_column = [
        [sg.Checkbox('Force 16:9', default=True, key='-WIDESCREEN-',  font=('Helvetiva, 12'))],
    ]


    #-- FRAMEWORKS BUILDING --#
    input_frame              = [[sg.Frame('', layout=input_link_column,   border_width=0)]]
    typeVideos_frame         = [[sg.Frame('', layout=options_type_column, border_width=1)]]
    qualityVideos_frame      = [[sg.Frame('Quality of the Video', layout=options_qualityVideo_column, border_width=1)]]
    qualityAudio_frame       = [[sg.Frame('Audio Output',         layout=options_formatAudio_column,  border_width=1)]]
    qualityVideo_frame       = [[sg.Frame('Video Output',         layout=options_formatVideo_column,  border_width=1)]]
    outputAudioVideo_frame   = [
        [sg.Frame('Audio Options', layout=options_onlyAudio_column, border_width=1)],
        [sg.Frame('Video Options', layout=options_audioToo_column,  border_width=1)]
    ]


    #-- Create layout with two columns using precreated frames --#
    main_win_layout = [
        [sg.Column(input_frame)],
        [sg.Column(typeVideos_frame, element_justification='c')],
        [sg.Column(qualityVideos_frame, element_justification='c'), 
         sg.Column(qualityAudio_frame, vertical_alignment="top"), 
         sg.Column(qualityVideo_frame, vertical_alignment="top"), 
         sg.Column(outputAudioVideo_frame, vertical_alignment="top")
        ],
        [sg.Text(" "*80), sg.Button('START', font=('Times New Roman',12))]
    ]



    ###Building the window###
    window_main = sg.Window("YTDownloader", layout=main_win_layout, finalize=True)
    return window_main
#============================================================#







if __name__ == '__main__':
    '''
    #==================================================#
    #                                                  #
    #             Testing the 'browse' GUI             #
    #                                                  #
    #==================================================# 
    win_openFile = OpenFiles()
    while True:
        window, events, values = sg.read_all_windows()
        if window == win_openFile and events == sg.WIN_CLOSED:
            Log(None, "Linha 166 - if window == win_mainWindow and events == sg.WIN_CLOSED: ")
            break  
    '''
    win_main = MainWindow()
    while True:
        window, events, values = sg.read_all_windows()
        if window == win_main and events == sg.WIN_CLOSED:
            break
      
