# CS109 view hacks

I heard good things about http://cs109.org/ and have started going through it.

However, I'm a big fan of watching videos at > 1X speed, and the built in viewer tools did not allow this.

However the syncronized slide viewer is kind of nice.

These tools do three things:

- scrape the course schedule and fetch an XML file per lecture
- download the FLV file for the lecture video (in highest res)
- load the right slide for the current video position in VLC, regardless of playback speed


You need the rtmpdump set of tools (on Mac: brew install rtmpdump)

	cd harvard-view-tools
	brew install rtmpdump
	# you've already set up a virtualenv, right?
	pip install -r requirements.txt
	python get_class.py
	python get_video.py L01.xml
	# open video in VLC, then
	python slide_player.py L01.xml
	# ^C when done


### License
Copyright 2014 Preston Holmes

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
