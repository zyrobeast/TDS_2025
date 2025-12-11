import yt_dlp

# YouTube video URL
VIDEO_URL = "https://www.youtube.com/watch?v=NRntuOJu4ok"

# Output subtitle file
SUB_FILE = "clip_subtitles.srt"

# Time range in seconds
START_TIME = 117
END_TIME = 351.6

ydl_opts = {
    "writesubtitles": True,           # Download subtitles
    "writeautomaticsub": True,        # Use auto-generated subtitles if no manual
    "subtitlesformat": "srt",         # Save as SRT
    "subtitleslangs": ["en"],         # Only English subtitles
    "outtmpl": "temp_video.%(ext)s",  # Temporary video file
    "download_sections": [f"*{START_TIME}-{END_TIME}"],  # Only the segment
    "skip_download": True             # Don't download the full video
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.download([VIDEO_URL])

print(f"Subtitles saved as {SUB_FILE}")



# from faster_whisper import WhisperModel

# FILE = "/mnt/e/Python/TDS_2025/A Mystery Story [NRntuOJu4ok].mp3"
# model = WhisperModel("medium", device="cpu")
# segments, info = model.transcribe(FILE, beam_size=5, language="en")

# start_time = 117.0
# end_time = 351.6
# filtered_text = []
# for segment in segments:
#     if segment.end >= start_time and segment.start <= end_time:
#         filtered_text.append(segment.text)

# transcript_window = " ".join(filtered_text)

# print(f"Transcript from {start_time}s to {end_time}s:\n")
# print(transcript_window)
