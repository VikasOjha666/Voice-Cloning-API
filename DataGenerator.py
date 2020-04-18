from tkinter import *
import pyaudio
import wave



class RecordAPI:

    def __init__(self, chunk=3024, format=pyaudio.paInt16, channels=2, rate=44100):
        self.top=Tk()
        self.top.title('Data Generator')
        self.top.geometry('500x400')
        self.record_button=Button(self.top,text='Record',fg='red',command=lambda:self.start_record())
        self.record_button.bind("<Button-1>", self.start_record)
        self.record_button.bind("<ButtonRelease-1>", self.stop)
        self.next_button=Button(self.top,text='Next',fg='red',command=lambda:self.change_label())
        self.heading=Label(self.top,text='Record Speech',fg='red')
        self.txt1=Text(self.top,height=20,width=60,fg='red')
        self.txt1.insert(INSERT,"Hello how are you")
        self.collections = []
        self.CHUNK = chunk
        self.i=0
        self.list1=['How are you?','I am fine.','I am dangerous','I dreamed I was messing you were so scared and no one would listen cause no one cared so if your asking me']
        self.FORMAT = format
        self.CHANNELS = channels
        self.RATE = rate
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        self.heading.pack()
        self.txt1.pack()
        self.record_button.pack()
        self.next_button.pack()
        #self.stop_button.pack()
        self.top.mainloop()





    def get_index(self):
        idx=self.i
        self.i+=1
        return idx

    def change_label(self):
        try:
            self.txt1.delete('1.0',END)
            text2insert=self.list1[self.get_index()]
            self.txt1.insert(INSERT,text2insert)
            self.top.update()
        except:
            pass

    def start_record(self,event):
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            self.top.update()

        stream.close()

        wf = wave.open('test_recording.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self,event):
        self.st = 0

recapi = RecordAPI()
