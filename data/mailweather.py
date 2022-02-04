import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage 

def MailWeather(w_city,mailid):
    try:
        BASE_URL = "https://api.openweathermap.org/data_w2/2.5/weather?"
        API_KEY = "b4085fdcb9101aa45b49cac926ac0d98"

        URL = BASE_URL + "q=" + w_city + "&appid=" + API_KEY
        req = requests.get(URL)
        data_w2= req.json()

        try:
            weather_main=data_w2['weather'][0]['main']
        except:
            weather_main='NA'
        try:
            weather_description=data_w2['weather'][0]['description']
        except:
            weather_description='NA'
        try:
            icon=data_w2['weather'][0]['icon']
        except:
            icon='01d'
        try:
            temp=data_w2['main']['temp']
        except:
            temp=0
        try:
            humidity=data_w2['main']['humidity']
        except:
            humidity=0
        try:
            visibility=data_w2['visibility']
        except:
            visibility=0
        try:
            wind_speed=data_w2['wind']['speed']
        except:
            wind_speed=0
        try:
            wind_deg=data_w2['wind']['deg']
        except:
            wind_deg=0
        try:
            clouds=data_w2['clouds']['all']
        except:
            clouds=0
        try:
            date=(str(datetime.fromtimestamp(data_w2['dt'])).split(' '))[0]
        except:
            date='NA'
        try:
            sunrise=(str(datetime.fromtimestamp(data_w2['sys']['sunrise'])).split(' '))[1]
        except:
            sunrise='NA'
        try:
            sunset=(str(datetime.fromtimestamp(data_w2['sys']['sunset'])).split(' '))[1]
        except:
            sunset='NA'
        try:
            wcity=data_w2['name']
        except:
            wcity=w_city
        weathermaildata="Weather Data\n"+"\nCity :\t"+w_city+"\nDate :\t"+str(date)+"\nsunrise :\t"+str(sunrise)+"\nsunset :\t"+str(sunset)+"\nWeather :\t"+ str(weather_main)+"\nWeather description :\t"+ str(weather_description)+"\nTemperature :\t"+ str(int(temp-273.15))+" C ,"+ str(temp) +" K" +"\nHumidity :\t"+ str(humidity)+' %'+"\nVisibility :\t"+ str(visibility)+" mi"+"\nWind Speed :\t"+ str(wind_speed)+" km/s"+"\nWind Direction :\t"+ str(wind_deg)+" Degrees"+"\nClouds :\t"+ str(clouds)+" okta" 

        urllib.request.urlretrieve("http://openweathermap.org/img/w/" + icon + ".png", "data\\iconweatherin.png")
        # weathericoin = Image.open('data\\iconweatherin.png')

        passfile=open('data\\pygraph.pydb',"r")
        EMAIL_ADDRESS = 'airprojectjnv2020@gmail.com'
        EMAIL_PASSWORD = passfile.read()
        weathermailu = EmailMessage()
        weathermailu['Subject'] = 'Sending Weather information of your city.'
        weathermailu['From'] = EMAIL_ADDRESS
        weathermailu['To'] = str(mailid)

        weathermailu.set_content(weathermaildata)
        f=open("data\\iconweatherin.png",'rb')
        file_data=f.read()
        file_type='png'
        file_name='Weather icon'
        weathermailu.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
            
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(weathermailu)
        return True
    except:
        return False