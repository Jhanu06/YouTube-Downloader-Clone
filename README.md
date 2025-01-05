
# YouTube Video Downloader Clone  

A feature-rich YouTube Video Downloader that enables users to download videos and audio in various resolutions and formats. Built using **FastAPI** for the backend and **HTML/CSS/JavaScript** for the frontend, this project provides a smooth and user-friendly interface for seamless downloads.  

---

## Features  

- **Video Downloads**: Download YouTube videos in multiple resolutions and formats, including MP4 and MP3.  
- **Video-to-Audio Conversion**: Convert YouTube videos to audio files (MP3).  
- **Batch Downloading**: Download multiple videos simultaneously for enhanced productivity.  
- **Error Handling**: Comprehensive error management ensures smooth operations even with invalid inputs or network issues.  
- **Modern UI**: Intuitive and responsive user interface built using HTML, CSS, and JavaScript.  

---

## Tech Stack  

- **Frontend**:  
  - HTML  
  - CSS (for styling)  
  - JavaScript (for interactivity and API integration)  

- **Backend**:  
  - **FastAPI**: A modern, fast web framework for Python for handling API requests.  
  - **yt-dlp**: A powerful library for downloading YouTube videos and audio.  

---

## How It Works  

1. **User Interaction**:  
   - The user enters the YouTube video URL in the provided input field.  
   - Selects the desired format and resolution (if applicable).  

2. **Backend Processing**:  
   - The URL is sent to the FastAPI backend, where the **yt-dlp** library processes the request.  
   - The backend extracts video metadata, handles the download, and converts the file if needed.  

3. **Download**:  
   - The processed file is sent back to the user for download.  

## API Endpoints  

### 1. Download Video  
- **Endpoint**: `/download`  
- **Method**: POST  
- **Body**: `{ "link": "<YouTube video URL>" }`  
- **Response**: JSON with download status and file URL  
