import librosa

audio_path = "src\Audio_Files\\"

def detect_tempo(audio_path):
    audio_path += input("Enter Filename('.wav' only): ")
    try:
        y, sr = librosa.load(audio_path) 
    except FileNotFoundError:
        print(f"{audio_path} is not a valid file")
        raise SystemExit
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    print(f"Estimated Tempo: {tempo}\n Beat Times(in seconds): {beat_times}")
    return tempo

detect_tempo(audio_path)

