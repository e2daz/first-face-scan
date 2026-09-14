import cv2
import numpy as np


class FaceDetector:
    """Face detection using OpenCV Haar Cascade classifier."""
    
    def __init__(self):
        """Initialize the face cascade classifier."""
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        
        if self.face_cascade.empty():
            raise RuntimeError("Failed to load Haar Cascade classifier")
    
    def detect_faces(self, frame):
        """
        Detect faces in a frame.
        
        Args:
            frame: Input image/frame (BGR format)
            
        Returns:
            List of detected faces as (x, y, w, h) tuples
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        return faces
    
    def draw_detections(self, frame, faces, color=(0, 255, 0), thickness=2):
        """
        Draw bounding boxes around detected faces.
        
        Args:
            frame: Input image/frame
            faces: List of detected faces
            color: RGB color for bounding boxes
            thickness: Line thickness
            
        Returns:
            Frame with drawn bounding boxes
        """
        result = frame.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(result, (x, y), (x + w, y + h), color, thickness)
        return result
