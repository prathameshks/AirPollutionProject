from tkinter import *
import tkinter
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3 as sql
import webbrowser as wb
import os
import urllib.request
from datetime import datetime
import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
from time import sleep
import ctypes
import requests  # pip install requests
from PIL import Image, ImageTk  # pip install pillow
import matplotlib.pyplot as plt  # pip install matplotlib
import center_tk_window  # pip install center_tk_window

u32 = ctypes.windll.user32
u32.SetProcessDPIAware()
swidth, shight = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
time = datetime.now()
timemain = int(time.hour)
root.attributes("-topmost", False)
root.iconbitmap(default='data\\icon.ico')
root.attributes("-fullscreen", True)
if timemain >= 18 or timemain <= 6:
    mainbgnight = Image.open('data/MAINBACKG.jpg')
    mainbgnight1 = mainbgnight.resize((int(swidth), int(shight)), Image.ANTIALIAS)
    mainbgpic = ImageTk.PhotoImage(mainbgnight1)
else:
    mainbgday = Image.open('data/MAINBACKGDAY.jpg')
    mainbgday1 = mainbgday.resize((int(swidth), int(shight)), Image.ANTIALIAS)
    mainbgpic = ImageTk.PhotoImage(mainbgday1)
mainbg = Label(root, image=mainbgpic)
mainbg.grid(row=0, column=0, sticky='nsew')
searchcityforgrapha = False
fullall = False
allsw = int(swidth * 3 / 10)
allsh = 50
color = '#AED6F1'
win = Toplevel()
root.attributes("-alpha", 0.95)
win.attributes("-topmost", True)
win.title('HOME')
win.minsize(470, 600)
win.geometry('400x700')
win.config(bg=color)
center_tk_window.center(root, win)
win.iconbitmap('data\\icon.ico')
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(2, weight=2)
win.rowconfigure(1, weight=2)
win.rowconfigure(3, weight=2)
win.rowconfigure(4, weight=2)
win.rowconfigure(5, weight=2)
win.rowconfigure(6, weight=1)
win.rowconfigure(7, weight=1)


def fullfunfscr(wind, rowp, cp, csp=1, rsp=1):
    def fscreen():
        global fullall
        wind.attributes("-fullscreen", True)
        fullall = True

    def fscreenout():
        global fullall
        wind.attributes("-fullscreen", False)
        fullall = False

    btf = ttk.Button(wind, text='Fullscreen', command=fscreen)
    btf.grid(row=rowp, column=cp, columnspan=csp, rowspan=rsp, sticky='NE', padx=100)
    btfn = ttk.Button(wind, text='Exit Fullscreen', command=fscreenout)
    btfn.grid(row=rowp, column=cp, columnspan=csp, rowspan=rsp, sticky='Ne', padx=185)


fullfunfscr(win, 0, 0)


def cehckfull(winx):
    if fullall:
        win.attributes("-fullscreen", True)
    else:
        win.attributes("-fullscreen", False)


# close btn
def quit():
    win.withdraw()
    echoicem = messagebox.askokcancel("Exit Application", "Do you really want to Exit", icon="warning")
    if echoicem:
        win.destroy()
        exit()
    else:
        win.deiconify()


bt = ttk.Button(win, text='Exit Application', command=quit)
bt.grid(row=0, column=0, sticky='NE')

