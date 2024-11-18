from typing import Any

# Import pywhispercpp
try:
    import pywhispercpp.model as pywhispercpp
    from pywhispercpp.utils import to_timestamp

    WHISPER_INSTALLED = True  # pywhispercpp is installed
except ModuleNotFoundError:
    pywhispercpp = type("pywhispercpp", (object,), {"Model": Any})  # Set pywhispercpp for type hints
    def to_timestamp(t: int, separator=',') -> str:
        del t, separator
        raise NotImplementedError
    WHISPER_INSTALLED = False  # pywhispercpp is not installed

# Import vosk
try:
    import vosk

    VOSK_INSTALLED = True  # vosk is installed
except ModuleNotFoundError:
    vosk = type("vosk", (object,), {"Model": Any, "KaldiRecognizer": Any})  # Set vosk for type hints
    VOSK_INSTALLED = False  # vosk is not installed
