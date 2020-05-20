from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import ScreenManager,Screen,CardTransition,FadeTransition
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color
import csv
import wave
import pyaudio
import multiprocessing
import random
import string


#Some variable declaration.
line_ptr=0
read_files=open('TextforData.txt','r').readlines()

#multiprocessing and recording related variables.
st=multiprocessing.Value('i',1)
frames=[]

class HomeScreen(Screen):
    pass

class RecordScreen(Screen):
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)

    def next_label(self):
        global line_ptr,read_files
        line_ptr+=1
        to_ret=read_files[line_ptr]
        return to_ret
    def prev_label(self):
        global line_ptr,read_files
        line_ptr-=1
        to_ret=read_files[line_ptr]
        return to_ret
    def start_record(self,st):
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
            wf = wave.open(loc,'wb')
            wf.setnchannels(2)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
            wf.close()
            with open('./Data/transcripts.csv','a+') as csvfile:
                csvwriter=csv.writer(csvfile,delimiter=' ')
                csvwriter.writerow([f'{filename}|'+self.ids.txtread.text])
    def stop_record(self,st):
        with st.get_lock():
            st.value=0

    def ssrecord(self):
        global st
        if __name__ == '__main__':
            multiprocessing.Process(target=self.start_record,args=[st]).start()
    def strecord(self):
        global st
        if __name__ == '__main__':
            multiprocessing.Process(target=self.stop_record,args=[st]).start()






class ScreenManagement(ScreenManager):
    pass

class AboutScreen(Screen):
    pass

class ContactUSScreen(Screen):
    pass

class HelpScreen(Screen):
    pass



#Slider part.
class UISlide(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__wrapper=BoxLayout(orientation="vertical")
        self.add_widget(self.__wrapper)

    def add_child(self,child):
        self.__wrapper.add_widget(child)

class UISlider(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__scrnmngr=ScreenManager(transition=CardTransition())
        self.add_widget(self.__scrnmngr)
        self.first_touch=None
        self.moved=None

    def add_slide(self,slide:UISlide):
        self.__scrnmngr.add_widget(slide)

    def __slide(self,direction):
        mngr=self.__scrnmngr
        mngr.transition.direction=direction

        current=mngr.current_screen
        if direction=="right":
            idx=mngr.screens.index(current)
            if idx==0:
                pass
            else:
                mngr.current=mngr.previous()
        else:
            last=mngr.screens[-1]
            if current==last:
                pass
            else:
                mngr.current=mngr.next()
    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            self.first_touch=touch.x
            touch.grab(self)
            return True
        return False

    def on_touch_move(self,touch):
        if self.collide_point(touch.x,touch.y) and touch.grab_current==self:
            if self.moved:
                return
        if touch.x>self.first_touch:
            self.__slide("right")
        else:
            self.__slide("left")
        self.moved=True

    def on_touch_up(self,touch):
        if self.collide_point(touch.x,touch.y) and touch.grab_current==self:
            touch.ungrab(self)
            self.moved=None
            return True
        return False

class SliderWin(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        uislider=UISlider()
        self.add_widget(uislider)
        slide0=UISlide(name='scrn_0')
        slide1=UISlide(name='scrn_1')
        slide2=UISlide(name='scrn_2')

        im0=Image(source="slide1.jpg",allow_stretch=True)
        im1=Image(source="slide2.jpg",allow_stretch=True)
        im2=Image(source="slide3.jpg",allow_stretch=True)

        slide0.add_child(im0)
        slide1.add_child(im1)
        slide2.add_child(im2)



        uislider.add_slide(slide0)
        uislider.add_slide(slide1)
        uislider.add_slide(slide2)






class ContentNavigationDrawer(BoxLayout):
    pass



class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_file('UI.kv')

TestNavigationDrawer().run()
