import cv2
from ultralytics import YOLO

class DribbleCounter:
    def __init__(self, video_path):
        # Load the YOLO model for ball detection
        self.model = YOLO("C:/Users/dilee/Downloads/yolov8s.pt")

        # Open the video file
        self.cap = cv2.VideoCapture(video_path)

        # Initialize variables to store the previous position of the basketball
        self.prev_y_center = None
        self.prev_delta_y = None

        # Initialize the dribble counter
        self.dribble_count = 0

        # Threshold for the y-coordinate change to be considered as a dribble
        self.dribble_threshold = 197

        # Number of frames to increase dribble count after a dribble
        self.increase_count_frames = 200
        self.frames_since_last_increase = 0

        # Flag to track upward and downward movement
        self.upward_movement = False
        self.downward_movement = False

    def run(self):
        # Process frames from the video until the end
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if success:
                results_list = self.model(frame, verbose=False, conf=0.65)

                for results in results_list:
                    for bbox in results.boxes.xyxy:
                        x1, y1, x2, y2 = bbox[:4]

                        y_center = (y1 + y2) / 2

                        self.update_dribble_count(y_center)

                        self.prev_y_center = y_center

                    annotated_frame = results.plot()

                    # Draw the dribble count on the frame
                    cv2.putText(annotated_frame, f"Dribbles: {self.dribble_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    cv2.imshow("YOLOv8 Inference", annotated_frame)

                # Adjust the delay to control the play speed (increase the delay to increase play speed)
                if cv2.waitKey(20) & 0xFF == ord("q"):  # Adjust the delay to 20 milliseconds
                    break
            else:
                break

        # Release the video and destroy the windows
        self.cap.release()
        cv2.destroyAllWindows()

    def update_dribble_count(self, y_center):
        if self.prev_y_center is not None:
            delta_y = y_center - self.prev_y_center

            if delta_y > self.dribble_threshold and not self.upward_movement:
                self.upward_movement = True
                self.downward_movement = False
                self.frames_since_last_increase = 0

            if delta_y < -self.dribble_threshold and self.upward_movement:
                self.dribble_count += 1
                self.downward_movement = True
                self.upward_movement = False
                self.frames_since_last_increase = 0

            if self.frames_since_last_increase >= self.increase_count_frames:
                self.dribble_count += 1
                self.frames_since_last_increase = 0
            else:
                self.frames_since_last_increase += 1

if __name__ == "__main__":
    video_path = "C:/Users/dilee/Downloads/WHATSAAP ASSIGNMENT.mp4"  # Change this to the path of your video file
    dribble_counter = DribbleCounter(video_path)
    dribble_counter.run()
