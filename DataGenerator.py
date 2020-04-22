#Generates data for the voice cloning model.
from tkinter import *
import pyaudio
import wave
import string
import csv
import random



class RecordAPI:

    def __init__(self, chunk=3024, format=pyaudio.paInt16, channels=2, rate=44100):
        """Creates the GUI for the data generator."""
        self.top=Tk()
        self.top.title('Data Generator')
        self.top.geometry('500x430')
        self.record_button=Button(self.top,text='Record',fg='red',command=lambda:self.start_record())
        self.record_button.bind("<Button-1>", self.start_record)
        self.record_button.bind("<ButtonRelease-1>", self.stop)
        self.next_button=Button(self.top,text='Next',fg='red',command=lambda:self.change_label())
        self.prev_button=Button(self.top,text='Prev',fg='red',command=lambda:self.prev_label())
        self.heading=Label(self.top,text='Record Speech',fg='red')
        self.txt1=Text(self.top,height=20,width=60,fg='red')
        self.txt1.insert(INSERT,"This is welcome screen")
        self.collections = []
        self.CHUNK = chunk
        self.i=-1
        self.txtstream=open('TextforData.txt','r').readlines()
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
        self.prev_button.pack()
        self.top.mainloop()




    def prev_index(self):
        """Gives the index using which the text is obtained which has to be shown on GUI. """
        self.i-=1
        return self.i

    def prev_label(self):
        """Changes the text on text generator GUI"""
        try:
            self.txt1.delete('1.0',END)
            text2insert=self.txtstream[self.prev_index()]
            self.txt1.insert(INSERT,text2insert)
            self.top.update()
        except:
            pass

    def get_index(self):
        """Gives the index using which the text is obtained which has to be shown on GUI. """
        self.i+=1
        return self.i

    def change_label(self):
        """Changes the text on text generator GUI"""
        try:
            self.txt1.delete('1.0',END)
            text2insert=self.txtstream[self.get_index()]
            self.txt1.insert(INSERT,text2insert)
            self.top.update()
        except:
            pass
    def random_filename(self):
        textpart=[np.random.choice([string.alphabets])]

    def start_record(self,event):
        """Records the audio until self.st variable is True and saves to file."""
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            self.top.update()

        stream.close()
        filename=''.join(random.choice(string.ascii_lowercase) for i in range(12))
        filename=filename+'.wav'
        loc='./Data/wavs/'+filename
        wf = wave.open(loc,'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        with open('./Data/transcripts.csv','a+') as csvfile:
            csvwriter=csv.writer(csvfile,delimiter=' ')
            csvwriter.writerow([f'{filename}|'+self.txt1.get("1.0",END)])

    def stop(self,event):
        """Sets the self.st variable to false which stops the recording. """
        self.st = 0

#Cretes the instance of the Recorder Object.
recapi = RecordAPI()
