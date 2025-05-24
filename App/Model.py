import os
import urllib.request
import nemo.collections.asr as nemo_asr
import torchaudio

MODEL_DIR = "models"
MODEL_FILENAME = "stt_hi_conformer_ctc_medium.nemo"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)
MODEL_URL = "https://api.ngc.nvidia.com/v2/models/nvidia/nemo/stt_hi_conformer_ctc_medium/versions/1/files/stt_hi_conformer_ctc_medium.nemo"

# Download model if missing
def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading NeMo ASR model...")
        os.makedirs(MODEL_DIR, exist_ok=True)
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Download complete.")

# Load model at import time
download_model()
asr_model = nemo_asr.models.EncDecCTCModel.restore_from(MODEL_PATH)

def transcribe_audio(audio_path: str) -> str:
    # Transcribe the input WAV file
    return asr_model.transcribe(paths2audio_files=[audio_path])[0]
