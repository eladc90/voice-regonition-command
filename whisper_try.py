import whisper

model = whisper.load_model("base")
result = model.transcribe(r"C:\Users\eladc\Downloads\Audio_Twitter_Tweets.mp3")
print(result["text"])