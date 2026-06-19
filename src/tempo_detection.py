import librosa

audio_path = "src\Audio_Files\\"

def detect_tempo(audio_path):
    audio_path += input("Enter Filename('.wav' only): ")
    try:
        y, sr = librosa.load(audio_path) 
    except FileNotFoundError:
        print(f"{audio_path} is not a valid file")
        raise SystemExit

detect_tempo(audio_path)

