import cv2
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from traffic_app.models.vehicle_detector import VehicleDetector

router = APIRouter()

detector = VehicleDetector()
camera = cv2.VideoCapture(0)  # 0 = webcam, replace with CCTV URL if needed


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        frame, count = detector.detect(frame)

        cv2.putText(
            frame,
            f"Vehicles: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        _, buffer = cv2.imencode(".jpg", frame)
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
        )


@router.get("/live")
def live_stream():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
