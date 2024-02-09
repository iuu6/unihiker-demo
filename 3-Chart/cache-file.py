#  -*- coding: UTF-8 -*-
# unihiker.com

from unihiker import GUI
import time

print("Chart")
print("Start...")
time.sleep(2)

def numberMap(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def math_mean(myList):
  return float(sum(myList)) / len(myList)


def draw_line_chart():
    global X
    global Y
    global Y1
    global data_all_ls
    for my_variable in range(0, 10):
        data1 = (data_all_ls[my_variable])
        X = (X + 20)
        Y = (numberMap(data1, 0, 2100, 150, 10))
        circle=u_gui.fill_circle(x=X,y=Y,r=2,color="#FF6600")
        if (X > 39):
            u_gui.draw_line(x0=(X - 20),y0=Y1,x1=X,y1=Y,width=1,color="#FF6600")
        Y1 = Y
        time.sleep(1)

def draw_histogram():
    global data1_ls
    global data_all_ls
    global Y
    global data2_ls

    u_gui.fill_rect(x=180,y=160,w=20,h=10,color="#FF6600")
    u_gui.draw_text(text="label1",x=205,y=158,font_size=8, color="#000000")
    u_gui.fill_rect(x=180,y=175,w=20,h=10,color="#FF99FF")
    u_gui.draw_text(text="label2",x=205,y=173,font_size=8, color="#000000")
    u_gui.fill_rect(x=180,y=190,w=20,h=10,color="#0000FF")
    u_gui.draw_text(text="label3",x=205,y=188,font_size=8, color="#000000")
    time.sleep(1)
    Y = (numberMap(math_mean(data_all_ls), 0, 2100, 300, 160))
    u_gui.draw_line(x0=70,y0=Y,x1=70,y1=300,width=20,color="#FF6600")
    u_gui.draw_text(text=math_mean(data_all_ls),x=50,y=(Y - 15),font_size=8, color="#FF6600")
    time.sleep(1)
    for my_variable in range(1, 10, 2):
        data1_ls.append((data_all_ls[my_variable]))
    Y = (numberMap(math_mean(data1_ls), 0, 2100, 300, 160))
    u_gui.draw_line(x0=110,y0=Y,x1=110,y1=300,width=20,color="#FF99FF")
    u_gui.draw_text(text=math_mean(data1_ls),x=90,y=(Y - 15),font_size=8, color="#FF99FF")
    time.sleep(1)
    for my_variable in range(0, 10, 2):
        data2_ls.append((data_all_ls[my_variable]))
    Y = (numberMap(math_mean(data2_ls), 0, 2100, 300, 160))
    u_gui.draw_line(x0=150,y0=Y,x1=150,y1=300,width=20,color="#0000FF")
    u_gui.draw_text(text=math_mean(data2_ls),x=130,y=(Y - 15),font_size=8, color="#0000FF")
    time.sleep(1)


u_gui=GUI()
aixs=u_gui.draw_image(image="axisimg.png",x=0,y=0)
data_all_ls = [1675,1028,1205,1165,1985,1305,1897,1195,1498,995]
data1_ls = []
data2_ls = []
X = 19
Y = 0
Y1 = 0
draw_line_chart()
draw_histogram()

while True:
    pass
