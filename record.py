import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk, ImageSequence
from itertools import count
import tkinter as tk
import string
from PIL import GifImagePlugin
import wave

#import selecting
# obtain audio from the microphone
def data_gif():

    isl_gif=['all the best', 'any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call an ambulance', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your age', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight']
    g=isl_gif   
    return g
        
def data_img():
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
    p=arr
    return p
def func():
    r = sr.Recognizer()
    data_gif()
    data_img()
    with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print('Say something')
                        audio = r.listen(source)

                                                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                print("you said " + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                if(a.lower()=='goodbye'):
                                        print("oops!Time To say good bye")
                                        break
                               
                                elif(a.lower() in isl_gif):
                                                                 
                                    path = 'ISL_Gifs/{}.gif'.format(a.lower())
                
                                    for img in ImageSequence.Iterator(Image.open(path)):
                                        ImageNumpyFormat = np.asarray(img)
                                        plt.imshow(ImageNumpyFormat)
                                        plt.draw()
                                        plt.pause(0.0002) 
                                else:

                                    for i in range(len(a)):
                                                    
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8) 
                                                            
                                                    else:
                                                            continue

                        except:
                               print("Could not listen")
                        plt.close()
import pyaudio
import wave
def sound():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 10
    filename = "output.wav"
    
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    
    print('Recording')
    
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
        
    print('Finished recording')

# Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

import simpleaudio as sa
def play():
    

    filename = 'output.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


from os import path
from pydub import AudioSegment
        
def text():
    data_gif()
    data_img()


# transcribe audio file                                                         
    AUDIO_FILE = "output.wav"

# use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
         audio = r.record(source)
         a= r.recognize_google(audio)
         print(a)
         i=0
         while True:
             try:
                 
                 for c in string.punctuation:
                     a= a.replace(c,"")
                 
                 if(a.lower() in isl_gif):
                     path = 'ISL_Gifs/{}.gif'.format(a.lower())
                     for img in ImageSequence.Iterator(Image.open(path)):
                         ImageNumpyFormat = np.asarray(img)
                         plt.imshow(ImageNumpyFormat)
                         plt.draw()
                         plt.pause(0.0002) 
                     break
                 else:
                     for i in range(len(a)):
                         if(a[i] in arr):
                             ImageAddress = 'letters/'+a[i]+'.jpg'
                             ImageItself = Image.open(ImageAddress)
                             ImageNumpyFormat = np.asarray(ImageItself)
                             plt.imshow(ImageNumpyFormat)
                             plt.draw()
                             plt.pause(0.8) 
                         else:
                             continue
                 break
             except:
                 print("Recorded Data not found")
                 break
                 plt.close()
            
            
#func()
while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!","Record Audio","Play Audio","TEXT"]
  reply = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        exit()
  if reply==choices[2]:
      sound()
  if reply==choices[3]:
      play()
  if reply==choices[4]:
      text()