# Hand-Tracking-Canvas

---

<p align="center">
  <img width="350" src="https://github.com/sand050965/Mini-Room/main/readme/logo.png?raw=true">
</p>
Hand Tracking Canvas is a canvas using AI. It will track your hand's landmarks and then use the tracking points to draw on the screen.There are 3 mode to paint: both index and middle up for selection mode, both thumb and index finger up dor drag and drop mode, and only index finger up for drawing.
<br/>
<br/>

## Installation

---

You could directly download application by Links below:
(MacOS m1, m2 are not supported so far):
<br/>
MacOS (x86_64): [https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand+Tracking+Canvas+(Mac+x86_64).app.zip](https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand+Tracking+Canvas+(Mac+x86_64).app.zip)
<br/>
Windows: [https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand+Tracking+Canvas+(Windows).zip](https://s3.amazonaws.com/www.miniroom.online/hand_tracking_canvas/Hand+Tracking+Canvas+(Windows).zip)
<br/>
<br/>
Or download the source code and run this project.
However, there are some prerequisites that are needed to be done first.
It's needed to install the required libraries by running the following command lines in the project's directory:

```bash
pip install -r requirements
```

now you can run the project directly from your terminal or IDE:

```bash
cd src
python app.py
```

If everything has gone right, you can use below hand gesture modes to paint:

## Selection Mode

![image](https://https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/selection-mode.gif?raw=true)

## Paintin Mode

![image](https://https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/images/painting-mode.gif?raw=true)

## Drag and Drop Mode

![image](https://https://github.com/sand050965/Hand-Tracking-Canvas/blob/main/readme/drag-and-drop-mode.gif?raw=true)

## Table of Contents

- [Main Idea and Features](#main-idea-and-features)
- [Technique](#technique)
  - [Key Points](#key-points)
  - [Environment](#environment)
  - [Version Control](#version-control)
- [Architecture](#architecture)
- [Contact](#contact)

## Main Idea and Features

- Using opencv to proccess video frame captured from camera, turn it into .jpeg file
- Using Flask framework to keep sending response to the front end displayed image
- Using mediapipe to detect hand and finger's tip location
- when both index and middle fingers are up, then turn into selection mode, and make a selection
- paint when only the index finger is up
- After select a shape to draw, use thumb and index finger to drag, when all fingers are up are up, then the shape would be fixed on th canvas

## Technique

### Key Points

- mediapipe
- opencv

### Environment

- Python Flask

### Version Control

- Git/GitHub


## Architecture

- Server Architecture

  ![image]()

## Contact

Sand, Yang
<br/>

Email: sand050965@gmail.com
