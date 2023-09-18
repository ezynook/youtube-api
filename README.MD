<img src='https://www.gyanblog.com/static/5fbb6c92f37667a196720584b625703a/f3583/youtube_data_api.png' width='150'>

# Youtube Open API 3

## สร้าง credentials

Open browsers and URL here
```bash
https://console.cloud.google.com/
```
* เข้าเมนู 
    * ```IAM & Admin```
    * ```Service Accounts```
    * ```Create Service Account``` ให้เรียบร้อย
* คลิกแถบ 
    * ```Keys```
    * เลือก Type เป็น JSON
    * จากนั้นดาวน์โหลดไฟล์ JSON เก็บไว้ในเครื่อง

## สร้าง API Keys
กลับสู่หน้าแรก

```bash
https://console.cloud.google.com/
```
* เข้าเมนู
    * ```APIs & Services```
    * ```Libraly```
    * เลือก ```Youtube Data API v3```
    * กด ```ENABLE```
    * กด ```MANAGE```
    * กดแถบ ```credentials``` ทำการกด + เพิ่ม
    * ทำการเลือกข้อมูลดังนี้
        * API restrictions ```Restrict key```
    * จากนั้นทำการกด Copy API KEY ด้านข้าง

___OK!___

## ปรับใช้ใน Code แสดง Youtube Channel Playlist
[สามารถดู API Reference เพิ่มเติมได้ที่](https://developers.google.com/youtube/v3/docs?hl=th)

Install Package -> ```pip install google-api-python-client oauth2client```
```py
import os, json, datetime
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
```
```py
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/keys.json"
youtube = build("youtube", "v3", developerKey="API_KEY")
channel_id = "CHANNEL_ID"
```
```py
results = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    order="date", #Order By Date DESC
    maxResults=50 #จำนวนที่ต้องการให้แสดง
).execute()
```
```py
data = []
for item in results["items"]:
    try:
        video_title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        data.append({
            "title": video_title,
            "video": video_id
        })
    except KeyError:
        continue
```
ตัวอย่าง Result JSON
```javascript
    {
        'title': 'เรื่องนี้โหดมาก | สายสุดท้ายหลังเที่ยงคืน #shorts',
        'video': '_-TOhL0NzSE'
    },
    {
        'title': 'เปิดเรื่องมาก็สะดุ้งแล้ว | เรื่องแรกและเรื่องสุดท้าย #shorts',
        'video': 'HItaKCorymw'
    },
```