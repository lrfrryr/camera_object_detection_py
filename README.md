# Movement detector on camera
Detects objects moving in camera and sends an email notification with attached picture.

## General overview
Videos are a stack of static pictures called frames. This algorithm compares frames to the stored first frame (which is what the camera captures the moment the program starts running), by comparing the intensity value of the pixels (frames are previously altered to remove unnecesary information to make the comparison more accurate). When something new appears, frames are saved in the "images" directory and once the frame goes back to being equal to the initial frame, one of the frames stored in the "images" directory gets send by email. 

### Points I would like to improve
- Get the program to detect which kind of object is appearing on frame. This could be done by using an advanced library or by integrating and implementing some ML algorithm that recognizes different objects.

#### Requirements
- Python3

#### How to use
Clone repository and install needed packages. Run through command line.


<img src="camera_detector.gif"/>
