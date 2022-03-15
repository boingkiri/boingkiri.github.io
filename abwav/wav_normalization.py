import os 
import numpy as np 
import pdb
import librosa 
import soundfile as sf

wav_dirs = os.listdir("wav")
abtest_dirs = os.listdir("wav/abtest")

for abtest in abtest_dirs:
    wav_file_name = "wav/abtest/"+abtest
    wav, sr = librosa.load(wav_file_name, 24000)
    wav = librosa.util.normalize(wav) * 0.3
    sf.write(wav_file_name, wav, 24000)
