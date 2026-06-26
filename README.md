# Woodshed
A musical analysis tool planned to be built using NVIDIA's Jetson Orin Nano. Currently analyses practice audio locally.

# Current Version: v0.1

## What it does
Detects tempo from an audio recording using LibROSA's beat tracking algorithm. Takes a WAV file as input, analyzes it and returns a tempo in BPM (beats per minute) along with number of detected beats. 

## Functionality
- Takes a WAV file as user input
- Displays file size in human-readable units(KB/MB)
- Detects number of distinct beats in recording
- Handles Invalid File path through OSError and many other audio related errors via a broader Exception catch, without crashing.
- Calculates total compute time

## Testing and Findings
### Primitive Testing - 2 real recordings
1. Solo clean guitar recording of the intro to "Out Getting Ribs" - King Krule.
  - Returned an accurate tempo of 123 BPM 
2. Saxophone solo during a jazz combo rehearsal (multiple instruments, freeform jazz ballad)
  - tempo estimate was inaccurate

#### Findings
- This suggests that LibROSA is accurate and reliable for solo instrument input with predictable rhythm, but struggles with dense, multi-instrumental recordings. This finding will direct the future of Woodshed with a focus on solo practice sessions.

### Secondary Testing
Tested against an empty and corrupted audio file to seek out potential edge cases and errors where applicable.
- Found that both these types (Empty vs Corrupted) can raise different specific exception types, which led to the decision to use broader exception handling due to the wide variety of potential audio loading errors.

### Performance Notes
- Test 1 (Guitar Intro) took approximately 4.8-6.1 seconds for a 10 second(1.8 MB) audio clip. Important to note as it will come into play when weighing the value of jetson, and if this method of tempo detection is still viable to achieve real-time detection

## Limitations 
- No passage management - singular .wav file
- No database or session logging/tracking
- Not yet deployed on jetson
- Tempo detection only: No pitch or accuracy analysis yet

## Setup
```bash
git clone https://github.com/wishesha/woodshed.git
cd woodshed
python -m venv woodshed-env
woodshed-env\Scripts\activate
pip install -r requirements.txt
```

