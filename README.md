# Video Feature Extraction Tool

This Python project extracts key features from a video file including:

- **Text Detection Ratio** – how much text appears in the video.
- **Motion Analysis** – average motion intensity between frames.
- **Object vs Person Dominance** – ratio of frames containing people vs other objects using YOLOv3.

The output is a **single JSON** summarizing all features.

---

## 📁 Folder Structure
```
video_extractor/
 ├── main.py
 ├── text_detection.py
 ├── motion_analysis.py
 ├── object_dominance.py
 ├── yolov3.weights
 ├── yolov3.cfg
 ├── coco.names
 └── sample_video.mp4
```

---

## ⚙️ Requirements

- Python 3.10+ (MacOS, Windows, or Linux)
- pip packages:

```bash
pip install opencv-python numpy pytesseract
```

- **Tesseract OCR** installed (for text detection):

**MacOS:**
```bash
brew install tesseract
```

**Windows:** Download installer from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

- YOLOv3 weights, config, and COCO names:
  - `yolov3.weights` – [Download](https://pjreddie.com/media/files/yolov3.weights)  
  - `yolov3.cfg` – [Download](https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg)  
  - `coco.names` – [Download](https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names)  

Place all YOLO files in the **root folder** alongside `main.py`.

---

## Running the Project

1. Activate your Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> **Sample `requirements.txt`:**
```
opencv-python
numpy
pytesseract
```

3. Place a video in the project folder (e.g., `sample_video.mp4`).

4. Run the main script:

```bash
python main.py
```

5. The output will be a **JSON** like this:

```json
{
    "video_path": "sample_video.mp4",
    "features": {
        "text_presence_ratio": 0.12,
        "average_motion": 2.35,
        "person_dominance_ratio": 0.67,
        "object_dominance_ratio": 0.45
    }
}
```

---

## ⚡ Notes

- Adjust `sample_rate` in each module for faster processing. Higher values = fewer frames sampled.  
- Text detection uses Tesseract; ensure Tesseract path is correct in `text_detection.py`.  
- Motion analysis uses OpenCV’s Farneback optical flow.  
- YOLO object detection uses pre-trained YOLOv3 on COCO dataset.  

---

## 📌 References

- [OpenCV Python Docs](https://docs.opencv.org/)
- [Pytesseract Docs](https://pypi.org/project/pytesseract/)
- [YOLOv3 Paper](https://pjreddie.com/media/files/papers/YOLOv3.pdf)

