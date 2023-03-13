<!-- @format -->

# Hand-Tracking-Canvas

Hand Tracking Canvas is a canvas using AI. It will track your hand's landmarks and then use the tracking points to draw on the screen.There are 3 mode to paint: both index and middle up for selection mode, both thumb and index finger up dor drag and drop mode, and only index finger up for drawing.
<br/>
<br/>

#### Selection Mode

<img src="https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/selection-mode.gif?raw=true" width = "500" height = "400" alt="selection-mode" align="center" />
<br/>
<br/>
<br/>

#### Paintin Mode

<img src="https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/painting-mode.gif?raw=true" width = "500" height = "400" alt="selection-mode" align="center" />
<br/>
<br/>
<br/>

#### Drag and Drop Mode

<img src="https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/drag-and-drop-mode.gif?raw=true" width = "500" height = "400" alt="selection-mode" align="center" />
<br/>
<br/>

## Installation

You could directly download application by Links below:
<br/>
(MacOS m1, m2 are not supported so far)
<br/>
<br/>
MacOS (x86_64):
<br/>
[https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand-Tracking-Canvas+(Mac+x86_64).app.zip](<https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand-Tracking-Canvas+(Mac+x86_64).app.zip>)
<br/>
<br/>
Windows:
<br/>
[https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand-Tracking-Canvas(Windows).zip](<https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand-Tracking-Canvas(Windows).zip>)
<br/>
<br/>
Or download the source code to run this project.
<br/>
However, there are some prerequisites that are needed to be done first.
<br/>
You need to install the required libraries by running the following command lines in the project's directory:

```bash
pip install -r requirements
```

now you can run the project directly from your terminal or IDE:

```bash
cd src
python app.py
```

<br/>
If everything has gone right, you can use different hand gesture modes as demo above to paint:
<br/>
<br/>

## Using Tips

- when both index and middle fingers are up, then turn into selection mode, and make a selection
- paint when only the index finger is up
- After select a shape to draw, use thumb and index finger to drag, when all fingers are up are up, then the shape would be fixed on th canvas
  <br/>
  <br/>

## Table of Contents

- [Main Idea and Features](#main-idea-and-features)
- [Technique](#technique)
  - [Key Points](#key-points)
  - [Environment](#environment)
  - [Version Control](#version-control)
- [Architecture](#architecture)
- [Contact](#contact)

<br/>
<br/>

## Main Idea and Features

- Using opencv to proccess video frame captured from camera, turn it into .jpeg file
- Using Flask framework to keep sending response to the front end displayed image
- Using mediapipe to detect hand and finger's tip location, as the image shown below

![image](https://media.geeksforgeeks.org/wp-content/uploads/20210802154942/HandLandmarks.png)

<br/>
<br/>

## Technique

### Key Points

- mediapipe
- opencv

<br/>
<br/>

### Environment

- Python Flask

<br/>
<br/>

### Version Control

- Git/GitHub

<br/>
<br/>

## Architecture

- Server Architecture

  ![image]()

<br/>
<br/>

## Contact

Sand, Yang
<br/>

Email: sand050965@gmail.com
