import pyttsx3
import cv2

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use first available voice
engine.setProperty('rate', 150)

# Text-to-speech function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')  # Load the trained model
    cascadepath = "haarcascade_frontalface_default.xml"
    facecascade = cv2.CascadeClassifier(cascadepath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Define known names for recognized IDs
    names = ['', 'Adarsh']  # Add names corresponding to trained IDs

    # Initialize webcam
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # Set width
    cam.set(4, 480)  # Set height
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()  # Capture frames
        convertedimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facecascade.detectMultiScale(
            convertedimage, scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH))
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, accuracy = recognizer.predict(convertedimage[y:y + h, x:x + w])
            print(accuracy)

            if accuracy > 50:  # Threshold for successful recognition
                id = names[id] if id < len(names) else "Unknown"
                accuracy_text = f"{round(100 - accuracy)}%"
                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 0), 1)
                cv2.putText(img, str(accuracy_text), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
                print(f"Authentication successful")
                speak("Authentication successful")
                """cam.release()
                cv2.destroyAllWindows()"""
                cv2.imshow('Camera', img)
                k = cv2.waitKey(10) & 0xff
                if k == 27:  # Press 'ESC' to exit
                    break
                break

            else:
                id = "Unknown"
                accuracy_text = f"{round(100 - accuracy)}%"
                print(f"Authentication unsuccessful: {id}, Accuracy: {accuracy_text}")
                speak("Authentication unsuccessful")



    cam.release()
    cv2.destroyAllWindows()
