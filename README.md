# 🎨 Air Canvas AI  
### Gesture-Based Virtual Drawing & Letter Recognition using OpenCV and TensorFlow

Air Canvas AI is an AI-powered virtual drawing system that allows users to write letters in the air using hand gestures captured by a webcam. The system uses Computer Vision and Deep Learning to detect hand movements, recognize handwritten letters, and convert them into digital text in real time.

This project combines **OpenCV, MediaPipe, and TensorFlow** to create an interactive human–computer interface where users can write without touching any physical device.

---

# 🚀 Project Overview

Traditional input devices like keyboards, mouse, and touchscreens require physical interaction. Air Canvas AI introduces a **touchless writing interface** where users draw letters in the air using finger gestures.

The system detects the **index finger position** to draw on a virtual canvas and uses a trained deep learning model to recognize the written letters.

Predicted characters are displayed and can be stored to form words.

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Main programming language |
| OpenCV | Image processing and drawing canvas |
| MediaPipe | Real-time hand tracking |
| TensorFlow / Keras | Deep learning model for letter recognition |
| NumPy | Numerical computations |
| Computer Vision | Gesture detection and tracking |

---

# ✨ Features

• Air drawing using hand gestures  
• Real-time letter recognition using AI  
• Hand gesture based controls  
• Erasing mode using finger gesture  
• Dataset collection for improving model  
• Word canvas to display predicted letters  
• Color selection toolbar  
• Prediction confidence score display  
• Real-time webcam processing  

---

# 🖐 Gesture Controls

| Gesture | Function |
|-------|---------|
| ☝ Index Finger | Draw on canvas |
| ✌ Two Fingers | Select drawing color |
| 🤟 Three Fingers | Erase drawing |
| 🖐 Five Fingers | Save predicted letter |

---

# ⚙️ System Workflow

1. Webcam captures live video frames  
2. MediaPipe detects hand landmarks  
3. Index finger tip is tracked  
4. Drawing occurs on virtual canvas  
5. Canvas image is processed  
6. Image resized to 28×28 pixels  
7. Image passed to CNN model  
8. Model predicts the letter  
9. Prediction and confidence are displayed  

---

# 🧠 AI Model

The recognition system uses a **Convolutional Neural Network (CNN)** trained on handwritten alphabet images.

**Model Input**
```
28 × 28 grayscale image
```

**Model Output**
```
26 alphabet classes (A–Z)
```

---

# 📂 Project Structure

```
air-canvas-ai
│
├── main.py
├── HandTrackingModule.py
├── letter_model.h5
│
├── dataset
│   ├── A
│   ├── B
│   ├── C
│
├── new_dataset
│   ├── A
│   ├── B
│
├── screenshots
│   ├── interface.png
│   ├── drawing.png
│   ├── prediction.png
│
├── requirements.txt
└── README.md
```

---

# 🖥 System Requirements

### Hardware
• Webcam  
• Minimum 4GB RAM  
• CPU / GPU capable of running Python ML libraries  

### Software
• Python 3.8 or higher  
• OpenCV  
• MediaPipe  
• TensorFlow  
• NumPy  

---

# 📦 Installation

### Clone the repository

```
git clone https://github.com/anfas-02/air-canvas-ai.git
```

### Navigate to project folder

```
cd air-canvas-ai
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the project

```
python main.py
```

---

# 📋 Requirements

Create **requirements.txt**

```
opencv-python
numpy
tensorflow
mediapipe
```

---

# 🧪 Dataset Collection

The system can collect new handwriting samples.

When a letter is saved, the image is stored in:

```
new_dataset/<letter>/
```

This helps expand the dataset and improve model accuracy.

---

# 📊 Example Output

Example prediction:

```
Prediction: A (0.94)
```

Where  
A = predicted letter  
0.94 = confidence score  

---

# 📸 Screenshots

Add screenshots inside the **screenshots folder**

Example:

```
![Interface](screenshots/interface.png)
![Drawing](screenshots/drawing.png)
![Prediction](screenshots/prediction.png)
```

---

# 🔬 Applications

• Touchless writing systems  
• Smart classrooms  
• Virtual whiteboards  
• Accessibility tools  
• Gesture-based interfaces  
• AR / VR input systems  

---

# ⚠ Limitations

• Requires proper lighting  
• Hand must remain within camera view  
• Prediction depends on dataset quality  
• Complex handwriting may reduce accuracy  

---

# 🔮 Future Improvements

• Word prediction using NLP  
• Sentence generation  
• Multi-user support  
• Mobile application  
• AR / VR integration  
• Transformer-based handwriting recognition  

---

# 🏁 Conclusion

Air Canvas AI demonstrates how computer vision and deep learning can transform human-computer interaction. By replacing traditional input devices with gesture-based writing, the system provides a more natural and intuitive way to interact with digital systems.

The project showcases the power of combining **OpenCV, MediaPipe, and TensorFlow** to create intelligent real-time applications.

---

# 👨‍💻 Author

**Anfas**

GitHub  
https://github.com/anfas-02

---

⭐ If you like this project, give it a star on GitHub!
