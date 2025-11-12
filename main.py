import json
from text_detection import text_detection_ratio
from motion_analysis import motion_analysis
from object_dominance import object_vs_person_ratio

if __name__ == "__main__":
    video_path = "sample_video.mp4"

    # Text detection ratio
    text_ratio = text_detection_ratio(video_path)

    # Motion analysis
    motion_value = motion_analysis(video_path)

    # Object vs person dominance
    person_ratio, object_ratio = object_vs_person_ratio(video_path)

    # Combine all results
    result = {
        "video_path": video_path,
        "features": {
            "text_presence_ratio": round(text_ratio, 2),
            "average_motion": round(motion_value, 2),
            "person_dominance_ratio": round(person_ratio, 2),
            "object_dominance_ratio": round(object_ratio, 2)
        }
    }

    print(json.dumps(result, indent=4))
