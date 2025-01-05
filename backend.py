from fastapi import FastAPI, Form
import os
import yt_dlp # type: ignore

app = FastAPI()
cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    output_path = os.path.join(cur_dir, "abcsample.mp4")
    
    youtube_dl_options = {
        "format": "best",
        "outtmpl": output_path
    }
    
    # Create a yt_dlp object with options
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        # Download the video
        ydl.download([link])
    
    return {"message": f"Video downloaded successfully to {output_path}!"}
