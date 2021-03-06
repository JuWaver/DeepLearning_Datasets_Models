import scipy.signal
import numpy as np


def low_pass_filter(x, f=1., fs=100):
    f = f / (fs / 2)
    x = np.abs(x)
    b, a = scipy.signal.butter(1, f, 'low')  # low pass filter
    output = scipy.signal.filtfilt(
        b, a, x, axis=0,
        padtype='odd', padlen=3 * (max(len(b), len(a)) - 1)
    )
    return output


