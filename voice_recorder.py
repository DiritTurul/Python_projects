import sounddevice as sd
import wavio as wv
import time
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Voice_Recorder")
print(ascii_banner)
dur = int(input("Enter thelength of the RECORDING - "))
print("an aditional 1 sec is added to your recoeding session of ", dur)
freq = 44100
duration = dur + 1
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Recording saved Succesfully")
countdown(dur) 
sd.wait()
wv.write("recording.wav", recording, freq, sampwidth=2)

