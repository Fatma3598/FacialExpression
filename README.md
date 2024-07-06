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

# Demo: Local deployment with the onnx model of > 0.78 mAP

https://github.com/Fatma3598/FacialExpression/assets/50721861/e1e5980b-59c8-44ab-9a69-b02ec1461429

