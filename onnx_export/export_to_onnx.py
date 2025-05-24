import nemo.collections.asr as nemo_asr

# Load the pre-trained model
asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from("model/stt_hi_conformer_ctc_medium.nemo")

# Export to ONNX
asr_model.export("model/stt_hi_conformer_ctc_medium.onnx")
