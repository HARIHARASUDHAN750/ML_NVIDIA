# Description.md

## ✅ Features Implemented
- ✅ FastAPI server with `/transcribe` endpoint
- ✅ Audio file validation (.wav, 16kHz, 5–10 seconds)
- ✅ Transcription using NVIDIA NeMo's `stt_hi_conformer_ctc_medium`
- ✅ Automatic model download and caching
- ✅ Clean Docker container setup
- ✅ Sample test and response

## ⚠️ Issues Faced
- ONNX export caused shape mismatch (model uses dynamic axes).
- Large NeMo model size — container took longer to build.
- GPU inference not tested due to CPU-only environment.

## 🚫 What’s Missing (if applicable)
- Async inference not fully implemented (NeMo doesn’t support async by default).
- CI/CD and automated testing (due to time constraints).

## 💡 Future Improvements
- Add GPU support with `nemo.collections.asr.models.EncDecCTCModel.restore_from`.
- Integrate streaming audio (WebSocket) for real-time ASR.
- Add front-end for uploading audio.

## ⚠️ Known Limitations
- Works only with `.wav` audio at 16kHz sample rate.
- Transcription time may vary based on hardware.
