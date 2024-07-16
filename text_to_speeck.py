import pyttsx3
import pyfiglet

def output(text):
    try:
        spk = pyttsx3.init()
        voices = spk.getProperty('voices')
        spk.setProperty('voice', voices[1].id)
        spk.say(text)
        spk.runAndWait()

    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    ascii_banner = pyfiglet.figlet_format("Text_to_Speech")
    print(ascii_banner)
    output("Hello, This is a text to Speech convertor")
    text = input("Enter the text you want to convert:")
    output(text)
    


main()