# Pi_Central
The aim of this project is to develop a computer simulation that is similar to those found in Sci Fi Programs that I followed as a child. These were the Centra Computer System on the Star Ship Liberator from Blake’s Seven, Holly from Red Dwarf. I guess ORAC from Dr Who should also get a mention here. Other later inspirations for this project would have been CENTRAL, the mainframe computer system in Judge Dredd and Jarvis from Iron Man.

**Requirements**
To run the program the following mudules will need to be installed:
opencv
deepface
python-vlc

**Explanation**
The main program is called pi_central.py, this contains the main program. In the same folder you will need an image named reference.jpg, this is the image that is used by function face_detection to check whether the face (if found) is recognised. Once recognised the program will play a number of videos. These videos also need to be in the same folder as the main program or the path to them needs to be amended in pi_central.py    

**Folder and File Structure:** 
Program Folder
  <pi_central.py
  <reference.jpg
  <video1.mp4
  <video2.mp4
  <video3.mp4

**In Progress**
This is a work in progress and although a working example, some elements have been bypassed as they have yet to be completed. The light sensor, opencv motion detetection and pir motion detections external functions / modules have not yet been written. To get around this a simple input statement check has been added to simulate these. I have reached the point where it will start face detection and when a face is detected in the camera, it will start face recognition using the reference.jpg image as a reference to check against.




