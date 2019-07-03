import random
import time
import speech_recognition as sr

def recognize_from_mic(recognizer,microphone):
    if not isinstance(recognizer,sr.Recognizer):
        raise TypeError("`recognizer` must be an instance of `Recognizer`")
    if not isinstance(microphone,sr.Microphone):
        raise TypeError("`microphone` must be ab instance of `Microphone`")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"]=recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"]=False
        response["error"]="API not available"
    except sr.UnknownValueError:
        response["error"]="Unable to recognize Speech"
    return response

if __name__=="__main__":
    prompt_limit=5
    
    recognizer=sr.Recognizer()
    microphone=sr.Microphone()

    print("Hey there!\nMy name is Romeo and I have a special talent. I can memeorize any phone number at once.")
    time.sleep(3)

    for i in range(prompt_limit):
        print('\nTry me B-)')
        guess = recognize_from_mic(recognizer, microphone)
        if guess["transcription"]:
                break
        if not guess["success"]:
                break
        print("I didn't catch that. What did you say?\n")

    if guess["error"]:
        print("ERROR: {}".format(guess["error"]))


    print("Well, as I told you... \nI'm too good at this.\nThe number is: {} \nThanks for the number BTW ;)".format(guess["transcription"]))