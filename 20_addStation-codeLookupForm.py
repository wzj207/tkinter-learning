from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('650x160')



null = ''
api_request_content = '''[
    {"aqi": 82,"area": "珠海","pm2_5": 31,"pm2_5_24h": 60,"position_name": "吉大",
    "primary_pollutant": "颗粒物(PM2.5)","quality": "良","station_code": "1367A",
    "time_point": "2013-03-07T19:00:00Z"},
    {"aqi": 108,"area": "滨河","pm2_5": 0,"pm2_5_24h": 53,"position_name": "河西",
        "primary_pollutant": "臭氧8小时","quality": "轻度污染","station_code": "1370A",
        "time_point": "2013-03-07T19:00:00Z"},
    {"aqi": 98,"area": "泗水","pm2_5": 0,"pm2_5_24h": 53,"position_name": "斗门",
        "primary_pollutant": "臭氧8小时","quality": "好","station_code": "1370A",
        "time_point": "2013-03-07T19:00:00Z"}]'''

# api = json.loads(api_request_content)
# print(api)
# Create station_code function
def codelookup():
    # codelabel = Label(root, text=station_code.get())
    # codelabel.grid(row=1, column=0, columnspan=2)

    try:
        api = json.loads(api_request_content)
        index = 0
        city = api[index]['area']
        quality = api[index]['quality']
        primary_pollutant = api[index]['primary_pollutant']

        font = ('黑体', 20)

        if quality == '好':
            weather_color = 'green'
        elif quality == '良':
            weather_color = 'yellow'
        elif quality == '轻度污染':
            weather_color = 'red'

        root.configure(bg=weather_color)

        myLabel = Label(root, text=city + ' 空气质量:' + quality + ' ' + '污染物:' + primary_pollutant,
                        font=font, bg=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

station_code = Entry(root)
station_code.grid(row=0, column=0, stick='WENS')

station_codeButton = Button(root, text='Lookup Station_code', command=codelookup)
station_codeButton.grid(row=0, column=1, stick='WENS')


root.mainloop()




