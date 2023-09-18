from flask import *
import os, json, datetime
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

app = Flask(__name__)
app.secret_key = 'MjkwOQ=='

@app.route('/')
def root():
    return redirect("/playlist/20")

@app.route('/playlist/<limit>', methods=['GET'])
def index(limit: int):
    if limit:
        length = limit
    else:
        length = 20
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./keys.json"
    youtube = build("youtube", "v3", developerKey="AIzaSyCcw8q-RgiHGYv3cmuB84Dh_1wHFLyQV4w")
    channel_id = "UCM246zZ4qNNmFQ2WHnP_CRA"
    results = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        order="date",
        maxResults=length
    ).execute()
    data = []
    for item in results["items"]:
        try:
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            if "short" not in video_title:
                data.append({
                    "title": video_title,
                    "video": video_id
                })
        except KeyError:
            continue

    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
