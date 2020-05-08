from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import pyaudio
import wave
import multiprocessing,time
import random
import string

frames=[]
st=multiprocessing.Value('i',1)

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
        #loc='./Data/wavs/'+filename
        wf = wave.open(filename,'wb')
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()
        with st.get_lock():
            st.value=1

def stop_record(st):
    with st.get_lock():
        st.value=0

def prompt_start():
    time.sleep(0.8)
    print("Start")


class MultButton(GridLayout):
    def __init__(self,**kwargs):
        super(MultButton,self).__init__(**kwargs)
        self.cols=2
        # self.add_widget(Label(text='Hello Button'))
        # self.add_widget(Button(text='Hello'))
        # self.add_widget(Label(text='Shape Test'))
        # self.add_widget(Button(text='Button2'))
        self.st=1
        self.isthereprevrec=0
        self.frames=[]



    def on_touch_down(self,touch):
        multiprocessing.Process(target=prompt_start).start()
        multiprocessing.Process(target=start_record,args=[st]).start()

    def on_touch_up(self,touch):
        multiprocessing.Process(target=stop_record,args=[st]).start()






class SimpleEvent(App):
    def build(self):
        return MultButton()

if __name__=='__main__':
    SimpleEvent().run()
