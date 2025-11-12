import cv2

def motion_analysis(video_path, sample_rate=1):
    cap = cv2.VideoCapture(video_path)
    ret, prev_frame = cap.read()
    if not ret:
        return 0

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    total_flow = 0
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_id = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        if frame_id % sample_rate != 0:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None,
                                            0.5, 3, 15, 3, 5, 1.2, 0)
        mag, _ = cv2.cartToPolar(flow[...,0], flow[...,1])
        total_flow += mag.mean()
        frame_count += 1
        prev_gray = gray

    cap.release()
    average_motion = float(total_flow / frame_count) if frame_count else 0
    return average_motion
