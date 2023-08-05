import tkinter as tk
import cv2
import dlib

# Load the face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmarks predictor from dlib
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def capture_face():
    # Open the video capture device (webcam)
    cap = cv2.VideoCapture(0)
    
    # Continuously read frames from the camera
    while True:
        ret, frame = cap.read()
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = detector(gray)
        
        # Iterate over detected faces
        for face in faces:
            # Get the facial landmarks for the face
            landmarks = predictor(gray, face)
            
            # Draw a rectangle around the face
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
            
            # Save the face to a file
            cv2.imwrite("face.jpg", frame)
            
        # Display the frame
        cv2.imshow("Capture Face", frame)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture device and close the windows
    cap.release()
    cv2.destroyAllWindows()
    app.destroy()  # Close the tkinter window when finished capturing the face

# Create the tkinter app
app = tk.Tk()

# Add a button to capture the face
capture_button = tk.Button(app, text="Capture Face", command=capture_face)
capture_button.pack()

# Start the tkinter event loop
app.mainloop()
