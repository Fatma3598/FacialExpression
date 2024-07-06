# FacualExpression Notebook
1. Code for affectnet-yolo-format dataset downloading in colab or working with it directly in kaggle
2. PyTorch model creation, training, validation and testing

# ONNX Notebook
1. Export ONNX model from the pytorch model
2. onnex model validation and testing

# Deployment
1. The main.py file has the FastAPi script for the local deployment
2. make sure to update the images folder and the model paths in the file
3. Install FactAPi: pip install fastapi uvicorn
5. run: uvicorn main:app --reload

# Dataset link
  https://www.kaggle.com/datasets/fatihkgg/affectnet-yolo-format

# Models Link
  PyTorch models: https://drive.google.com/drive/folders/12-tpSJAc-tq1bDYKwN5tfhYQOdIUVzuX?usp=drive_link
  
  ONNX models: https://drive.google.com/drive/folders/128PDDXSYdEv0ytusLmlcfwD60Hi02Je-?usp=drive_link

# Project documentation
The "Facial Expression Detection AI Model" file provides a comparison of different models.

# Demo: Local deployment with the onnx model of > 0.78 mAP

https://github.com/Fatma3598/FacialExpression/assets/50721861/8be9a91e-0a3d-4b54-8909-b9080eacaf6a


