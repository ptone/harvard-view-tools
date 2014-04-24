import sys
import os
import xml.etree.ElementTree as ET
from subprocess import call


cmd = "rtmpdump -r rtmp://flash.dce.harvard.edu/bounce -C B:0 -C Z: \
-C S:/{vidlink} \
-C S:BounceAPI3.0 -C N:0.000000 -C S:mp4 \
-y mp4:{vidlink} \
-o {lesson}.flv"

def get_vid_from_xml(f):
    tree = ET.parse(f)
    root = tree.getroot()
    rtmp_link = root.getchildren()[0][0][0][0].text
    lesson = os.path.splitext(os.path.basename(f))[0]
    dl_cmd = cmd.format(vidlink=rtmp_link.split(':')[-1], lesson=lesson)
    call(dl_cmd, shell=True)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        get_vid_from_xml(f)
