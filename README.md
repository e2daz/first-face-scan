# First Face Scan

A Python face detection program that detects faces in images and real-time webcam streams using OpenCV and Haar Cascade classifiers.

## Features
✓ Detect faces in static images  
✓ Real-time face detection from webcam  
✓ Visual bounding boxes around detected faces  
✓ Face count display for webcam stream  
✓ Robust error handling and validation  

## Project Structure
```
.
├── main.py              # Entry point with argument parsing and processing logic
├── face_detector.py     # FaceDetector class for face detection and visualization
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Detect faces in a static image:
```bash
python main.py --image path/to/image.jpg
```

Example:
```bash
python main.py --image sample.jpg
```

### Detect faces in real-time webcam stream:
```bash
python main.py --webcam
```

Press `q` to quit the webcam stream.

## Usage Notes

- **Image mode**: The image will be displayed in a window with bounding boxes around detected faces. Press any key to close.
- **Webcam mode**: Shows live video feed with real-time face detections and face count in the top-left corner.
- The program uses OpenCV's Haar Cascade frontalface classifier for detection.

## Design Choices

### 1. **Face Detection Library: OpenCV Haar Cascade**
   - **Why**: Simple, fast, lightweight, and built-in. No heavy model downloads required.
   - **Tradeoff**: Slightly less accurate than deep learning methods (like MediaPipe/YOLO), but excellent for basic face detection tasks.
   - **Alternative considered**: MediaPipe (more accurate but heavier dependency)

### 2. **Code Architecture: Modular Design**
   - `FaceDetector` class encapsulates all detection and visualization logic
   - Separate functions for image and webcam processing for clarity
   - Clean argument parsing in main function

### 3. **Parameters for Detection**:
   - `scaleFactor=1.1`: Controls image pyramid construction speed/accuracy tradeoff
   - `minNeighbors=5`: Reduces false positives by requiring at least 5 neighbors
   - `minSize=(30, 30)`: Ignores very small detections (likely false positives)

### 4. **Visualization**:
   - Green bounding boxes (0, 255, 0 in BGR format)
   - Real-time face count display for webcam
   - Simple and clear visual feedback

### 5. **Error Handling**:
   - Validates Haar Cascade loads correctly
   - Checks if image files exist and are readable
   - Verifies webcam is available before streaming
   - User-friendly error messages
