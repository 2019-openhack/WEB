import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def tts(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='ko-KR',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open(text + '.wav', 'wb') as out:
        out.write(response.audio_content)
        print('"'+ text +'.wav"파일로 저장되었습니다.')


# 현재 디렉토리에 있는 .raw 확장자를 가진 파일을 입력받고
# 결과를 가져온다. 아직 리턴값은 정하지 않음
def sst(audioFile):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        audioFile)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    return response.results
    '''
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    '''

if __name__ == "__main__":
    tts('타이머가 설정되었습니다.')
    #sst('input.raw')
