import cv2
import os
import numpy as np

def object_vs_person_ratio(video_path, sample_rate=30):
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    with open("coco.names") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    cap = cv2.VideoCapture(video_path)
    total_frames = 0
    person_frames = 0
    object_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_id = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        if frame_id % sample_rate != 0:
            continue

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        person_detected = False
        object_detected = False

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = int(np.argmax(scores))
                confidence = scores[class_id]
                if confidence > 0.5:
                    label = classes[class_id]
                    if label == "person":
                        person_detected = True
                    else:
                        object_detected = True

        if person_detected:
            person_frames += 1
        if object_detected:
            object_frames += 1
        total_frames += 1

    cap.release()
    person_ratio = person_frames / total_frames if total_frames else 0
    object_ratio = object_frames / total_frames if total_frames else 0
    return float(person_ratio), float(object_ratio)
