# Pi_Central main program

# start up

import threading                # for face_recognition
from time import sleep
#import motion_detection_cv
#import motion_detection_pir
#import face_detection
#import face_recognition
from gpiozero import MotionSensor
import test
import cv2
from deepface import DeepFace   # for face_recognition
import vlc


movement_camera = ""
movement_pir = ""

#attempt to check to see if code is running on a Pi, if not enter a test environment
#try:
#     pir = MotionSensor(4) #insert GPIO pin that the PIR sensor is connected to
#     test_environment = false
#except (BadPinFactory):
#    test_environment = True

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# added for face face_recognition
counter = 0 # does not work as needs to be in the function

face_match = False

reference_img = cv2.imread("reference.jpg",1) # reference.jpg is the known image picture file

# start defining functions

def startup():
    test.main()
    print("Pi_Central starting up .......")
    sleep(1)
    print("initiating environmental monitoring")
    environment_monitoring() # start monitoring the environment to determine whether it is light or dark

def environment_monitoring():
    # this module determines night or day using light sensor
    light_level = light_sensor()
    if light_level <= 5:
        lights = input("It's dark, do you want me to switch the lights on? 'y' or 'n'")
        if lights == 'y':
            lights_on()
        else:
            return

def security():
    print("initiating security protocols")
    sleep(0.25)
    # this module checks for motion in the immediate area

    movement_camera = cv_motion_detection()
    movement_pir = pir_motion_detection()
    #pir_monitor()

    if movement_camera == "true" or movement_pir == "true":
        print("movement detected, initiating intruder checks")

        print("starting facial detection")
        sleep(0.5)
        face_detection()

def cv_motion_detection(): # called from security()
    # start motion cv_motion_detection
    # insert OpenCV motion detection code here ...
    global movement_camera
    if movement_camera == "":
        movement_camera = input("camera motion detection, 'y' or 'n'")
        if movement_camera == "y":
            movement_camera = "true"
        else:
            movement_camera == "false"
            print("movement_camera =", movement_camera)
            return movement_camera
    else:
        return movement_camera

def pir_motion_detection(): # called from security()
    # start pir_monitor motion detection
    global movement_pir
    if movement_pir == "":
        movement_pir = input("PIR motion detection, 'y' or 'n'")
        if movement_pir == "y":
            movement_pir = "true"
        else:
            movement_pir == "false"
        print("movement_pir =", movement_pir)
        return movement_pir

    else:
        return movement_pir

    # insert pir motion detection code here ...

    # complete code below when PIR is fitted
    #while True:
    #    if pir.motion_detected:
    #        print("movement detected")
    #        return movement_pir

    #    else:
    #        movement_pir = "false"
    #    return movement_pir

def light_sensor():
    # start light_sensor - this module determines night or day
    # find light levels
    # insert light sensor code here ...

    light_level = 4
    return light_level

def lights_on():
    # turn the lights on
    print("Turning on the lights")
    # insert lights on code here ...

def face_detection(): # called from security(), is there a face in the camera for face_detection
    while True:
        result, video_frame = video_capture.read()
        if result is False:
            print("no video")
            break

        faces = detect_bounding_box(video_frame)
        if len(faces) == 0:
            print("Faces missing")
            #return
            security()
            break
        cv2.imshow("Face Detection", video_frame)
        sleep(1)
        if len(faces) != 0:
            print("starting face_recognition")
            face_recognition() # added since last working

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows

def detect_bounding_box(video_frame): # for face_detection
    print("now running detect_bounding_box")
    gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.putText(video_frame, "Face Identified", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    return faces

def face_recognition():
    counter = 0
    while True:
        ret, frame = video_capture.read()

        if ret:
            if counter % 30 == 0:
                try:
                    threading.Thread(target=check_face, args=(frame.copy(),)).start()
                except ValueError:
                    pass

            counter += 1

            if face_match:
                cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                sleep(1)
                break
            else:
                cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                sleep(1)
            cv2.imshow("video", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    welcome()

def check_face(frame): # for face_recognition
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True

        else:
            face_match = False

    except ValueError:
        face_match = False


def play_video(player, media):
    # You need to call "set_media()" to (re)load a video before playing it

    player.set_media(media)
    player.play()

def welcome():
    print("Hello")
    # Create a new VLC instance and media player:
    #
    # This could be done in one line using vlc.MediaPlayer()
    # that will create an instance behind the scene
    # but we will pass some parameters to the instance in future example codes

    instance = vlc.Instance()
    player = instance.media_player_new()

    # Create libVLC objects representing the two videos
    video1 = vlc.Media("video1.mp4") #enter the name of the video file you wish to play and ensure the video is in the same directory as this program
    video2 = vlc.Media("video2.mp4") #enter the name of the video file you wish to play and ensure the video is in the same directory as this program
    video3 = vlc.Media("video3.mp4") #enter the name of the video file you wish to play and ensure the video is in the same directory as this program

    # Start the player for the first time
    play_video(player, video1)
    current_video = video1
    while True:
        try:
            if current_video == video1 and player.get_state() == vlc.State.Ended:
                play_video(player, video2)
                current_video = video2

            elif current_video == video2 and player.get_state() == vlc.State.Ended:
                    play_video(player, video3)
                    current_video = video3

            elif current_video == video3 and player.get_state() == vlc.State.Ended:
                return
        except:
            break

startup()
security()
print("program completed")

video_capture.release()
cv2.destroyAllWindows


# end of file
