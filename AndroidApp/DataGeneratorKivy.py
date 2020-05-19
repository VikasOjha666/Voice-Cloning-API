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


class HomeScreen(Screen):
    pass

class RecordScreen(Screen):
    def __init__(self,**kwargs):
        self.textinp='text1'
        super(Screen,self).__init__(**kwargs)

class ScreenManagement(ScreenManager):
    pass

class AboutScreen(Screen):
    pass

class ContactUSScreen(Screen):
    pass

class HelpScreen(Screen):
    pass


KV1 = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "Voice Cloning Tool"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "MENU"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            OneLineListItem:
                text:'Home'
                on_release:app.root.current='home_screen'

            OneLineListItem:
                text:'Record Voice'
                on_release:app.root.current='rec_screen'
            OneLineListItem:
                on_release:app.root.current='help_screen'
                text:'Help'
            OneLineListItem:
                text:'About'
                on_release:app.root.current='about_screen'

            OneLineListItem:
                text:'Contact Us'
                on_release:app.root.current='contact_screen'
ScreenManagement:
    transition:FadeTransition()
    HomeScreen:
    RecordScreen:
    HelpScreen:
    AboutScreen:
    ContactUSScreen:

<HomeScreen>:
    name:'home_screen'

    NavigationLayout:

        ScreenManager:

            Screen:
                SliderWin

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Explore Voice cloning Tool"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

<RecordScreen>:
    name:'rec_screen'

    NavigationLayout:

        ScreenManager:

            Screen:



                BoxLayout:

                    orientation: 'vertical'

                    MDToolbar:
                        title: "Explore Voice cloning Tool"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    FloatLayout:
                        Label:
                            text:'Record your voice'
                            size_hint:0.5,0.1
                            color:0,1,0,1
                            pos_hint:{'x':0.25,'y':0.9}
                        TextInput:
                            text:'This is a text example you have to read.'
                            size_hint:0.7,0.2
                            pos_hint:{'x':0.13,'y':0.7}
                            color:0,1,0,1
                        Button:
                            text:'Record'
                            size_hint:0.1,0.1
                            pos_hint:{'x':0.45,'y':0.6}
                            color:0,1,0,1
                        Button:
                            text:'Next'
                            size_hint:0.1,0.1
                            pos_hint:{'x':0.55,'y':0.6}
                            color:0,1,0,1
                        Button:
                            text:'Prev'
                            size_hint:0.1,0.1
                            pos_hint:{'x':0.35,'y':0.6}
                            color:0,1,0,1







        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

<HelpScreen>:
    name:'help_screen'

    NavigationLayout:

        ScreenManager:

            Screen:



                BoxLayout:

                    orientation: 'vertical'

                    MDToolbar:
                        title: "Explore Voice cloning Tool"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    FloatLayout:
                        Label:
                            text:'HELP'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.9}
                            color:1,0,0,1
                        Label:
                            text:'See the text displayed on the screen'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.85}
                            color:0,1,0,1
                        Label:
                            text:'and read it while holding record button.'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.80}
                            color:0,1,0,1

                        Label:
                            text:'As soon as you complete reading the text'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.75}
                            color:0,1,0,1

                        Label:
                            text:'release the hold button.Click next to view'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.70}
                            color:0,1,0,1

                        Label:
                            text:'next text.Prev in case you want to repeat previous text.'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.65}
                            color:0,1,0,1
                        Label:
                            text:'For any additional queries you can contact the developer'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.60}
                            color:0,1,0,1
                        Label:
                            text:'on:darkemperorVKO@gmail.com'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.55}
                            color:0,1,0,1


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer



<AboutScreen>:
    name:'about_screen'

    NavigationLayout:

        ScreenManager:

            Screen:



                BoxLayout:

                    orientation: 'vertical'

                    MDToolbar:
                        title: "Explore Voice cloning Tool"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    FloatLayout:
                        Label:
                            text:'ABOUT VOICE CLONING APP'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.9}
                            color:1,0,0,1
                        Label:
                            text:'This app was developed by Vikas Kumar Ojha'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.85}
                            color:0,1,0,1
                        Label:
                            text:'so as to aid the user in creating voice sample '
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.80}
                            color:0,1,0,1

                        Label:
                            text:'currently app supports just creating data'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.75}
                            color:0,1,0,1

                        Label:
                            text:'as the AI model for the app was too heavy for'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.70}
                            color:0,1,0,1

                        Label:
                            text:'deploying on a phone. '
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.65}
                            color:0,1,0,1
                        Label:
                            text:'But in future backend may be deployed in cloud.'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.60}
                            color:0,1,0,1
                        Label:
                            text:'Currently the app only support data creation in english '
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.55}
                            color:0,1,0,1

                        Label:
                            text:'but soon enough it will be available for Hindi.'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.50}
                            color:0,1,0,1

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer


<ContactUSScreen>:
    name:'contact_screen'

    NavigationLayout:

        ScreenManager:

            Screen:



                BoxLayout:

                    orientation: 'vertical'

                    MDToolbar:
                        title: "Explore Voice cloning Tool"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    FloatLayout:
                        Label:
                            text:'CONTACT US'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.9}
                            color:1,0,0,1
                        Label:
                            text:'Email id:darkemperorVKO@gmail.com'
                            size_hint:0.5,0.1
                            pos_hint:{'x':0.3,'y':0.85}
                            color:1,0,0,1

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer


'''

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
        return Builder.load_string(KV1)

TestNavigationDrawer().run()