# main image
main = Image.open('data/main1.png')
main1 = main.resize((350, 150), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(main1)
labelsky = Label(win, image=pic, bg=color)
labelsky.grid(row=1, column=0, sticky='nsew')


# check your city data
def citydata():
    global fullall
    w1 = Toplevel(win)
    win.withdraw()
    w1.title('Check Your City Pollution')
    w1.geometry("+%d+%d" % (allsw - 200, 0))
    cehckfull(w1)
    w1.attributes("-topmost", True)
    fullfunfscr(w1, 0, 1, csp=2)
    w1.minsize(600, 330)
    w1.iconbitmap('data\\icon.ico')
    center_tk_window.center(win, w1)
    w1.config(bg=color)
    w1.columnconfigure(0, weight=1)
    w1.columnconfigure(1, weight=1)
    w1.columnconfigure(2, weight=0)
    w1.rowconfigure(0, weight=0)
    w1.rowconfigure(1, weight=1)
    w1.rowconfigure(3, weight=0)
    w1.rowconfigure(4, weight=1)
    w1.rowconfigure(5, weight=1)
    w1.rowconfigure(6, weight=1)
    w1.rowconfigure(7, weight=1)
    w1.rowconfigure(8, weight=1)
    w1.rowconfigure(9, weight=1)
    w1.rowconfigure(10, weight=1)
    w1.rowconfigure(11, weight=1)
    w1.rowconfigure(12, weight=1)
    w1.rowconfigure(13, weight=1)
    w1.rowconfigure(14, weight=1)
    w1.rowconfigure(15, weight=1)
    w1.rowconfigure(16, weight=1)
    w1.rowconfigure(17, weight=1)
    w1.rowconfigure(18, weight=1)

    # close btn
    def clz1():
        w1.destroy()
        win.deiconify()

    btw1 = ttk.Button(w1, text='Close', command=clz1)
    btw1.grid(row=0, column=1, columnspan=2, sticky='NE')

    # w1 main image
    labelw1 = Label(w1, image=w1pic, bg=color)
    labelw1.grid(row=1, column=0, columnspan=3, sticky='nsew')

    # w1 city search entry
    fcity = open('data/CityList.txt', 'r')
    citynames = (fcity.read().split(","))
    citylist = ['Please Select City.'] + citynames
    dropdown = ttk.Combobox(w1, values=citylist)
    dropdown.current(0)
    dropdown.grid(row=2, column=0, sticky='nsew')

    # search cmd
    def search():
        city = dropdown.get()
        search_main(city)

    def locsearch():
        try:
            resloco = requests.get('https://ipinfo.io/')
            data_locauto = resloco.json()
            cityl = data_locauto['city']
            search_main(cityl)
        except:
            tkinter.messagebox.showerror(title="Error Message",
                                         message="No Internet Connection\nCan't Locate you")

    def search_main(cityxyz):
        w1.attributes("-topmost", False)
        global searchcityforgrapha
        conn = sql.connect('data/ColorCode.db')
        cur = conn.cursor()
        try:
            global city
            global data
            global dataf
            city = cityxyz
            if city == "" or city == 'Please Select City.':
                resloco = requests.get('https://ipinfo.io/')
                data_locauto = resloco.json()
                city = data_locauto['city']
            url = 'http://api.waqi.info/feed/' + city + '/?token='
            api_key = 'aa47374836b21e3e050b3b9fb4131bfd74b1474a'
            main_url = url + api_key
            r = requests.get(main_url)
            dataall = r.json()
            status = dataall["status"]
            if status == "ok":
                # show data start
                data = dataall["data"]
                dataf = dataall["data"]
                try:
                    aqi = data['aqi']
                except:
                    aqi = 0

                try:
                    station = data['attributions'][0]['name']
                except:
                    station = "Not Available"

                try:
                    global cityloc; cityloc = data['city']['geo']
                except:
                    cityloc = "Not Available"

                try:
                    address = data['city']['name']
                except:
                    address = "Not Available"

                try:
                    iaqi = data['iaqi']
                except:
                    iaqi = "Not Available"

                try:
                    co = iaqi["co"]['v']
                except:
                    co = 0

                try:
                    dew = iaqi["dew"]['v']
                except:
                    dew = 0

                try:
                    no2 = iaqi["no2"]['v']
                except:
                    no2 = 0

                try:
                    o3 = iaqi["o3"]['v']
                except:
                    o3 = 0

                try:
                    pm10 = iaqi["pm10"]['v']
                except:
                    pm10 = 0

                try:
                    pm25 = iaqi["pm25"]['v']
                except:
                    pm25 = 0

                try:
                    date = data['time']['s'].split(" ")[0]
                except:
                    date = "Not Available"

                try:
                    time = data['time']['s'].split(" ")[1]
                except:
                    time = "Not Available"

                try:
                    dominentpol = data['dominentpol']
                except:
                    dominentpol = "aqi"

                global pollutant
                pollutant = {'aqi': {"v": aqi}, 'pm10': {"v": pm10}, 'pm25': {"v": pm25}, 'co': {"v": co},
                             'dew': {"v": dew}, 'no2': {"v": no2}, 'o3': {"v": o3}}
                for matter in pollutant.keys():
                    cur.execute("select * from color where pollutant == ? and lowlevel<=? and highlevel>=?;",
                                (matter, pollutant[matter]['v'], pollutant[matter]['v']))
                    data = cur.fetchall()
                    pollutant[matter]['color'] = data[0][3]
                    pollutant[matter]['status'] = data[0][4]
                conn.commit()
                w1lab1 = Label(w1, text="Air Pollution Data", font=("Helvetica", 14), bg=color)
                w1lab1.grid(row=3, column=0, columnspan=3, sticky="nsew")

                btsearchloc.config(text=" ")

                w1lab6 = Label(w1, text="City", font=("sans-serif", 8, 'bold'), bg=color)
                w1lab6.grid(row=4, column=0, sticky="nsew")

                w1lab2 = Label(w1, text="Station", font=("sans-serif", 8, 'bold'), bg=color)
                w1lab2.grid(row=5, column=0, sticky="nsew")

                w1lab3 = Label(w1, text="Address", font=("sans-serif", 8, 'bold'), bg=color)
                w1lab3.grid(row=6, column=0, sticky="nsew")

                w1lab4 = Label(w1, text="Date Of collection", font=("sans-serif", 8, 'bold'), bg=color)
                w1lab4.grid(row=7, column=0, sticky="nsew")

                w1lab5 = Label(w1, text="Time", font=("sans-serif", 8, 'bold'), bg=color)
                w1lab5.grid(row=8, column=0, sticky="nsew")

                w1lab6a = Label(w1, text=":\t" + city, font=("sans-serif", 10), bg=color)
                w1lab6a.grid(row=4, column=1, sticky="nsw")

                w1lab2a = Label(w1, text=":\t" + station, font=("sans-serif", 10), bg=color)
                w1lab2a.grid(row=5, column=1, sticky="nsw")

                w1lab3a = Label(w1, text=":\t" + address, font=("sans-serif", 10), bg=color)
                w1lab3a.grid(row=6, column=1, sticky="nsw")

                w1lab4a = Label(w1, text=":\t" + date, font=("sans-serif", 10), bg=color)
                w1lab4a.grid(row=7, column=1, sticky="nsw")

                w1lab5a = Label(w1, text=":\t" + time, font=("sans-serif", 10), bg=color)
                w1lab5a.grid(row=8, column=1, sticky="nsw")

                polllist = list(pollutant.keys())
                for i in range(len(polllist)):
                    w1labp = Label(w1, text=polllist[i], font=("sans-serif", 8, 'bold'), bg=color)
                    w1labp.grid(row=9 + i, column=0, sticky="nsew")

                for j in range(len(polllist)):
                    w1labp = Label(w1, text=":\t" + str(pollutant[polllist[j]]['v']), font=("sans-serif", 14, "bold"),
                                   bg=color, fg=pollutant[polllist[j]]['color'])
                    w1labp.grid(row=9 + j, column=1, sticky="nsw")

                w1labf = Label(w1, text="Air Pollution Forecast Data", font=("Helvetica", 15), bg=color)
                w1labf.grid(row=16, column=0, columnspan=3, sticky="nsew")

                # show notify
                try:
                    poll_status = pollutant[dominentpol]['status']
                except:
                    poll_status = pollutant['aqi']['status']

                if poll_status == "good":
                    icon_notify = 'info'
                    msz = "Air Quality In selected City is Good.\nYou Are safe to go Outside."
                elif poll_status == "satisfactory":
                    icon_notify = 'info'
                    msz = "Air Quality In selected City is Satisfactory.\nIf you have any seviour problem of respiration \nUse mask when going outside."
                elif poll_status == "medium":
                    icon_notify = 'info'
                    msz = "Air Quality In selected City is medium.\nGeneral public is not likely to be affected."
                elif poll_status == "poor":
                    icon_notify = 'info'
                    msz = "Air Quality In selected City is poor.\nEvery one may experiance problem\nUse Mask."
                elif poll_status == "very poor":
                    icon_notify = 'warning'
                    msz = "Air Quality In selected City is very poor.\nEach one will face health problem.\nDon't Go outside without Mask."
                elif poll_status == "dangerous":
                    icon_notify = 'warning'
                    msz = "Air Quality In selected City is Dangerous.\nYou Should not go Outside without any acceptable reason.\nUse Mask."
                else:
                    icon_notify = 'error'
                    msz = "Something went Wrong.Can't tell AQI information"
                w1.state('zoomed')

                global futuredata
                try:
                    futuredata1 = dataf['forecast']; futuredata = (futuredata1['daily'])
                except:
                    futuredata = {'Not Available': [
                        {'day': 'Not Available', 'avg': 'Not Available', 'min': 'Not Available',
                         'max': 'Not Available'}]}
                cno = 0
                for i in (futuredata.keys()):
                    cn = len(futuredata[i])
                    if cno < cn:
                        cno = cn
                        cols = [futuredata[i][index]["day"] for index in range(cn)]
                datecols = tuple(cols)
                columns_tree = ('Pollutant', 'parameter') + datecols
                forecast_tree = ttk.Treeview(w1)
                # deefining columns
                forecast_tree['columns'] = columns_tree
                # format columns
                forecast_tree.column('#0', width=40, minwidth=40)
                forecast_tree.column('Pollutant', width=60, minwidth=60, anchor=CENTER)
                forecast_tree.column('parameter', width=70, minwidth=70, anchor=CENTER)
                for col in datecols:
                    forecast_tree.column(col, width=80, minwidth=80, anchor=CENTER)
                # headings
                forecast_tree.heading("#0", text="SrNo.", anchor=CENTER)
                forecast_tree.heading("Pollutant", text="Pollutant.", anchor=CENTER)
                forecast_tree.heading("parameter", text="Parameter", anchor=CENTER)
                for col in datecols:
                    forecast_tree.heading(col, text=col, anchor=CENTER)
                # add data
                iid_count, sr_no_iid = 0, 1
                for key in futuredata.keys():
                    cn_temp = len(futuredata[key])
                    for para in ("avg", "max", "min"):
                        main = (key, para)
                        sencod_vals = []
                        for x in range(cn_temp):
                            sencod_vals.append(futuredata[key][x][para])
                        main_values = main + tuple(sencod_vals)
                        if len(main_values) != (cno + 2):
                            extra_add = []
                            for ext_a in range((cno + 2) - len(main_values)):
                                extra_add.append("Not Available")
                            main_values = main_values + tuple(extra_add)
                        iid_count += 1
                        if para == 'avg':
                            forecast_tree.insert(parent='', index='end', iid=iid_count, text=sr_no_iid,
                                                 values=main_values)
                            sr_no_iid += 1
                            next_iid = iid_count
                        else:
                            forecast_tree.insert(parent=next_iid, index='end', iid=iid_count, text=">",
                                                 values=main_values)
                # pack here
                forecast_tree.grid(row=17, column=0, columnspan=2, sticky='nsew')
                forecast_tree.config(height=sr_no_iid - 1)
                # y scrollbar vertical
                forecast_yscroll = ttk.Scrollbar(w1, orient="vertical", command=forecast_tree.yview)
                forecast_yscroll.grid(row=17, column=2, columnspan=1, sticky='ns')
                forecast_tree.configure(yscrollcommand=forecast_yscroll.set)
                # x horizontal scrollbar
                forecast_xscroll = ttk.Scrollbar(w1, orient="horizontal", command=forecast_tree.xview)
                forecast_xscroll.grid(row=sr_no_iid + 16, column=0, columnspan=2, sticky='ew')
                forecast_tree.configure(xscrollcommand=forecast_xscroll.set)
                searchcityforgrapha = True
                tkinter.messagebox.showinfo(title="Pollution information", message=msz, icon=icon_notify)
                w1.attributes("-topmost", True)
            elif status == "error":
                # error valid city/ internet
                tkinter.messagebox.showerror(title="Error Message",
                                             message="No Such City\nOR\nThere is No Weather station at that City")
        except:
            tkinter.messagebox.showerror(title="Error Message", message="No Internet Connection")
        searchcityforgrapha = True

    def show_today_graph():
        w1.attributes("-topmost", False)
        if searchcityforgrapha:
            pollutants = [i for i in pollutant.keys()]
            values = [pollutant[i]['v'] for i in pollutant.keys()]

            # Exploding the first slice
            explode = [0 for i in pollutants]
            mx = values.index(max(values))  # explode 1st slice
            explode[mx] = 0.1

            # Plot a pie chart
            plt.figure(figsize=(8, 6))
            plt.pie(values, labels=pollutants, explode=explode, autopct='%0.3f%%', shadow=True)
            plt.title('Air pollutants and their probable amount in atmosphere\ncity: ' + str(city))
            plt.axis('equal')
            plt.show()
        else:
            tkinter.messagebox.showerror(title="No city selected", message="Search for a city first.")
        w1.attributes("-topmost", True)

    def show_forecast_graph():
        w1.attributes("-topmost", False)
        if searchcityforgrapha:
            try:
                futuredata = dataf['forecast']['daily']
            except:
                futuredata = {'Data Not Available': [{'day': 'Not Available', 'avg': 0, 'min': 0, 'max': 0}]}
            dropshowfuture = list(futuredata.keys())
            dropshowfuture.insert(0, "Please Select")
            w1_f = Toplevel(w1)
            w1_f.title("Select Pollutant")
            w1_f.overrideredirect(1)
            w1_f.geometry("300x100")
            w1_f.rowconfigure(0, weight=1)
            w1_f.rowconfigure(1, weight=1)
            w1_f.rowconfigure(2, weight=1)
            w1_f.columnconfigure(0, weight=1)
            w1_f.columnconfigure(1, weight=1)
            w1_f.iconbitmap('data\\icon.ico')
            w1_f.attributes("-topmost", True)
            center_tk_window.center(w1, w1_f)
            labw1f = Label(w1_f, text="Select Pollutant To show its forecast.")
            labw1f.grid(row=0, padx=10, pady=10, column=0, columnspan=2, sticky='nsew')
            dropdownw1f = ttk.Combobox(w1_f, values=dropshowfuture)
            dropdownw1f.current(0)
            dropdownw1f.grid(row=1, padx=10, pady=10, column=0, sticky='nsew')

            def w1fsearch():
                futurepw1f = dropdownw1f.get()
                if futurepw1f not in dropshowfuture:
                    labw1fwar = Label(w1_f, text="Please Select...", fg="red")
                    labw1fwar.grid(row=2, padx=10, pady=10, column=0, columnspan=2, sticky='nsew')
                else:
                    if futurepw1f == "Please Select":
                        labw1fwar = Label(w1_f, text="Please Select...", fg="red")
                        labw1fwar.grid(row=2, padx=10, pady=10, column=0, columnspan=2, sticky='nsew')
                    else:
                        w1_f.destroy()
                        try:
                            gmain = futuredata[futurepw1f]
                            gpoll = futurepw1f
                        except:
                            gmain = [{'day': 'Not Available', 'avg': 0, 'min': 0, 'max': 0}]
                            gpoll = 'Data Not Available'
                        y_data = []
                        x_data = []
                        for i in gmain:
                            y_data.append(i['avg'])
                            x_data.append(i['day'])
                        plt.bar(x_data, y_data, width=0.5)
                        plt.rcParams["figure.figsize"] = [6.4, 4.8]
                        plt.xlabel('Date')
                        plt.ylabel('Pollutant values')
                        plt.title('Forecast graph representation : ' + gpoll)
                        plt.show()
                        try:
                            w1_f.destroy()
                        except:
                            pass

            w1fsearchbtn = Button(w1_f, text="Select", command=w1fsearch)
            w1fsearchbtn.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        else:
            tkinter.messagebox.showerror(title="No city selected", message="Search for a city first.")

    def show_forecast_graph_c():
        w1.attributes("-topmost", False)
        if searchcityforgrapha:
            w, mx = 0.2, 0

            def maker(data):
                if len(data) != minl:
                    for i in range(minl - len(data)):
                        data.append(0)
                return data

            for i in futuredata.keys():
                n = len(futuredata[i])
                if n > mx:
                    mx = n
                    mainp = i
            xlabel = [d['day'] for d in futuredata[mainp]]
            minl = len(xlabel)
            bar = [s for s in range(minl)]
            barx, w = bar, 0
            for i in futuredata.keys():
                data = []
                for j in futuredata[i]:
                    data.append(j['avg'])
                data = maker(data)
                bar = [i + w for i in bar]
                w = 0.2
                plt.bar(bar, data, w, label=i)
            plt.xlabel('date')
            plt.ylabel('value')
            bar2 = [p + w * 3 / 2 for p in barx]
            plt.title('data value')
            plt.xticks(bar2, xlabel)
            plt.legend()
            plt.show()
        else:
            tkinter.messagebox.showerror(title="No city selected", message="Search for a city first.")
        w1.attributes("-topmost", True)

    def show_map():
        w1.attributes("-topmost", False)
        if searchcityforgrapha:
            f = open("data\\map.html", "w")
            htmlmapfile1 = open("data\\maphtml1.txt", 'r')
            htmlmapdata1 = htmlmapfile1.read()
            htmlmapfile2 = open("data\\maphtml2.txt", 'r')
            htmlmapdata2 = htmlmapfile2.read()
            txt = htmlmapdata1 + str(cityloc) + htmlmapdata2
            f.write(txt)
            f.close()
            file_path1 = os.getcwd()
            urlfie = file_path1 + "\\data\\map.html"
            wb.open_new(urlfie)
        else:
            tkinter.messagebox.showerror(title="No city selected", message="Search for a city first.")

    menubar = Menu(w1, font=("Helvetica", 16))
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="More Functions", menu=filemenu)
    filemenu.add_command(label="Show Todays Graph", command=show_today_graph)
    fmenu = Menu(filemenu, tearoff=0)
    fmenu.add_command(label="Show Consoled forecast graph", command=show_forecast_graph_c)
    fmenu.add_command(label="Show Different forecast graph", command=show_forecast_graph)
    filemenu.add_cascade(label="Show forecast Graph", menu=fmenu)
    filemenu.add_command(label="Show Map", command=show_map)
    filemenu.add_command(label="Exit", command=clz1)
    w1.config(menu=menubar)
    # search btn
    btsearch = Button(w1, text='Search', command=search, compound=LEFT)
    btsearch.grid(row=2, column=1, columnspan=2, sticky='nsew', )
    global btsearchloc
    btsearchloc = Button(w1, bg=color, relief="flat", activebackground=color, bd=0, command=locsearch, compound=RIGHT)
    btsearchloc.config(image=locs2, compound=RIGHT)
    btsearchloc.grid(row=3, column=0, columnspan=3, sticky="ne")


