import os
import torch
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

torch.hub.set_dir(os.path.join(os.environ['TORCH_HOME'], 'hub'))

os.environ['TORCH_HOME'] = r'D:\ai_cache\torch'
os.environ['XDG_CACHE_HOME'] = r'D:\ai_cache'
os.environ['XDG_CACHE_HOME'] = r'D:\ai_cache'        # used by bark (generation.py)
os.environ['TORCH_HOME'] = r'D:\ai_cache\torch'     # used by torch/torch.hub
os.environ['HF_HOME'] = r'D:\ai_cache\huggingface'  # optional: Hugging Face repo/cache
os.environ['BARK_CACHE_DIR'] = r'D:\ai_cache'       # optional: if you patch bark

# download and load all models
preload_models()

def text_to_speech_bark(i, question):
     
     # You can also use custom voice clones or None for default voice
     voice_preset = "v2/en_speaker_8"  # Change this to select different voice
     audio_array = generate_audio(question, history_prompt=voice_preset)

     # save audio to disk
     write_wav(f"output/{i}.wav", SAMPLE_RATE, audio_array)
     
     # play text in notebook
     Audio(audio_array, rate=SAMPLE_RATE)