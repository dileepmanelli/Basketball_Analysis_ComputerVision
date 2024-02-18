import cv2
import numpy as np

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Load the basketball video
video_path = "C:/Users/dilee/Downloads/WHATSAAP ASSIGNMENT.mp4"
cap = cv2.VideoCapture(video_path)

# Variables for tracking
prev_ball_pos = None
dribble_distance = 0
total_dribble_distance = 0

# Background subtraction parameters
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=False)

# Main loop through video frames
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (presumably the basketball)
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(max_contour)
        ball_position = (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))
        
        # Calculate distance covered during dribble
        if prev_ball_pos is not None:
            dribble_distance += calculate_distance(prev_ball_pos, ball_position)

        # Update previous ball position
        prev_ball_pos = ball_position

        # Draw ball position on frame (for visualization)
        cv2.circle(frame, ball_position, 5, (0, 0, 255), -1)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Calculate total dribble distance
total_dribble_distance += dribble_distance

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()

print("Total dribble distance covered:", total_dribble_distance)

# Width of the basketball court in meters (example)
basketball_court_width_meters = 15

# Width of the basketball court in pixels (measured from the video)
basketball_court_width_pixels = 600  # Example value, replace with actual measurement

# Calculate pixel-to-meter ratio
pixel_to_meter_ratio = basketball_court_width_meters / basketball_court_width_pixels

# Convert total dribble distance to meters
total_dribble_distance_meters = total_dribble_distance * pixel_to_meter_ratio

print("Total dribble distance covered (in meters):", total_dribble_distance_meters)