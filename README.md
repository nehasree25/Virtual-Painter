# 🎨 Virtual Painter

A real-time **Virtual Painter** application built using **Python**, **OpenCV**, and **MediaPipe** that allows users to draw in the air using hand gestures without touching the screen.

## 📌 Features

- ✋ Real-time hand tracking using MediaPipe
- 🖌️ Draw using your index finger
- 👆 Gesture-based color selection
- 🧽 Eraser tool
- 🎨 Multiple brush colors
- ⚡ Smooth drawing experience
- 📷 Live webcam interface

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Project Structure

```
Virtual Painter/
│
├── Paint_Images/          # Header images for color selection
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   └── 5.png
│
├── handDetection.py       # Hand detection module
├── virtualPainter.py      # Main application
└── README.md
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/virtual-painter.git
cd virtual-painter
```

### Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ Run the Project

```bash
python virtualPainter.py
```

---

## 🖐️ Hand Gestures

### 🎨 Selection Mode

Raise **Index Finger + Middle Finger**

- Move your fingers to the top toolbar.
- Select:
  - Pink Brush
  - Orange Brush
  - Green Brush
  - Yellow Brush
  - Eraser

---

### ✍️ Drawing Mode

Raise **Only the Index Finger**

- Move your finger freely to draw.
- The application tracks your fingertip and creates smooth strokes.

---

## 🧠 How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Finger positions determine the current gesture.
4. If two fingers are up, the application enters **Selection Mode**.
5. If only the index finger is up, it enters **Drawing Mode**.
6. Drawings are stored on a separate canvas and merged with the webcam feed.

---

## 📸 Application Workflow

```
Webcam
   │
   ▼
Capture Frame
   │
   ▼
Detect Hand Landmarks
   │
   ▼
Recognize Gesture
   │
   ├─────────────► Selection Mode
   │                 │
   │                 ▼
   │          Choose Brush Color
   │
   └─────────────► Drawing Mode
                     │
                     ▼
              Draw on Canvas
                     │
                     ▼
         Merge Canvas with Webcam
                     │
                     ▼
               Display Output
```

---

