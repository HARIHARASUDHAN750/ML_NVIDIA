import wave

def validate_audio(file_path: str):
    try:
        with wave.open(file_path, 'rb') as wf:
            duration = wf.getnframes() / float(wf.getframerate())
            sample_rate = wf.getframerate()

            if sample_rate != 16000:
                return False, "Invalid sample rate. Expected 16kHz."
            if duration < 5 or duration > 10:
                return False, "Invalid duration. Audio must be between 5 and 10 seconds."
    except wave.Error as e:
        return False, f"Error processing audio file: {str(e)}"

    return True, "Valid audio file."
