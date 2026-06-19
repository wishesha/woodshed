# Woodshed
A musical analysis tool built using NVIDIA's Jetson Orin Nano. Analyses practice audio locally. 

# Current Version: v0.1

# What it does
Detects tempo from an audio recording using LibROSA's beat tracking algorithm. Takes a WAV file as input, analyses it and returns a tempo in BPM along with timestamped beat positions. 

# Functionality
- Takes a WAV file as user input
- Converts beat frame positions to timestamps in seconds
- Handles FileNotFoundErrors

# Testing and Findings
Tested against 2 real recordings
1. Solo Clean Guitar Recording of the intro to "Out Getting Ribs" - King Krule.
  - Returned an accurate tempo of 123 BPM
2. Saxophone Solo during a jazz combo rehearsal (multiple instruments, freeform jazz ballad)
  - tempo estimate was inaccurate

This suggests that LibROSA is accurate and reliable for solo instrument input with predictable rhythm, but struggles with dense, multi-instrumental recordings. This finding will direct the future of Woodshed with a focus on solo practice sessions.

# Limitations 
- No passage management - singular .wav file
- No database or session logging/tracking
- Not yet deployed on jetson
- Tempo detection only: No pitch or accuracy analysis yet

# Setup
```bash
git clone https://github.com/wishesha/woodshed.git
cd woodshed
python -m venv woodshed-env
woodshed-env\Scripts\activate
pip install -r requirements.txt
```

