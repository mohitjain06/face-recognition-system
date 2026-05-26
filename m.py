import cv2

# Open the camera (index 0 usually refers to the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not access the camera. Please check if the camera is connected.")
else:
    print("Camera is opened successfully!")

# Read and display the frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Camera Feed", frame)

    # Press 'q' to quit the camera window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
