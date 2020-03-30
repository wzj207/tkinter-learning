from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
root.geometry('650x40')
root.configure(bg='green')

null = ''
api_request_content = '''[
    {"aqi": 82,"area": "珠海","pm2_5": 31,"pm2_5_24h": 60,"position_name": "吉大",
    "primary_pollutant": "颗粒物(PM2.5)","quality": "良","station_code": "1367A",
    "time_point": "2013-03-07T19:00:00Z"},
    {"aqi": 108,"area": "滨河","pm2_5": 0,"pm2_5_24h": 53,"position_name": "河西",
        "primary_pollutant": "臭氧8小时","quality": "轻度污染","station_code": "1370A",
        "time_point": "2013-03-07T19:00:00Z"},
    {"aqi": 98,"area": "泗水","pm2_5": 0,"pm2_5_24h": 53,"position_name": "斗门",
        "primary_pollutant": "臭氧8小时","quality": "良","station_code": "1370A",
        "time_point": "2013-03-07T19:00:00Z"}]'''

# api = json.loads(api_request_content)
# print(api)
try:
    api = json.loads(api_request_content)
    city = api[0]['area']
    quality = api[0]['quality']
    primary_pollutant = api[0]['primary_pollutant']
except Exception as e:
    api = "Error..."

font = ('黑体', 20)
myLabel = Label(root, text=city + ' 空气质量 ' + quality + ' ' + '污染物 ' + primary_pollutant,
                font=font, bg='green')
myLabel.pack()

root.mainloop()