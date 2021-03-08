import moviepy
import moviepy.editor


video = moviepy.editor.VideoFileClip("C:/Users/lenovo/Downloads/Rec (3).mp4")    # Put your file path in here

audio = video.audio
audio.write_audiofile('new.mp3')