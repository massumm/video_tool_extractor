import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def text_detection_ratio(video_path, sample_rate=30):
    cap = cv2.VideoCapture(video_path)
    total_frames, text_frames = 0, 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % sample_rate == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            if len(text.strip()) > 5:
                text_frames += 1
            total_frames += 1
    cap.release()
    return float(text_frames / total_frames) if total_frames else 0
