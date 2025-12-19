import cv2
from ultralytics import YOLO

class VehicleDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.vehicle_classes = [2, 3, 5, 7]  # car, motorcycle, bus, truck

    def detect(self, frame):
        results = self.model(frame, conf=0.4, verbose=False)
        vehicle_count = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                if cls in self.vehicle_classes:
                    vehicle_count += 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(
                        frame,
                        r.names[cls],
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

        return frame, vehicle_count
