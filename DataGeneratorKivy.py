from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import ScreenManager,Screen,CardTransition
from kivy.uix.image import Image


KV = '''
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
            id: md_list



Screen:

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

        im0=Image(source="Bird.png",allow_stretch=True)
        im1=Image(source="wallpaper.jpg",allow_stretch=True)
        im2=Image(source="elephant-illusion.jpg",allow_stretch=True)

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
        return Builder.load_string(KV)
        # return SliderWin()
    def on_start(self):
        icons_item = {
            "record":"Record Voice",
            "help": "Help",
            "information": "About"
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


TestNavigationDrawer().run()
