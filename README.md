# 🌱 PlantCare AI  
### Advanced Plant Disease Detection Using Transfer Learning  

<p align="center">
  <a href="https://omkumar04-plant-care-ai.hf.space">
    <img src="https://img.shields.io/badge/Live-Demo-success?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/TensorFlow-DeepLearning-orange?style=for-the-badge&logo=tensorflow" />
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/MobileNetV2-TransferLearning-blue?style=for-the-badge" />
</p>


---

## 🌍 Live Demo

👉 https://omkumar04-plant-care-ai.hf.space

---
## 🎥 Project Demo 

👉 [view live project](https://omkumar04-plant-care-ai.hf.space/)

## 🚀 Overview

**PlantCare AI** is a deep learning-powered web application that detects plant diseases from leaf images using **Transfer Learning**.  

The model leverages a pre-trained **MobileNetV2 CNN** to classify plant leaves into **38 different disease categories** with ~90% validation accuracy.

The system is designed to be lightweight, fast, and deployable for real-world agricultural use.

---

## 🧠 How It Works

### 🔄 Application Flow

1. User accesses the web application  
2. Uploads or captures a plant leaf image  
3. Image is resized to **224x224x3** and normalized  
4. MobileNetV2 processes the image  
5. Disease prediction + recommendations are displayed  

---

## 🏗️ Model Architecture

```
Input Layer (224x224x3 RGB)
        ↓
MobileNetV2 Base (Pre-trained, Partially Frozen)
        ↓
GlobalAveragePooling2D
        ↓
Dropout (0.35)
        ↓
Dense (256, ReLU)
        ↓
Dropout (0.25)
        ↓
Dense (38, Softmax)
```

### 🔍 Architecture Details

- **Base Model**: MobileNetV2 (ImageNet Pre-trained)
- **Pooling**: GlobalAveragePooling2D
- **Regularization**: Dropout Layers
- **Output Layer**: 38-class Softmax classification

---

## 📊 Model Details

| Feature | Description |
|----------|------------|
| Architecture | MobileNetV2 (Transfer Learning) |
| Framework | TensorFlow / Keras |
| Dataset | New Plant Diseases Dataset (Kaggle) |
| Total Images | ~87,000 |
| Classes | 38 |
| Image Size | 224x224 |
| Validation Accuracy | ~90% |

---

## 📂 Dataset Information

The project uses the **New Plant Diseases Dataset**, containing:

- 87,000+ annotated leaf images
- 38 plant disease categories
- Multiple crops including:
  - Apple
  - Tomato
  - Potato
  - Corn
  - Grape
  - Strawberry
  - Pepper
  - Soybean
  - Peach
  - Orange
  - Healthy leaf classes

---

## ⚙️ Tech Stack

### 🔹 Backend
- Flask
- TensorFlow
- NumPy

### 🔹 Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 💻 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Om-Pramod-Kumar/Plant-Care-AI.git
cd Plant-Care-AI
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open browser at:  
```
http://127.0.0.1:5000/
```

---

## 🎯 Future Improvements

- ONNX model optimization
- Faster inference
- Disease-wise treatment recommendation system
- User prediction history tracking
- Admin analytics dashboard

---


## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!

---
