import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)  # Replace with your microscope camera ID

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = camera.read()
if ret:
    # Display the captured image
    cv2.imshow("Coin Image", frame)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Show edges
    cv2.imshow("Edges", edges)

    # Wait for key press and save
    cv2.waitKey(0)
    cv2.imwrite("coin_image.jpg", frame)
else:
    print("Error: Unable to capture image.")

camera.release()
cv2.destroyAllWindows()
