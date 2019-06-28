import io
import os
import sys


def tts(path,text):
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
    save_path = os.path.join(path, text+'.wav')
    print(save_path)
    # The response's audio_content is binary.
    with open(save_path, 'wb') as out:
        out.write(response.audio_content)
        print('"'+ text +'.wav" is saved')


if __name__ == "__main__":
    tts('jisu','apple')
    #sst('input.raw')