# w1 main image
w1_main = Image.open(r'data/w1main1.png')
w1main1 = w1_main.resize((400, 160), Image.ANTIALIAS)
w1pic = ImageTk.PhotoImage(w1main1)
# loc image
locs = Image.open('data/loc_map.png')
locs1 = locs.resize((60, 60), Image.ANTIALIAS)
locs2 = ImageTk.PhotoImage(locs1)

bt1 = Button(win, text='Check Your City Pollution', command=citydata, bg='black', fg='white')
air1 = Image.open('data/air.png')
air1 = air1.resize((60, 60), Image.ANTIALIAS)
air2 = ImageTk.PhotoImage(air1)

bt1.config(image=air2, compound=LEFT)
bt1.grid(row=2, column=0, pady=10, padx=10, sticky='nsew')
searchw_cityforgrapha = False


# check your city weather
def cityweather():
    global w2_mainicon
    global w2main1
    global w2pic
    global fullall
    w2 = Toplevel(win)
    win.withdraw()
    w2.attributes("-topmost", True)
    cehckfull(w2)
    w2.title('Check Your City weather')
    w2.minsize(600, 330)
    w2.iconbitmap('data\\icon.ico')
    center_tk_window.center(win, w2)
    w2.columnconfigure(0, weight=1)
    w2.columnconfigure(1, weight=1)
    w2.columnconfigure(2, weight=0)
    w2.rowconfigure(0, weight=0)
    w2.rowconfigure(1, weight=1)
    w2.rowconfigure(3, weight=0)
    w2.rowconfigure(4, weight=1)
    w2.rowconfigure(5, weight=1)
    w2.rowconfigure(6, weight=1)
    w2.rowconfigure(7, weight=1)
    w2.rowconfigure(8, weight=1)
    w2.rowconfigure(9, weight=1)
    w2.rowconfigure(10, weight=1)
    w2.rowconfigure(11, weight=1)
    w2.rowconfigure(12, weight=1)
    w2.rowconfigure(13, weight=1)
    w2.rowconfigure(14, weight=1)
    w2.rowconfigure(15, weight=1)

    w2.config(bg=color)

    # close btn
    def clz1():
        w2.destroy()
        win.deiconify()

    btw2 = ttk.Button(w2, text='Close', command=clz1)
    btw2.grid(row=0, column=0, columnspan=3, sticky='NE')
    fullfunfscr(w2, 0, 0, csp=3)
    w2_mainicon = Image.open(r'data/w2iconmain1.png')
    w2main1 = w2_mainicon.resize((400, 160), Image.ANTIALIAS)
    w2pic = ImageTk.PhotoImage(w2main1)
    # w2 main image
    labelw2 = Label(w2, image=w2pic, bg=color)
    labelw2.grid(row=1, column=0, columnspan=3, sticky='nsew')
    # w2 w_city search entry
    w_cityentry = Entry(w2)
    w_cityentry.grid(row=2, column=0, sticky='nsew')

    # search cmd
    def search():
        w_city = w_cityentry.get()
        search_main(w_city)

    def locsearch():
        resloco = requests.get('https://ipinfo.io/')
        data_locauto = resloco.json()
        w_cityl = data_locauto['city']
        search_main(w_cityl)

    def search_main(w2_cityxyz):
        global w_city
        global weathericoin
        global weathericoin1
        global weather_iconinw2
        global w2dataall
        try:
            w_city = w2_cityxyz
            if w_city == "" or w_city == 'Please Select w_City.':
                resloco = requests.get('https://ipinfo.io/')
                data_locauto = resloco.json()
                w_city = data_locauto['city']
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            API_KEY = "b4085fdcb9101aa45b49cac926ac0d98"
            URL = BASE_URL + "q=" + w_city + "&appid=" + API_KEY
            try:
                rw2 = requests.get(URL)
                w2dataall = rw2.json()
                s = w2dataall['cod']
                if s == 404:
                    # print('eee')
                    status = 'error'
                else:
                    status = 'ok'
            except:
                status = "interror"
            if status == "ok":
                # show data start
                data_w2 = w2dataall
                global coord
                try:
                    coord = [data_w2['coord']['lon'], data_w2['coord']['lat']]
                except:
                    coord = [0, 0]
                try:
                    weather_main = data_w2['weather'][0]['main']
                except:
                    weather_main = 'NA'
                try:
                    weather_description = data_w2['weather'][0]['description']
                except:
                    weather_description = 'NA'
                global iconnamew2
                try:
                    iconnamew2 = data_w2['weather'][0]['icon']
                except:
                    iconnamew2 = '01d'
                try:
                    temp = data_w2['main']['temp']
                except:
                    temp = 0
                try:
                    humidity = data_w2['main']['humidity']
                except:
                    humidity = 0
                try:
                    visibility = data_w2['visibility']
                except:
                    visibility = 0
                try:
                    wind_speed = data_w2['wind']['speed']
                except:
                    wind_speed = 0
                try:
                    wind_deg = data_w2['wind']['deg']
                except:
                    wind_deg = 0
                try:
                    clouds = data_w2['clouds']['all']
                except:
                    clouds = 0
                try:
                    date = (str(datetime.fromtimestamp(data_w2['dt'])).split(' '))[0]
                except:
                    date = 'NA'
                try:
                    sunrise = (str(datetime.fromtimestamp(data_w2['sys']['sunrise'])).split(' '))[1]
                except:
                    sunrise = 'NA'
                try:
                    sunset = (str(datetime.fromtimestamp(data_w2['sys']['sunset'])).split(' '))[1]
                except:
                    sunset = 'NA'
                try:
                    wcity = data_w2['name']
                except:
                    wcity = w_city

                w2labmain = Label(w2, text="Weather Data", font=("Helvetica", 18, 'bold'), bg=color)
                w2labmain.grid(row=3, column=0, columnspan=3, sticky="nsew")

                w2lab0 = Label(w2, text=str(w_city), font=("sans-serif", 14, 'bold'), bg=color)
                w2lab0.grid(row=4, column=0, sticky="nsew")

                w2lab1 = Label(w2, text="Date", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab1.grid(row=5, column=0, sticky="nsew")

                w2lab2 = Label(w2, text="sunrise", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab2.grid(row=6, column=0, sticky="nsew")

                w2lab3 = Label(w2, text="sunset", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab3.grid(row=7, column=0, sticky="nsew")

                w2lab4 = Label(w2, text="Weather", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab4.grid(row=8, column=0, sticky="nsew")

                w2lab5 = Label(w2, text="Weather description", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab5.grid(row=9, column=0, sticky="nsew")

                w2lab6 = Label(w2, text="Temperature", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab6.grid(row=10, column=0, sticky="nsew")

                w2lab7 = Label(w2, text="Humidity", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab7.grid(row=11, column=0, sticky="nsew")

                w2lab8 = Label(w2, text="Visibility", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab8.grid(row=12, column=0, sticky="nsew")

                w2lab9 = Label(w2, text="Wind Speed", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab9.grid(row=13, column=0, sticky="nsew")

                w2lab10 = Label(w2, text="Wind Direction", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab10.grid(row=14, column=0, sticky="nsew")

                w2lab11 = Label(w2, text="Clouds", font=("sans-serif", 8, 'bold'), bg=color)
                w2lab11.grid(row=15, column=0, sticky="nsew")

                urllib.request.urlretrieve("http://openweathermap.org/img/w/" + iconnamew2 + ".png",
                                           "data\\iconweatherin.png")
                weathericoin = Image.open('data\\iconweatherin.png')
                weathericoin1 = weathericoin.resize((60, 60), Image.ANTIALIAS)
                weather_iconinw2 = ImageTk.PhotoImage(weathericoin1)

                w2lab0a = Label(w2, image=weather_iconinw2, font=("sans-serif", 10), bg=color)
                w2lab0a.grid(row=4, column=1, sticky="nsew")

                w2lab1a = Label(w2, text=":\t" + str(date), font=("sans-serif", 10), bg=color)
                w2lab1a.grid(row=5, column=1, sticky="nsw")

                w2lab2a = Label(w2, text=":\t" + str(sunrise), font=("sans-serif", 10), bg=color)
                w2lab2a.grid(row=6, column=1, sticky="nsw")

                w2lab3a = Label(w2, text=":\t" + str(sunset), font=("sans-serif", 10), bg=color)
                w2lab3a.grid(row=7, column=1, sticky="nsw")

                w2lab4a = Label(w2, text=":\t" + str(weather_main), font=("sans-serif", 10), bg=color)
                w2lab4a.grid(row=8, column=1, sticky="nsw")

                w2lab5a = Label(w2, text=":\t" + str(weather_description), font=("sans-serif", 10), bg=color)
                w2lab5a.grid(row=9, column=1, sticky="nsw")

                w2lab6a = Label(w2, text=":\t" + str(int(temp - 273.15)) + " C ," + str(temp) + " K",
                                font=("sans-serif", 10), bg=color)
                w2lab6a.grid(row=10, column=1, sticky="nsw")

                w2lab7a = Label(w2, text=":\t" + str(humidity) + ' %', font=("sans-serif", 10), bg=color)
                w2lab7a.grid(row=11, column=1, sticky="nsw")

                w2lab8a = Label(w2, text=":\t" + str(visibility) + " mi", font=("sans-serif", 10), bg=color)
                w2lab8a.grid(row=12, column=1, sticky="nsw")

                w2lab9a = Label(w2, text=":\t" + str(wind_speed) + " km/hr", font=("sans-serif", 10), bg=color)
                w2lab9a.grid(row=13, column=1, sticky="nsw")

                w2lab10a = Label(w2, text=":\t" + str(wind_deg) + " Degrees", font=("sans-serif", 10), bg=color)
                w2lab10a.grid(row=14, column=1, sticky="nsw")

                w2lab11a = Label(w2, text=":\t" + str(clouds) + " okta", font=("sans-serif", 10), bg=color)
                w2lab11a.grid(row=15, column=1, sticky="nsw")

                w2.geometry('400x700')
                global searchw_cityforgrapha
                searchw_cityforgrapha = True

            elif status == "error":
                # error valid w_city/ internet
                tkinter.messagebox.showerror(title="Error Message", message="No Such City")
            elif status == "interror":
                # error valid w_city/ internet
                tkinter.messagebox.showerror(title="Error Message", message="No Internet Connection")
        except:
            tkinter.messagebox.showerror(title="Error Message", message="No Internet Connection")

    def show_map():
        w2.attributes("-topmost", False)
        if searchw_cityforgrapha:
            mainmapw2url = "https://www.google.com/maps?ll=" + str(coord[1]) + ',' + str(
                coord[0]) + "&z=12&t=h&hl=en-US&gl=US&mapclient=embed"
            wb.open_new(mainmapw2url)
        else:
            tkinter.messagebox.showerror(title="No city selected", message="Search for a city first.")

    menubar = Menu(w2, font=("Helvetica", 16))
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="More Functions", menu=filemenu)
    filemenu.add_command(label="Show Map", command=show_map)
    filemenu.add_command(label="Exit", command=clz1)
    w2.config(menu=menubar)
    # search btn
    wbtsearch = Button(w2, text='Search', command=search, compound=LEFT)
    wbtsearch.grid(row=2, column=1, columnspan=2, sticky='nsew', )
    global btsearchloc
    wbtsearchloc = Button(w2, bg=color, relief="flat", activebackground=color, bd=0, command=locsearch, compound=RIGHT)
    wbtsearchloc.config(image=locs2, compound=RIGHT)
    wbtsearchloc.grid(row=3, column=2, columnspan=2, sticky='ne')


bt2 = Button(win, text='Check Your City weather', command=cityweather, bg='black', fg='white')
weather1 = Image.open('data/weather.png')
weather1 = weather1.resize((60, 60), Image.ANTIALIAS)
weather2 = ImageTk.PhotoImage(weather1)
bt2.config(image=weather2, compound=LEFT)
bt2.grid(row=3, column=0, pady=10, padx=10, sticky='nsew')


# send data on mail
def maildata():
    global fullall
    w3 = Toplevel(win)
    win.withdraw()
    w3.title('Send City Data on Mail')
    w3.config(bg=color)
    w3.attributes("-topmost", True)
    w3.minsize(530, 330)
    w3.iconbitmap('data\\icon.ico')
    center_tk_window.center(win, w3)
    w3.columnconfigure(0, weight=1)
    w3.rowconfigure(0, weight=0)
    w3.rowconfigure(1, weight=1)
    w3.rowconfigure(2, weight=1)
    w3.rowconfigure(3, weight=1)
    w3.rowconfigure(4, weight=1)
    cehckfull(w3)

    def clz3():
        w3.destroy();
        win.deiconify()

    btw3 = ttk.Button(w3, text='Close', command=clz3)
    btw3.grid(row=0, column=0, sticky="ne")
    fullfunfscr(w3, 0, 0)
    labimgw3 = Label(w3, image=w3_pic, bg=color)
    labimgw3.grid(row=1, padx=10, pady=10, column=0, sticky="nsew")

    def mailpollution():
        global fullall
        w3_p = Toplevel(w3)
        w3.withdraw()
        w3_p.title("Send Pollution Data on Mail")
        w3_p.attributes("-topmost", True)
        w3_p.minsize(530, 300)
        w3_p.config(bg=color)
        w3_p.iconbitmap('data\\icon.ico')
        center_tk_window.center(w3, w3_p)
        w3_p.columnconfigure(0, weight=1)
        w3_p.columnconfigure(1, weight=1)
        w3_p.columnconfigure(2, weight=1)
        w3_p.rowconfigure(0, weight=0)
        w3_p.rowconfigure(1, weight=1)
        w3_p.rowconfigure(2, weight=1)
        w3_p.rowconfigure(3, weight=1)
        w3_p.rowconfigure(4, weight=1)
        w3_p.rowconfigure(5, weight=1)
        w3_p.rowconfigure(6, weight=1)
        w3_p.rowconfigure(7, weight=1)
        cehckfull(w3_p)

        def w3pclose():
            w3_p.destroy();
            w3.deiconify()

        clbtn = ttk.Button(w3_p, text="Close", command=w3pclose)
        clbtn.grid(row=0, column=0, columnspan=3, sticky="ne")
        fullfunfscr(w3_p, 0, 0, csp=3)

        labicon = Label(w3_p, image=w3_p_pic, bg=color)
        labicon.grid(row=1, padx=10, pady=10, column=0, columnspan=3, sticky='nsew')
        labec = Label(w3_p, text="Enter City:", bg=color)
        labec.grid(row=3, padx=10, pady=10, column=0, sticky='nsew')
        fcity = open('data\\CityList.txt', 'r')
        citynames = (fcity.read().split(","))
        citylist = ['Please Select City.'] + citynames
        dropdown = ttk.Combobox(w3_p, values=citylist)
        dropdown.current(0)
        dropdown.grid(row=3, padx=10, pady=10, column=1, sticky='ew', columnspan=2)

        def mailpollsearch():
            citymp = str(dropdown.get())
            url = 'http://api.waqi.info/feed/' + citymp + '/?token='
            api_key = 'aa47374836b21e3e050b3b9fb4131bfd74b1474a'
            main_url = url + api_key
            try:
                r = requests.get(main_url)
                dataall = r.json()
                status = dataall["status"]
            except:
                w3_p.attributes("-topmost", False)
                status = "nonet"
                messagebox.showerror("Network Error", "No internet Connection :(")
                w3_p.attributes("-topmost", True)
            if status == "ok":
                labshow = Label(w3_p, text="City Found \t*Data ready to send", bg=color, fg="green")
                labshow.grid(row=5, padx=10, pady=10, column=0, columnspan=2, sticky='nsew')

                w3_p.geometry('400x700')
                saveboolvar = BooleanVar(w3_p, False)
                secbn = Checkbutton(w3_p, text="Save Mail ID", bg=color, variable=saveboolvar)
                secbn.grid(row=5, padx=10, pady=10, column=2, columnspan=2, sticky='nsew')

                labmail = Label(w3_p, text="Enter YourEmail ID:", bg=color)
                labmail.grid(row=6, padx=10, pady=10, column=0, sticky='ew')

                savedmail = open('data\\mailsaved.txt', 'r')
                mailids = (savedmail.read().split('\n'))

                maillist = [''] + mailids
                getmail = ttk.Combobox(w3_p, values=maillist)
                getmail.current(0)
                getmail.grid(row=6, padx=10, pady=10, column=1, columnspan=2, sticky='ew')

                def sendpollmail():
                    mailid = str(getmail.get())
                    if saveboolvar.get():
                        savemail(mailid)
                    datareq = dataall
                    w3_p.attributes("-topmost", False)
                    mailpcon = messagebox.askokcancel("Mail Service", "Please conform the mailid.\n" + str(mailid),
                                                      icon="warning")
                    w3_p.attributes("-topmost", True)

                    # loadingw.deiconify()
                    if mailpcon:
                        mailpollsendstatus = MailCity(mailid, datareq, str(dropdown.get()))
                    else:
                        mailpollsendstatus = False
                    if mailpollsendstatus:
                        # loadingw.withdraw()
                        w3_p.attributes("-topmost", False)
                        tkinter.messagebox.showinfo(title="Mail Report", message="Mail Sent Sucessfully.")
                    else:
                        # loadingw.withdraw()
                        w3_p.attributes("-topmost", False)
                        tkinter.messagebox.showerror(title="Mail Report", message="Mail not send\nPlease try again.")
                    w3_p.attributes("-topmost", True)

                sendmail = Button(w3_p, text="Send Data on Mail", command=sendpollmail)
                sendmail.grid(row=7, padx=10, pady=10, column=1, sticky='nse')
            elif status == "nonet":
                labshow = Label(w3_p, text="NO Internet Availabel", bg=color, fg="red")
                labshow.grid(row=5, column=0, columnspan=3, sticky='nsew')
                w3_p.after(4000, labshow.destroy)
            else:
                labshow = Label(w3_p, text="City NOT Found.\tPlease Check", bg=color, fg="red")
                labshow.grid(row=5, column=0, columnspan=3, sticky='nsew')
                w3_p.after(4000, labshow.destroy)

        searchbtnmail = Button(w3_p, text="Search", command=mailpollsearch)
        searchbtnmail.grid(row=4, padx=10, pady=10, column=1, sticky='n', columnspan=2)

    btmailpoll = Button(w3, text="Send Pollution Data", command=mailpollution)
    btmailpoll.grid(row=2, padx=10, pady=10, column=0, sticky='nsew')

    def mailweather():
        global fullall
        w3_w = Toplevel(w3)
        w3.withdraw()
        w3_w.title("Send Weather Data on Mail")
        w3_w.attributes("-topmost", True)
        w3_w.minsize(530, 300)
        w3_w.config(bg=color)
        w3_w.iconbitmap('data\\icon.ico')
        center_tk_window.center(w3, w3_w)
        w3_w.columnconfigure(0, weight=1)
        w3_w.columnconfigure(1, weight=1)
        w3_w.columnconfigure(2, weight=1)
        w3_w.rowconfigure(0, weight=0)
        w3_w.rowconfigure(1, weight=1)
        w3_w.rowconfigure(2, weight=1)
        w3_w.rowconfigure(3, weight=1)
        w3_w.rowconfigure(4, weight=1)
        w3_w.rowconfigure(5, weight=1)
        w3_w.rowconfigure(6, weight=1)
        w3_w.rowconfigure(7, weight=1)
        w3_w.rowconfigure(8, weight=1)
        cehckfull(w3_w)

        def w3wclose():
            w3_w.destroy();
            w3.deiconify()

        clbtn = ttk.Button(w3_w, text="Close", command=w3wclose)
        clbtn.grid(row=0, column=0, columnspan=3, sticky="ne")
        fullfunfscr(w3_w, 0, 0, csp=3)
        labicon = Label(w3_w, image=w3_w_pic, bg=color)
        labicon.grid(row=1, padx=10, pady=10, column=0, columnspan=3, sticky='nsew')
        labec = Label(w3_w, text="Enter City:", bg=color)
        labec.grid(row=3, padx=10, pady=10, column=0, sticky='nsew')
        s = open('data\\savedwcity.txt', 'w')
        s.close()
        savedcity = open('data\\savedwcity.txt', 'r')
        cities = (savedcity.read().split('\n'))

        citylst = [''] + cities
        citywmailentry = ttk.Combobox(w3_w, values=citylst)
        citywmailentry.current(0)
        citywmailentry.grid(row=3, padx=10, pady=10, column=1, sticky='nsew', columnspan=2)

        def mailwsearch():
            citywm = str(citywmailentry.get())
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            API_KEY = "b4085fdcb9101aa45b49cac926ac0d98"
            URL = BASE_URL + "q=" + citywm + "&appid=" + API_KEY
            savewcity(citywm)
            try:
                rw2 = requests.get(URL)
                w2dataall = rw2.json()
                s = str(w2dataall['cod'])
            except:
                s = "nonet"
                w3_w.attributes("-topmost", False)
                messagebox.showerror("Network Error", "No internet Connection :(")
                w3_w.attributes("-topmost", True)
            if s == '404':
                status = 'error'
            else:
                status = 'ok'
            if status == 'ok':
                w3_w.geometry('400x700')
                labshow = Label(w3_w, text="City Found \t*Data ready to send", bg=color, fg="green")
                labshow.grid(row=5, padx=10, pady=10, column=0, columnspan=2, sticky='nsew')
                saveboolvar = BooleanVar(w3_w, False)
                secbn = Checkbutton(w3_w, text="Save Mail ID", bg=color, variable=saveboolvar)
                secbn.grid(row=5, padx=10, pady=10, column=2, columnspan=2, sticky='nsew')
                labmail = Label(w3_w, text="Enter YourEmail ID:", bg=color)
                labmail.grid(row=6, padx=10, pady=10, column=0, sticky='ew')
                savedmail = open('data\\mailsaved.txt', 'r')
                mailids = (savedmail.read().split('\n'))
                maillist = [''] + mailids
                getmail = ttk.Combobox(w3_w, values=maillist)
                getmail.current(0)
                getmail.grid(row=6, padx=10, pady=10, column=1, columnspan=2, sticky='ew')
                citymw = str(citywmailentry.get())

                def sendwmail():
                    mailid = str(getmail.get())
                    if saveboolvar.get():
                        savemail(mailid)
                    w3_w.attributes("-topmost", False)
                    mailwcon = messagebox.askokcancel("Mail Service", "Please conform the mailid.\n" + str(mailid),
                                                      icon="warning")
                    w3_w.attributes("-topmost", True)
                    lodlab = Label(w3_w, text="Sending Mail...", bg=color)
                    lodlab.grid(row=8, padx=5, pady=5, column=0, columnspan=3, sticky='nsew')
                    if mailwcon:
                        mailwsendstatus = MailWeather(citymw, mailid, w2dataall)
                    else:
                        mailwsendstatus = False
                    if mailwsendstatus:
                        w3_w.attributes("-topmost", False)
                        tkinter.messagebox.showinfo(title="Mail Report", message="Mail Sent Sucessfully.")
                        lodlab.destroy()
                    else:
                        w3_w.attributes("-topmost", False)
                        tkinter.messagebox.showerror(title="Mail Report", message="Mail not send\nPlease try again.")
                        lodlab.destroy()
                    w3_w.attributes("-topmost", True)

                sendmail = Button(w3_w, text="Send Data on Mail", command=sendwmail)
                sendmail.grid(row=7, padx=10, pady=10, column=1, sticky='nse')
            elif status == "nonet":
                labshow = Label(w3_w, text="NO Internet Availabel", bg=color, fg="red")
                labshow.grid(row=5, column=0, columnspan=3, sticky='nsew')
                w3_w.after(4000, labshow.destroy)
            else:
                labew = Label(w3_w, text="No such city *Please Check", bg=color, fg='red')
                labew.grid(row=5, padx=10, pady=10, columnspan=3, column=0, sticky='nsew')
                w3_w.after(5000, labew.destroy)

        searchbtnmail = Button(w3_w, text="Search", command=mailwsearch)
        searchbtnmail.grid(row=4, padx=10, pady=10, column=1, sticky='n', columnspan=2)

    btmailw = Button(w3, text="Send Weather Data", command=mailweather)
    btmailw.grid(row=3, padx=10, pady=10, column=0, sticky='nsew')


w3_p_main = Image.open(r'data/mailairicon.png')
w3_p_main1 = w3_p_main.resize((400, 160), Image.ANTIALIAS)
w3_p_pic = ImageTk.PhotoImage(w3_p_main1)
w3_w_main = Image.open(r'data/mailweathericon.png')
w3_w_main1 = w3_w_main.resize((400, 160), Image.ANTIALIAS)
w3_w_pic = ImageTk.PhotoImage(w3_w_main1)
w3_main = Image.open(r'data/mailicos.png')
w3_main1 = w3_main.resize((400, 160), Image.ANTIALIAS)
w3_pic = ImageTk.PhotoImage(w3_main1)
bt3 = Button(win, text='Send City Data on Mail', command=maildata, bg='black', fg='white')
mail1 = Image.open('data/mail.png')
mail1 = mail1.resize((60, 60), Image.ANTIALIAS)
mail2 = ImageTk.PhotoImage(mail1)
bt3.config(image=mail2, compound=LEFT)
bt3.grid(row=4, column=0, pady=10, padx=10, sticky='nsew')


# more information
def moreinfo():
    w4 = Toplevel(win)
    w4.title('More information on Pollution')
    w4.iconbitmap('data\\icon.ico')
    w4.attributes("-topmost", True)
    w4.geometry('470x600')
    w4.config(bg=color)
    center_tk_window.center(win, w4)
    w4.rowconfigure(0, weight=0)

    def makeweight1(a, b):
        for rowno in range(a, b):
            w4.rowconfigure(rowno, weight=1)

    w4.columnconfigure(0, weight=1)
    w4.columnconfigure(1, weight=2)
    w4.columnconfigure(2, weight=2)
    w4lmain = Label(w4, text="More Information", bg=color, bd=5, fg="black", font=("Helvetica", 16))
    w4lmain.grid(row=1, column=0, sticky="nsew", columnspan=3)
    a = 2
    # pollution info
    w4la = Label(w4, text="More Information about Pollution", bg=color, bd=5, font=("Helvetica", 12))
    w4la.grid(row=a, column=0, sticky="nsw", columnspan=3)

    def showa():
        w4la1 = Label(w4, text="1. Enter Or Select Your City in Box and click search.", bg=color, bd=5, fg="black")
        w4la1.grid(row=a + 1, column=1, sticky="nsw", columnspan=2)
        w4la2 = Label(w4,
                      text="2. You can also locate your nearest city by clicking on location icon below the serch button.",
                      bg=color, bd=5, fg="black")
        w4la2.grid(row=a + 2, column=1, sticky="nsw", columnspan=2)
        w4la3 = Label(w4,
                      text="3. After that you will be notified by your city's pollution information and Advice about health.",
                      bg=color, bd=5, fg="black")
        w4la3.grid(row=a + 3, column=1, sticky="nsw", columnspan=2)
        w4la4 = Label(w4, text="4. After that you can see all pollution data and forcast of next week.", bg=color, bd=5,
                      fg="black")
        w4la4.grid(row=a + 4, column=1, sticky="nsw", columnspan=2)
        w4la5 = Label(w4, text="5. Now you can access more functions in top left corner to see Graphs and Map.",
                      bg=color, bd=5, fg="black")
        w4la5.grid(row=a + 5, column=1, sticky="nsw", columnspan=2)

    bta = ttk.Button(w4, text="show", command=showa)
    bta.grid(row=a, column=0, sticky="nse", columnspan=3)
    b = a + 6
    w4lb = Label(w4, text="More Information about Whether", bg=color, bd=5, fg="black", font=("Helvetica", 12))
    w4lb.grid(row=b, column=0, sticky="nsw", columnspan=3)

    def showb():
        w4lb1 = Label(w4,
                      text="1. Enter Your city in text box given and click on search or click on location icon to locate automatically.",
                      bg=color, bd=5, fg="black")
        w4lb1.grid(row=b + 1, column=1, sticky="nsw", columnspan=2)
        w4lb2 = Label(w4, text="2. You will see all weather information of city you entered.", bg=color, bd=5,
                      fg="black")
        w4lb2.grid(row=b + 2, column=1, sticky="nsw", columnspan=2)
        w4lb3 = Label(w4, text="3. Now you can access more functions in top left corner to see map.", bg=color, bd=5,
                      fg="black")
        w4lb3.grid(row=b + 3, column=1, sticky="nsw", columnspan=2)
        w4lb4 = Label(w4, text="4. Click on close button to go to main screen.", bg=color, bd=5, fg="black")
        w4lb4.grid(row=b + 4, column=1, sticky="nsw", columnspan=2)

    btb = ttk.Button(w4, text="show", command=showb)
    btb.grid(row=b, column=0, sticky="nse", columnspan=3)
    c = b + 5
    w4lc = Label(w4, text="More Information about sending info on your mail ...", bg=color, bd=5, fg="black",
                 font=("Helvetica", 12))
    w4lc.grid(row=c, column=0, sticky="nsw", columnspan=3)

    def showc():
        w4lc1 = Label(w4, text="1. Click On the required option to send data on mail.", bg=color, bd=5, fg="black")
        w4lc1.grid(row=c + 1, column=1, sticky="nsw", columnspan=2)
        w4lc2 = Label(w4, text="2. Enter city to send data and click search.", bg=color, bd=5, fg="black")
        w4lc2.grid(row=c + 2, column=1, sticky="nsw", columnspan=2)
        w4lc3 = Label(w4, text="3. If every thing works correctly Enter your e-mail and click send data.", bg=color,
                      bd=5, fg="black")
        w4lc3.grid(row=c + 3, column=1, sticky="nsw", columnspan=2)
        w4lc4 = Label(w4, text="4. You can also tick on Save mail id to save your e-mail id in your local storage.",
                      bg=color, bd=5, fg="black")
        w4lc4.grid(row=c + 4, column=1, sticky="nsw", columnspan=2)

    w4ld = Label(w4,
                 text="If you still get error check your internet connection OR refer our website https://prathameshks.github.io/APWProject/",
                 bg=color, wraplength=450, fg="black", font=("Helvetica", 12))
    w4ld.grid(row=c + 6, column=0, sticky="nsw", columnspan=3)
    w4ld.bind("<Button-1>", lambda e: openmyweb("https://prathameshks.github.io/APWProject/"))
    btc = ttk.Button(w4, text="show", command=showc)
    btc.grid(row=c, column=0, sticky="nse", columnspan=3)
    makeweight1(2, c + 6)

    # close btn
    # close btn
    def clz4():
        w4.destroy();
        win.deiconify()

    btw4 = ttk.Button(w4, text='Close', command=clz4)
    btw4.grid(row=0, column=1, columnspan=2, sticky='NE')


def openmyweb(url): 
    win.iconify()
    root.iconify()
    wb.open_new_tab(url)


bt4 = Button(win, text='More information on Pollution', command=moreinfo, bg='black', fg='white')
info1 = Image.open('data/info.png')
info1 = info1.resize((60, 60), Image.ANTIALIAS)
info2 = ImageTk.PhotoImage(info1)
bt4.config(image=info2, compound=LEFT)
bt4.grid(row=5, column=0, pady=10, padx=10, sticky='nsew')
# copyright labels
lab2 = Label(win, text='\xa9 copyright : OpenWeather \x26 aqicn.org', wraplength=500, bg=color)
lab2.grid(row=6, column=0, pady=10, padx=10, sticky='nsew')
lab3 = Label(win, text='Click Here To open Our Website https://prathameshks.github.io/APWProject/', cursor="hand2", wraplength=500,
             bg=color)
lab3.grid(row=7, column=0, pady=10, padx=10, sticky='nsew')

lab3.bind("<Button-1>", lambda e: openmyweb("https://prathameshks.github.io/APWProject/"))


def MailWeather(w_city, mailid, data_w2):
    try:
        try:
            weather_main = data_w2['weather'][0]['main']
        except:
            weather_main = 'NA'
        try:
            weather_description = data_w2['weather'][0]['description']
        except:
            weather_description = 'NA'
        try:
            icon = data_w2['weather'][0]['icon']
        except:
            icon = '01d'
        try:
            temp = data_w2['main']['temp']
        except:
            temp = 0
        try:
            humidity = data_w2['main']['humidity']
        except:
            humidity = 0
        try:
            visibility = data_w2['visibility']
        except:
            visibility = 0
        try:
            wind_speed = data_w2['wind']['speed']
        except:
            wind_speed = 0
        try:
            wind_deg = data_w2['wind']['deg']
        except:
            wind_deg = 0
        try:
            clouds = data_w2['clouds']['all']
        except:
            clouds = 0
        try:
            date = (str(datetime.fromtimestamp(data_w2['dt'])).split(' '))[0]
        except:
            date = 'NA'
        try:
            sunrise = (str(datetime.fromtimestamp(data_w2['sys']['sunrise'])).split(' '))[1]
        except:
            sunrise = 'NA'
        try:
            sunset = (str(datetime.fromtimestamp(data_w2['sys']['sunset'])).split(' '))[1]
        except:
            sunset = 'NA'
        try:
            wcity = data_w2['name']
        except:
            wcity = w_city
        weathermaildata = "Weather Data\n" + "\nCity :\t" + w_city + "\nDate :\t" + str(date) + "\nsunrise :\t" + str(
            sunrise) + "\nsunset :\t" + str(sunset) + "\nWeather :\t" + str(
            weather_main) + "\nWeather description :\t" + str(weather_description) + "\nTemperature :\t" + str(
            int(temp - 273.15)) + " C ," + str(temp) + " K" + "\nHumidity :\t" + str(
            humidity) + ' %' + "\nVisibility :\t" + str(visibility) + " mi" + "\nWind Speed :\t" + str(
            wind_speed) + " km/hr" + "\nWind Direction :\t" + str(wind_deg) + " Degrees" + "\nClouds :\t" + str(
            clouds) + " okta"
        urllib.request.urlretrieve("http://openweathermap.org/img/w/" + icon + ".png", "data\\iconweatherin.png")
        passfile = open('data\\mailpassword.pydb', "r")
        emailfile = open('data\\mailid.pydb', "r")
        EMAIL_ADDRESS = emailfile.read()
        EMAIL_PASSWORD = passfile.read()
        weathermailu = EmailMessage()
        weathermailu['Subject'] = 'Sending Weather information of your city.'
        weathermailu['From'] = EMAIL_ADDRESS
        weathermailu['To'] = str(mailid)
        weathermailu.set_content(weathermaildata)
        f = open("data\\iconweatherin.png", 'rb')
        file_data = f.read()
        file_type = 'png'
        file_name = 'Weather icon'
        weathermailu.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(weathermailu)
        return True
    except:
        return False


def MailCity(mailidto, dataall, city):
    try:
        data = dataall["data"]
        try:
            aqi = data['aqi']
        except:
            aqi = 0
        try:
            station = data['attributions'][0]['name']
        except:
            station = "Not Available"
        try:
            global cityloc; cityloc = data['city']['geo']
        except:
            cityloc = "Not Available"
        try:
            address = data['city']['name']
        except:
            address = "Not Available"
        try:
            iaqi = data['iaqi']
        except:
            iaqi = "Not Available"
        try:
            co = iaqi["co"]['v']
        except:
            co = 0
        try:
            dew = iaqi["dew"]['v']
        except:
            dew = 0
        try:
            no2 = iaqi["no2"]['v']
        except:
            no2 = 0
        try:
            o3 = iaqi["o3"]['v']
        except:
            o3 = 0
        try:
            pm10 = iaqi["pm10"]['v']
        except:
            pm10 = 0
        try:
            pm25 = iaqi["pm25"]['v']
        except:
            pm25 = 0
        try:
            date = data['time']['s'].split(" ")[0]
        except:
            date = "Not Available"
        try:
            time = data['time']['s'].split(" ")[1]
        except:
            time = "Not Available"
        try:
            dominentpol = data['dominentpol']
        except:
            dominentpol = "aqi"
        message_poll_mail = "Air Pollution Data\n" + "City :\t" + str(city) + "\nStation :\t" + str(
            station) + "\nAddress :\t" + str(address) + "\nDate Of collection :\t" + str(date) + "\nTime :\t" + str(
            time) + '\naqi :\t' + str(aqi) + '\npm10 :\t' + str(pm10) + '\npm2.5 :\t' + str(pm25) + '\nco :\t' + str(
            co) + '\ndew :\t' + str(dew) + '\nno2 :\t' + str(no2) + '\no3 :\t' + str(
            o3) + '\nAir Quality Status :\t' + str(aqi)
        pollutant = {'aqi': {"v": aqi}, 'pm10': {"v": pm10}, 'pm25': {"v": pm25}, 'co': {"v": co}, 'dew': {"v": dew},
                     'no2': {"v": no2}, 'o3': {"v": o3}}
        pollutants = [i for i in pollutant.keys()]
        values = [pollutant[i]['v'] for i in pollutant.keys()]
        explode = [0 for i in pollutants]
        mx = values.index(max(values))  # explode 1st slice
        explode[mx] = 0.1
        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=pollutants, explode=explode, autopct='%0.3f%%', shadow=True)
        plt.title('Air pollutants and their probable amount in atmosphere\ncity: ' + str(city))
        plt.axis('equal')
        plt.savefig('data\\pie_chart_pollution.png', transparent=True)
        passfile = open('data\\mailpassword.pydb', "r")
        emailfile = open('data\\mailid.pydb', "r")
        EMAIL_ADDRESS = emailfile.read()
        EMAIL_PASSWORD = passfile.read()
        pollmailu = EmailMessage()
        pollmailu['Subject'] = 'Sending Air Pollution information for your city.'
        pollmailu['From'] = EMAIL_ADDRESS
        pollmailu['To'] = str(mailidto)
        pollmailu.set_content(message_poll_mail)
        f = open("data\\pie_chart_pollution.png", 'rb')
        file_data = f.read()
        file_type = 'png'
        file_name = 'GRAPH OF POLLUTION'
        pollmailu.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(pollmailu)
        return True
    except:
        return False


btnclosebg = Button(root, text="Close BackGround", command=lambda: root.withdraw(), width=17, height=1)
btnclosebg.grid(row=0, column=0, padx=10, pady=10, sticky='ne')


def rfscreen():
    root.attributes("-fullscreen", True)


def rfscreenout():
    root.attributes("-fullscreen", False)

def mainend():
    root.destroy()
    exit()

btf = Button(root, text='Fullscreen', command=rfscreen, width=17, height=1)
btf.grid(row=0, column=0, sticky='NE', pady=50, padx=10)
btfn = Button(root, text='Exit Fullscreen', command=rfscreenout, width=17, height=1)
btfn.grid(row=0, column=0, sticky='Ne', pady=90, padx=10)
btnexit = Button(root, text='End App', command=mainend, width=17, height=1)
btnexit.grid(row=0, column=0, sticky='Ne', pady=130, padx=10)


def savemail(email):
    filemaila = open("data\\mailsaved.txt", "a")
    filemailr = open("data\\mailsaved.txt", "r")
    mailidlst = filemailr.read().split("\n")
    if email not in mailidlst:
        filemaila.write(str(email) + '\n')
    filemaila.close()
    filemailr.close()


def savewcity(city):
    filemailca = open("data\\savedwcity.txt", "a")
    filemailcr = open("data\\savedwcity.txt", "r")
    mailidlst = filemailcr.read().split("\n")
    if city not in mailidlst:
        filemailca.write(str(city) + '\n')
    filemailca.close()
    filemailcr.close()


root.mainloop()

