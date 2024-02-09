#  -*- coding: UTF-8 -*-
# unihiker.com

from unihiker import GUI
import time

print("Hello World")
print("Start...")
time.sleep(2)

u_gui=GUI()

u_gui.draw_text(text="你好，",x=10,y=30,font_size=15, color="#FF0000")
u_gui.draw_text(text="行空板！",x=65,y=30,font_size=15, color="#FF6600")
u_gui.draw_text(text="Hello,",x=10,y=70,font_size=15, color="#FFFF00")
u_gui.draw_text(text="UNIHIKER!",x=65,y=70,font_size=15, color="#33FF33")
u_gui.draw_text(text="안녕하세요,",x=10,y=110,font_size=15, color="#33FFFF")
u_gui.draw_text(text="UNIHIKER!",x=125,y=110,font_size=15, color="#3333FF")
u_gui.draw_text(text="こんにちは、",x=10,y=150,font_size=15, color="#6600CC")
u_gui.draw_text(text="UNIHIKER!",x=125,y=150,font_size=15, color="#FFCCFF")
u_gui.draw_emoji(emoji="Wink",origin="center",x=120,y=230,w=100,duration=0.1)

while True:
    pass
