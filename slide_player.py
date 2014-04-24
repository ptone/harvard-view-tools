from appscript import *
import xml.etree.ElementTree as ET
import time
import webbrowser
import sys



tree = ET.parse(sys.argv[1])
root = tree.getroot()

slides = {}
for ts in root[0][2]:
    slides[int(ts.find('timeInSeconds').text)] = ts.find('url').text


offset = int(root[0][0][0].find('offsetInSeconds').text)
vlc = app("VLC")
current_slide = None
while True:
    current_time = vlc.current_time() - offset
    slide_time = min(slides.keys(), key=lambda x:abs(x - current_time))
    print current_time, slide_time
    slide_url = slides[slide_time]
    # not sure why - sometimes slidetime > current time
    if slide_url != current_slide and slide_time < current_time:
        current_slide = slide_url
        webbrowser.open(slide_url)
    time.sleep(1)

