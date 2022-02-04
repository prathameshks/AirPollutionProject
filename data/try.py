import tkinter
from typing import Union
window=tkinter.Tk()

print(window: Union[tkinter.Tk, tkinter.Toplevel])

# win.bind('<Configure>', setbackground)
# print("passed here")

# import os

# l=os.walk(r"C:\Users\ADMIN\AppData")
# for i in l:
#     print(i)





# futuredata={'o3': [{'avg': 28, 'day': '2020-11-22', 'max': 49, 'min': 19}, {'avg': 34, 'day': '2020-11-23', 'max': 49, 'min': 26}, {'avg': 30, 'day': '2020-11-24', 'max': 48, 'min': 19}, {'avg': 28, 'day': '2020-11-25', 'max': 47, 'min': 19}, {'avg': 31, 'day': '2020-11-26', 'max': 43, 'min': 24}, {'avg': 52, 'day': '2020-11-27', 'max': 65, 'min': 37}, {'avg': 49, 'day': '2020-11-28', 'max': 50, 'min': 48}], 'pm10': [{'avg': 30, 'day': '2020-11-22', 'max': 30, 'min': 30}, {'avg': 41, 'day': '2020-11-23', 'max': 45, 'min': 30}, {'avg': 45, 'day': '2020-11-24', 'max': 45, 'min': 45}, {'avg': 42, 'day': '2020-11-25', 'max': 45, 'min': 28}, {'avg': 45, 'day': '2020-11-26', 'max': 45, 'min': 45}, {'avg': 45, 'day': '2020-11-27', 'max': 45, 'min': 45}, {'avg': 30, 'day': '2020-11-28', 'max': 45, 'min': 27}, {'avg': 27, 'day': '2020-11-29', 'max': 27, 'min': 20}, {'avg': 27, 'day': '2020-11-30', 'max': 30, 'min': 27}], 'pm25': [{'avg': 89, 'day': '2020-11-22', 'max': 89, 'min': 89}, {'avg': 109, 'day': '2020-11-23', 'max': 137, 'min': 89}, {'avg': 128, 'day': '2020-11-24', 'max': 137, 'min': 96}, {'avg': 116, 'day': '2020-11-25', 'max': 137, 'min': 89}, {'avg': 135, 'day': '2020-11-26', 'max': 137, 'min': 116}, {'avg': 128, 'day': '2020-11-27', 'max': 137, 'min': 91}, {'avg': 88, 'day': '2020-11-28', 'max': 137, 'min': 67}, {'avg': 88, 'day': '2020-11-29', 'max': 89, 'min': 70}, {'avg': 89, 'day': '2020-11-30', 'max': 89, 'min': 89}], 'uvi': [{'avg': 0, 'day': '2020-11-23', 'max': 0, 'min': 0}, {'avg': 1, 'day': '2020-11-24', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2020-11-25', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2020-11-26', 'max': 5, 'min': 0}, {'avg': 1, 'day': '2020-11-27', 'max': 5, 'min': 0}, {'avg': 3, 'day': '2020-11-28', 'max': 5, 'min': 0}]}

# import matplotlib.pyplot as plt
# def show_forecast_graph_c():
#     w=0.2
#     mx=0
#     def maker(data):
#         if len(data)!= minl :
#             for i in range(minl-len(data)):
#                 data.append(0)
#         return data
#     for i in futuredata.keys():
#         n=len(futuredata[i])
#         if n>mx:
#             mx=n
#             mainp=i
#     xlabel=[d['day'] for d in futuredata[mainp]]
#     minl=len(xlabel)
#     print(xlabel)
#     bar=[s for s in range(minl)]
#     barx=bar
#     w=0
#     for i in futuredata.keys():
#         data=[]
#         for j in futuredata[i]:
#             data.append(j['avg'])
#         data=maker(data)
#         bar=[i+w for i in bar]
#         w=0.2
#         plt.bar(bar, data,w,label=i)
#     plt.xlabel('date')
#     plt.ylabel('value')
#     bar2=[p+w*3/2 for p in barx]
#     plt.title('data value')
#     plt.xticks(bar2,xlabel)
#     plt.legend()
#     plt.show()


# data1 = [5, 25, 50, 20]
# data2 = [4, 23, 51, 17]
# data3 = [6, 22, 52, 19]
# l=['abc1','abc2','abc3','abc4']

# bar1=np.arange(len(l))
# bar2=[i+w for i in bar1]
# bar3=[i+w for i in bar2]
# plt.bar(bar1, data1,w,label="datan1")
# plt.bar(bar2, data2,w,label="datan2")
# plt.bar(bar3, data3,w,label="datan3")

# plt.xlabel('data')
# plt.ylabel('value')
# plt.title('data value')
# plt.xticks(bar1+w,l)
# plt.legend()
# plt.show()


"""

from tkinter import *

def donothing():
     filewin = Toplevel(root)
     button = Button(filewin, text="Do nothing button")
     button.pack()
     
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
"""

