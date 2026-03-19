# 🥦 GreenClassify: Deep Learning-Based Approach For Vegetable Image Classification

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

GreenClassify is a Deep Learning project that utilizes a **Convolutional Neural Network (CNN)** to automate the classification and quality assessment of vegetable images. It features a web-based interface built with **Flask** for seamless image uploads and real-time classification results.

## 📸 Project Showcase
| Main Dashboard | Prediction Result |
| :---: | :---: |
| ![Home](screenshots/home.png) | ![Result](screenshots/result.png) |

## 🚀 Key Features
* **Advanced CNN Model:** Custom-trained architecture optimized for detecting vegetable features and freshness indicators.
* **Interactive Web Interface:** User-friendly UI designed for easy navigation and instant feedback.
* **Real-time Processing:** Provides rapid classification results upon image submission.

## 🛠️ Tech Stack
* **Language:** Python
* **Deep Learning:** TensorFlow / Keras
* **Web Framework:** Flask
* **Environment:** Virtualenv (Python 3.13)

## 📂 Project Structure
* `app.py`: The main Flask application and backend logic.
* `model/`: Contains `model_train.ipynb` used for training and evaluating the CNN.
* `screenshots/`: Folder containing UI demonstration images.
* `requirements.txt`: List of Python dependencies required to run the project.

## ⚙️ Installation & Setup
```bash
git clone [https://github.com/spsourabh17/GreenClassify.git](https://github.com/spsourabh17/GreenClassify.git)
cd GreenClassify
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py