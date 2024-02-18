import cv2
import numpy as np

# Function to calculate distance between two points
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Read video file
cap = cv2.VideoCapture("C:/Users/dilee/Downloads/WHATSAAP ASSIGNMENT.mp4")

# Initialize variables
prev_ball_position = None
total_distance = 0
frame_count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess frame (e.g., convert to grayscale, apply Gaussian blur, etc.)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform object detection/tracking to locate the basketball
    # You can use methods like Hough Circle Transform or template matching
    # Here we'll just detect a bright object (assuming basketball is brighter than surroundings)
    _, thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Assume the largest contour corresponds to the basketball
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        ball_position = (int(x), int(y))
        
        # Calculate distance moved by the basketball
        if prev_ball_position:
            total_distance += distance(prev_ball_position, ball_position)
        
        prev_ball_position = ball_position
        
    # Display frame with detected basketball
    cv2.imshow('Frame', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    frame_count += 1

# Calculate dribble speed
# Assuming a fixed framerate of 30 fps for the video
fps = 30
dribble_speed = total_distance / (fps * frame_count)

print("Average dribble speed:", dribble_speed, "pixels/frame")

# Release resources
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Function to calculate distance between two points
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Read video file
cap = cv2.VideoCapture("C:/Users/dilee/Downloads/WHATSAAP ASSIGNMENT.mp4")

# Initialize variables
prev_ball_position = None
total_distance = 0
frame_count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocess frame (e.g., convert to grayscale, apply Gaussian blur, etc.)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform object detection/tracking to locate the basketball
    # You can use methods like Hough Circle Transform or template matching
    # Here we'll just detect a bright object (assuming basketball is brighter than surroundings)
    _, thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Assume the largest contour corresponds to the basketball
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        ball_position = (int(x), int(y))
        
        # Calculate distance moved by the basketball
        if prev_ball_position:
            total_distance += distance(prev_ball_position, ball_position)
        
        prev_ball_position = ball_position
        
    # Display frame with detected basketball
    cv2.imshow('Frame', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    frame_count += 1

# Calculate dribble speed
# Assuming a fixed framerate of 30 fps for the video
fps = 30
dribble_speed = total_distance / (fps * frame_count)

print("Average dribble speed:", dribble_speed, "pixels/frame")

# Release resources
cap.release()
cv2.destroyAllWindows()

