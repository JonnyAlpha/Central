# Pi_Central
The aim of this project is to develop a computer similar to those found in Sci Fi Programs that I followed as a child. These were the Centra Computer System on the Star Ship Liberator from Blake’s Seven, Holly from Red Dwarf. I guess ORAC from Dr Who should also get a mention here. Other later inspirations for this project would have been CENTRAL, the mainframe computer system in Judge Dredd and Jarvis from Iron Man.
The main computer is currently a Raspberry Pi 4 - 4GB version running in an Argon M.2 Case with and M.2 SSD Drive on which the OS is stored.
Central will be tested on this setup but may be moved to a separate Pi 4.
As part of the overall project, the intent will also to have a mobile robot called Hammerstein Mk2. Hammerstein will be the eyes and ears on the ground for Central.

**Explanation**
The main program is called pi_central.py, this contains the main program. In the same folder you will need an image named reference.jpg, this is the image that is used by function face_detection to check whether the face (if found) is recognised. Once recognised the program will play a number of videos. These videos need to be in the same folder as the main program or the path to them needs to be amended in pi_central.py     
