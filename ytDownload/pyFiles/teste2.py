import datetime
import pytz
import json
import os
import PySimpleGUI as sg

font = ("Helvetica", 16)
str_time = "%H:%M"
text_color = "green"
background_color = "black"
justification = "center"
zones = [("Pacific", "US/Pacific"),
                 ("EST", "US/Eastern"),
                 ("London", "Europe/London"),
                 ("Sydney", "Australia/Sydney")]
tz_times = []
tz_layouts = []
tz_labels = []
frames = []
for title, _ in zones:
        tz_time = sg.Text("00:00", auto_size_text=True, font=font,
                          justification=justification, text_color=text_color,
                          background_color=background_color, border_width=2, relief="sunken")
        tz_label = sg.Text(title, auto_size_text=True, font=font,
                           justification=justification, text_color=text_color,
                           background_color=background_color, border_width=2, relief="sunken")
        z_layout = [[tz_time], [tz_label]]
        z_frame = sg.Frame(title="", layout=z_layout,
                           background_color=background_color, border_width=1,
                           element_justification=justification,
                           vertical_alignment="center")

        tz_times.append(tz_time)
        tz_layouts.append(z_layout)
        tz_labels.append(tz_label)
        frames.append(z_frame)
layout = [frames]
window = sg.Window("TimeZones", layout, resizable=True,
                       background_color=background_color, auto_size_text=True,
                       no_titlebar=True, return_keyboard_events=True, text_justification="center", element_justification="center")
window.read(timeout=1)
window.Maximize()

# Create an event loop
while True:
    event, values = window.read(timeout=1000)
    font_updated = False
    # End program if user closes window
    if (event == sg.WIN_CLOSED) or (event == "\r"):
        break

    # If not, update times
    for frame in frames:
        frame.expand(expand_x=True)
        frame.update()
    for idx, tz_time in enumerate(tz_times):
        frame = frames[idx]
        label = tz_labels[idx]
        _, zone_name = zones[idx]
        z_datetime = datetime.datetime.now().astimezone(
                pytz.timezone(zone_name)
        )
        tz_time.update(value=z_datetime.strftime(str_time))

    window.finalize()

window.close()