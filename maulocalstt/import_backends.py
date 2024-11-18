from typing import Any

# Import pywhispercpp
try:
    import pywhispercpp.model as pywhispercpp

    WHISPER_INSTALLED = True  # pywhispercpp is installed
except ModuleNotFoundError:
    pywhispercpp = type("pywhispercpp", (object,), {"Model": Any})  # Set pywhispercpp for type hints
    WHISPER_INSTALLED = False  # pywhispercpp is not installed

# Import vosk
try:
    import vosk

    VOSK_INSTALLED = True  # vosk is installed
except ModuleNotFoundError:
    vosk = type("vosk", (object,), {"Model": Any, "KaldiRecognizer": Any})  # Set vosk for type hints
    VOSK_INSTALLED = False  # vosk is not installed
