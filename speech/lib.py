from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError


def tts(text: str):
    gtts = gTTS(text, lang="ru")

    mp3_fp = BytesIO()
    gtts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    play(audio)


def stt() -> str:
    r = Recognizer()

    with Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            return r.recognize_google(audio, language="ru-RU")
        except UnknownValueError:
            return "Не удалось разобрать речь. Попробуйте говорить чётче."
        except RequestError:
            return "Ошибка подключения к сервису"


if __name__ == "__main__":
    data = stt()
    tts(data)
