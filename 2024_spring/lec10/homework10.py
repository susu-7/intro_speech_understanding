import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    num_frames = int((len(waveform) - frame_length) / step) + 1
    frames = np.zeros((frame_length, num_frames))
    for i in range(num_frames):
        start_index = i * step
        frames[:, i] = waveform[start_index:start_index + frame_length]
    return frames


def frames_to_stft(frames):
    frame_length, num_frames = frames.shape
    stft = np.fft.fft(frames, axis=0)
    return stft


def stft_to_spectrogram(stft):
    magnitude = np.abs(stft)
    max_mag = np.amax(magnitude)
    spectrogram = 20 * np.log10(np.maximum(1e-6, magnitude / max_mag))
    spectrogram = np.clip(spectrogram, -60, 0)
    return spectrogram



