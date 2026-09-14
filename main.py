import argparse
import sys
import cv2
from face_detector import FaceDetector


def process_image(image_path, detector):
    """
    Process a single image file and display results.
    
    Args:
        image_path: Path to the image file
        detector: FaceDetector instance
    """
    try:
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Error: Cannot read image from {image_path}")
            return False
        
        print(f"Processing image: {image_path}")
        faces = detector.detect_faces(frame)
        result = detector.draw_detections(frame, faces)
        
        print(f"Detected {len(faces)} face(s)")
        
        # Display the result
        cv2.imshow('Face Detection - Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        return True
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return False


def process_webcam(detector):
    """
    Process webcam stream in real-time.
    
    Args:
        detector: FaceDetector instance
    """
    try:
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Cannot open webcam")
            return False
        
        print("Webcam opened. Press 'q' to quit.")
        
        while True:
            ret, frame = cap.read()
            
            if not ret:
                print("Error: Failed to read frame from webcam")
                break
            
            faces = detector.detect_faces(frame)
            result = detector.draw_detections(frame, faces)
            
            # Display face count on the frame
            text = f"Faces detected: {len(faces)}"
            cv2.putText(result, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                       0.7, (0, 255, 0), 2)
            
            cv2.imshow('Face Detection - Webcam', result)
            
            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        return True
        
    except Exception as e:
        print(f"Error processing webcam: {e}")
        return False


def main():
    """Main entry point for the face detection program."""
    parser = argparse.ArgumentParser(
        description='Detect faces in images or webcam stream'
    )
    parser.add_argument(
        '--image',
        type=str,
        help='Path to an image file for face detection'
    )
    parser.add_argument(
        '--webcam',
        action='store_true',
        help='Run face detection on webcam stream'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.image and not args.webcam:
        parser.print_help()
        print("\nError: Please provide either --image or --webcam argument")
        return 1
    
    if args.image and args.webcam:
        print("Error: Cannot use both --image and --webcam simultaneously")
        return 1
    
    try:
        detector = FaceDetector()
    except RuntimeError as e:
        print(f"Error initializing detector: {e}")
        return 1
    
    # Process based on argument
    if args.image:
        success = process_image(args.image, detector)
    else:
        success = process_webcam(detector)
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
