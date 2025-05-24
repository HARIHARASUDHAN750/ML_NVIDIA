import nemo.collections.asr as nemo_asr

# Load the pre-trained model
asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from("model/stt_hi_conformer_ctc_medium.nemo")

def transcribe_audio(file_path: str) -> str:
    # Transcribe the audio file
    transcription = asr_model.transcribe([file_path])[0]
    return transcription
