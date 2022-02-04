import smtplib
from email.message import EmailMessage
import matplotlib.pyplot as plt
from email.mime.image import MIMEImage

def MailCity(mailidto,dataall,city):
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
            global cityloc
            cityloc = data['city']['geo']

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

        message_poll_mail="Air Pollution Data\n"+"City :\t"+str(city)+"\nStation :\t"+str(station)+"\nAddress :\t"+str(address)+"\nDate Of collection :\t"+str(date)+"\nTime :\t"+str(time)+'\naqi :\t'+str(aqi)+'\npm10 :\t'+str(pm10)+'\npm2.5 :\t'+str(pm25)+'\nco :\t'+str(co)+'\ndew :\t'+str(dew)+'\nno2 :\t'+str(no2)+'\no3 :\t'+str(o3)+'\nAir Quality Status :\t'+str(aqi)

        pollutant={'aqi':{"v":aqi},'pm10':{"v":pm10},'pm25':{"v":pm25},'co':{"v":co},'dew':{"v":dew},'no2':{"v":no2},'o3':{"v":o3}}
                    
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
        plt.savefig('data\\pie_chart_pollution.png',transparent=True)

        passfile=open('data\\pygraph.pydb',"r")
        EMAIL_ADDRESS = 'airprojectjnv2020@gmail.com'
        EMAIL_PASSWORD = passfile.read()
        pollmailu = EmailMessage()
        pollmailu['Subject'] = 'Sending Air Pollution information for your city.'
        pollmailu['From'] = EMAIL_ADDRESS
        pollmailu['To'] = str(mailidto)

        pollmailu.set_content(message_poll_mail)
        f=open("data\\pie_chart_pollution.png",'rb')
        file_data=f.read()
        file_type='png'
        file_name='GRAPH OF POLLUTION'
        pollmailu.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
            
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(pollmailu)
        return True
    except:
        return False
