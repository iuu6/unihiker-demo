from unihiker import GUI , Audio  
import time  
from datetime import datetime 
from pinpong.board import Board,Pin,Tone 

print("Alarm Clock")
print("Start...")
time.sleep(2)

def languageIsZh():
    import locale
    current_locale, encoding = locale.getdefaultlocale()
    if 'zh' in current_locale.lower():
        return True

if languageIsZh():
    print("联网后时间自动校准")
print("Automatic time calibration after networking")
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

Board().begin() 
tone = Tone(Pin(Pin.P26)) 
tone.freq(800) 

gui = GUI()  
audio = Audio() 

gui.fill_rect(x=0, y=0, w=240, h=320, color="#96adfd") 
gui.fill_rect(x=75, y=30, w=90, h=30, color="#7bed9f") 
gui.fill_rect(x=75, y=70, w=90, h=30, color="#7bed9f")

text1 = gui.draw_text(x=120, y=30, text='Sound:', origin = 'top') 
text_sound = gui.draw_text(x=120, y=70, text='', font_size=15, origin = 'top')

emj1 = gui.draw_emoji(x=82, y=90, w=100,h=100, emoji="Smile", duration=0.1) 
clock = gui.fill_clock(x=120, y=230, r=60, h=3, m=4, s=5, color=(255, 255, 255), fill="#57b5ff")

def clock_update():
    print("thread1 start")
    while True: 
        t = time.localtime() 
        clock.config(h=time.strftime("%H", t), m=time.strftime("%M", t), s=time.strftime("%S", t)) 
        time.sleep(1)
        now_time = datetime.now().strftime('%H:%M') 
        print(now_time)
        if  now_time == '8:00': 
            tone.on() 
            time.sleep(1) 
            tone.off() 
            time.sleep(0.5)    
    print("thread1 end")


clock_thread = gui.start_thread(clock_update)

while True :
    Sound = audio.sound_level()  
    text_sound.config(text = Sound) 
    time.sleep(0.1) 
    if Sound > 50: 
        emj1.config(emoji= "Angry")
        tone.on()  
        time.sleep(1) 
        tone.off() 
        time.sleep(0.5) 
        emj1.config(emoji= "Smile") 