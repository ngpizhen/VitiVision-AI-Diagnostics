# 🍇 VitiVision: AI-Powered Viticulture Diagnostics

## 🏆 Project Highlight
*   **Validation Accuracy:** **96.33%**
*   **Peak Accuracy:** **99.33%** (Achieved during epoch 6)
*   **Detection Classes:** Grape Black Rot, Grape Esca (Black Measles), and Healthy Leaves

---

## 📌 Overview
**VitiVision** is an intelligent agricultural solution designed to protect vineyards from devastating diseases. By leveraging advanced Computer Vision, our system provides farmers with a rapid, automated on-site diagnostic tool to ensure healthy crop yields and sustainable farming practices.

## ⚙️ Technical Methodology
We implemented a **Transfer Learning** strategy to achieve high-performance results with limited computational resources:
*   **Base Model:** MobileNetV2 (Pre-trained on ImageNet).
*   **Optimization:** We froze 2.2 million parameters of the base model to utilize pre-trained visual hierarchies while training a custom classification head.
*   **Architecture:** Added GlobalAveragePooling2D, a Dense layer (128 units, ReLU), and a Dropout layer (0.3) to prevent overfitting.
*   **Data Augmentation:** Applied random rotations, horizontal flips, and zooms to increase model robustness.

## 📊 Dataset & Training
*   **Dataset Size:** 1,500 curated images.
*   **Class Distribution:** Perfectly balanced with 500 images per class (Black Rot, Esca, Healthy).
*   **Efficiency:** Each training epoch was completed in approximately 15 seconds, demonstrating the model's suitability for real-time applications.

## 🚀 Web Application
The system is deployed via a **Gradio** web interface, allowing users to:
1.  Upload a high-resolution photo of a grape leaf.
2.  Receive an instant diagnostic classification.
3.  View confidence scores for all potential disease categories.

## 📁 Repository Structure
*   `CV_project_pizhen.ipynb`: Full training, validation, and evaluation pipeline.
*   `app.py`: Gradio web application deployment script.
*   `my_grape_model.h5`: The final trained model weights.

---
**Developed by:** Ng Pi Zhen  
**Institution:** Faculty of Artificial Intelligence (FAI), Universiti Teknologi Malaysia (UTM)
