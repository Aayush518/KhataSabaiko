import dlib
import os

# Load the face detector
detector = dlib.get_frontal_face_detector()

# Path to the known_faces directory
directory = r'D:\accounting-with-vat\known_faces'

# Iterate over files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image (optional)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(directory, filename)
        image = dlib.load_rgb_image(image_path)

        # Detect faces in the image
        face_locations = detector(image)
        num_faces = len(face_locations)  # Number of detected faces

        if num_faces == 0:
            # Delete the image if no faces are detected
            os.remove(image_path)
            print(f"Image: {filename} - No faces detected. Image deleted.")
        else:
            print(f"Image: {filename} - Number of faces: {num_faces}")
