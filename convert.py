from moviepy.editor import *
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def select_audio_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    audio_file_path = filedialog.askopenfilename(title="Select an audio file")
    return audio_file_path

def create_video(output_file):
    audio_file = select_audio_file()

    if not audio_file:
        print("No audio file selected. Exiting.")
        return

    # Load the image (logo)
    logo = ImageClip("logo.jfif")

    # Load the audio file
    audio = AudioFileClip(audio_file)

    # Set the duration of the video to match the audio's duration
    logo = logo.set_duration(audio.duration)
    logo = logo.set_fps(30)

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")  # Format the date as desired

    # Create a text clip with the current date
    date_text = TextClip(current_date, fontsize=60, color="white", bg_color="black", size=(logo.w, 100))
    date_text = date_text.set_duration(audio.duration)

    # Position the date text at the bottom center
    date_text = date_text.set_position(("center", "bottom"))

    # Composite the date text over the image
    video = CompositeVideoClip([logo, date_text])

    # Set the audio for the video
    video = video.set_audio(audio)

    # Write the final video with the combined image, audio, and date text
    video.write_videofile(output_file, codec="libx264", audio_codec="aac")

# Usage example
create_video("news_video.mp4")
