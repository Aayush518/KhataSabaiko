import cv2
import tkinter as tk
from PIL import ImageTk, Image
import threading

def start_face_lock():
    def face_lock_thread():
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            photo = ImageTk.PhotoImage(image)

            label.config(image=photo)
            label.image = photo

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()

    face_lock_thread = threading.Thread(target=face_lock_thread)
    face_lock_thread.start()

window = tk.Tk()
window.geometry("400x300")

label = tk.Label(window)
label.pack()

start_button = tk.Button(window, text="Start Face Lock", command=start_face_lock)
start_button.pack()

window.mainloop()
