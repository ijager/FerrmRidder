#/usr/bin/env python3

import pickle
import glob
import pandas as pd
from scipy.io import wavfile
import numpy as np

def generateWaveForm(filename):
    print("Trying to process", filename)
    fs, data = wavfile.read(filename)
    if data.ndim == 1:
        d = np.abs(data)
    else:
        # multi channel audio: only use one
        d = np.abs(data[:,0])
    d = np.abs(data)
    N = len(d)
    f = pd.DataFrame(d)
    t = np.linspace(0, N/fs, N)
    f.index = pd.to_timedelta(t, unit='s')
    downsampled = f.resample('5ms').mean()
    scaled = downsampled / np.max(downsampled)[0] * 255
    result = list(scaled[0])

    newFilename = filename.replace('.wav', '.pkl')
    # with open(newFilename, 'wb') as f:
    #     pickle.dump(result, f)
    return newFilename

wavfiles = glob.glob("thankyou/*.wav")
print(wavfiles)
[generateWaveForm(f) for f in wavfiles]