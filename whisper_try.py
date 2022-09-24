import whisper

model = whisper.load_model("base")
result = model.transcribe("Audio")
print(result["text"])