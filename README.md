Video Feature Extraction Tool

This Python project extracts key features from a video file including:

Text Detection Ratio – how much text appears in the video.

Motion Analysis – average motion intensity between frames.

Object vs Person Dominance – ratio of frames containing people vs other objects using YOLOv3.

The output is a single JSON summarizing all features.

📁 Folder Structure
video_extractor/
 ├── main.py
 ├── text_detection.py
 ├── motion_analysis.py
 ├── object_dominance.py
 ├── yolov3.weights
 ├── yolov3.cfg
 ├── coco.names
 └── sample_video.mp4

⚙️ Requirements

Python 3.10+ (MacOS, Windows, or Linux)

pip packages:

pip install opencv-python numpy pytesseract


Tesseract OCR installed (for text detection):

MacOS:

brew install tesseract


Windows: Download installer from https://github.com/tesseract-ocr/tesseract

YOLOv3 weights, config, and COCO names:

yolov3.weights – Download

yolov3.cfg – Download

coco.names – Download

Place all YOLO files in the root folder alongside main.py.

🚀 Running the Project

Activate your Python virtual environment:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Sample requirements.txt:

opencv-python
numpy
pytesseract


Place a video in the project folder (e.g., sample_video.mp4).

Run the main script:

python main.py


The output will be a JSON like this:

{
    "video_path": "sample_video.mp4",
    "features": {
        "text_presence_ratio": 0.12,
        "average_motion": 2.35,
        "person_dominance_ratio": 0.67,
        "object_dominance_ratio": 0.45
    }
}

⚡ Notes

Adjust sample_rate in each module for faster processing. Higher values = fewer frames sampled.

Text detection uses Tesseract; ensure Tesseract path is correct in text_detection.py.

Motion analysis uses OpenCV’s Farneback optical flow.

YOLO object detection uses pre-trained YOLOv3 on COCO dataset.

📌 References

OpenCV Python Docs

Pytesseract Docs

YOLOv3 Paper