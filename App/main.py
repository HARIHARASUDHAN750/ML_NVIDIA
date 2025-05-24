from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import os
from model import transcribe_audio
from utils import validate_audio

app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .wav files are supported.")

    # Save uploaded file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Validate audio duration and sample rate
    is_valid, message = validate_audio(file_location)
    if not is_valid:
        os.remove(file_location)
        raise HTTPException(status_code=400, detail=message)

    # Transcribe audio
    try:
        transcription = transcribe_audio(file_location)
    except Exception as e:
        os.remove(file_location)
        raise HTTPException(status_code=500, detail=str(e))

    # Clean up
    os.remove(file_location)

    return JSONResponse(content={"transcription": transcription})
