import pyaudio
import wave
from threading import Thread
import multiprocessing
import random
import string
import time

st=multiprocessing.Value('i',1)
frames=[]
def start_record(st):
        """Records the audio until self.st variable is True and saves to file."""
        frames = []
        stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=3024)
        while st.value == 1:
            data = stream.read(3024)
            frames.append(data)
            print("* recording")

        stream.close()
        filename=''.join(random.choice(string.ascii_lowercase) for i in range(12))
        filename=filename+'.wav'
        loc='./Data/wavs/'+filename
        wf = wave.open(filename,'wb')
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()

def stop_record(st):
    print("Sleep")
    time.sleep(3)
    with st.get_lock():
        st.value=0
    print(st.value)

def print_i():
    for i in range(10):
        print(f"{str(i)}")
if __name__ == '__main__':
    multiprocessing.Process(target=start_record,args=[st]).start()
    multiprocessing.Process(target=stop_record,args=[st]).start()
