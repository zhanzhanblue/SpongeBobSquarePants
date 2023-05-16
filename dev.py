from pydub import AudioSegment
import os
import time

# all we use is wav because of no using the ffmpeg.
audioSpongeBob = AudioSegment.from_wav('./Sponge.wav')

# test for all of the begining. 
# it's '41900' like 'aye aye captain!' end is '43900' length is 2000. 
# '45360' for the second 'aye aye captain!' end is '47860' length is 2500. 
# '52950' for the first 'SpongeBob SquarePants' end is '54850' length is 1900.  
# '57200' for the second 'Sp Sq' end is '59100' length is 1900. 
# '61500' for the third 'S S' the same as the up one. 
# '65800' for the forth time 'S S' the same as the up one. 
# '67800' for the last 4 times 'S S'. 
# audioOutput = audioSpongeBob[67800:] 

# Let's use the same name 'input.wav'.
print("Warning! Please make sure that your file's name is 'input.wav'")
if not os.path.exists('./input.wav'):
    print("Error! Please make sure that your file's name is 'input.wav'")
    time.sleep(3)
    exit(0)

audioOthers = AudioSegment.from_wav('./input.wav')
print("Warning! Please insert a number (mm) the beging of 'aye aye captain' for getting location of your sound.")
while True:
    beginPosition = input()
    if beginPosition.isdigit():
        beginPosition = int(beginPosition)
        break
    print("Error! Please insert a number (mm) the beging of 'aye aye captain' for getting location of your sound.")

length = 1900
# print(beginPosition, type(beginPosition))
audioOutput = audioSpongeBob.overlay(audioOthers[beginPosition:beginPosition+2000], position=41900)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+47860-41900:beginPosition+47860-41900+2500], position=47860)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+52950-41900:beginPosition+52950-41900+length], position=52950)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+57200-41900:beginPosition+57200-41900+length], position=57200)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+61500-41900:beginPosition+61500-41900+length], position=61500)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+65800-41900:beginPosition+65800-41900+length], position=65800)
audioOutput = audioOutput.overlay(audioOthers[beginPosition+67800-41900:], position=67800)

audioOutput.export('out.wav', format='wav')