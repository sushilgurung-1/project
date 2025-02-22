import moviepy.editor as mp
import whisper
from transformers import pipeline
from gtts import gTTS
import os

# Step 1: Extract Audio from Video
def extract_audio(video_path, audio_output):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output)

# Step 2: Transcribe Nepali Audio
def transcribe_audio(audio_path):
    model = whisper.load_model("large")
    result = model.transcribe(audio_path, language="ne")
    return result['text']

# Step 3: Translate Nepali to English
def translate_text(text):
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ne-en")
    translated_text = translator(text, max_length=500)[0]['translation_text']
    return translated_text

# Step 4: Convert Translated Text to Speech
def text_to_speech(text, output_audio):
    tts = gTTS(text=text, lang='en')
    tts.save(output_audio)

# Step 5: Overlay New Audio on Original Video
def overlay_audio_on_video(video_path, audio_path, output_video):
    video = mp.VideoFileClip(video_path)
    new_audio = mp.AudioFileClip(audio_path)
    final_video = video.set_audio(new_audio)
    final_video.write_videofile(output_video, codec='libx264', audio_codec='aac')

# Main Function
def main(video_path, output_path):
    temp_audio = "temp_audio.wav"
    translated_audio = "translated_audio.mp3"

    print("Extracting audio from video...")
    extract_audio(video_path, temp_audio)

    print("Transcribing audio...")
    nepali_text = transcribe_audio(temp_audio)
    print("Transcribed Text:", nepali_text)

    print("Translating to English...")
    english_text = translate_text(nepali_text)
    print("Translated Text:", english_text)

    print("Converting text to speech...")
    text_to_speech(english_text, translated_audio)

    print("Overlaying new audio on video...")
    overlay_audio_on_video(video_path, translated_audio, output_path)

    print("Translation and video processing complete!")
    os.remove(temp_audio)
    os.remove(translated_audio)

# Run the script
if __name__ == "__main__":
    input_video = "input_video.mp4"
    output_video = "output_translated_video.mp4"
    main(input_video, output_video)
