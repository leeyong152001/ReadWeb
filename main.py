import os
import sys
# argparse

from gtts import gTTS
import speech_recognition

from webscraping import gettext, tofile, scrap

def bot():
    bot_text = 'tôi nói hello bạn, bạn không nghe thấy à!'
    bot_ear = speech_recognition.Recognizer() #Siri nghe
    with speech_recognition.Microphone() as mic:
        print("\nSiri: I'm listening")
        # audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic, duration= 3) #Siri nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
        print("\nSiri: ....")
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN')# nó sẽ lấy giọng của chị Google
        print("\nYou: "+you)   
    except:
        you ="Tôi không hiểu bạn nói gì."
        print("\nSiri: "+you)

    language = 'vi'

    myobj = gTTS(text=bot_text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")

def run():
    # # google
    # language = 'en' #'vi'
    # myobj = gTTS(text=text, lang=language, slow=False)
    # # Saving the converted audio in a mp3 file named
    # # welcome 
    # myobj.save("welcome.mp3")
    # # Playing the converted file
    # os.system("start welcome.mp3")


    # microsoft
    cmd = "edge-tts -f fil etext.txt -v vi-VN-HoaiMyNeural --write-media hello.mp3 --write-subtitles hello.vtt"
    os.system(cmd)


if __name__ == "__main__":
    # argparse sys.argv[1]
    # scrap(630,641)
    run()
