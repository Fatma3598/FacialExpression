from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

import os
import torch
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt

 
IMAGEDIR = "images/"
 
app = FastAPI()
 
@app.get("/show/")
async def read_random_file(image_name: str):
    
    #get selected image path
    img_path = IMAGEDIR + image_name

    model = YOLO('last.onnx', task="detect")
    results = model(img_path)

        # Process results list
    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        #result.show()  # display to screen
        output_path = IMAGEDIR + "/ppoutput_image.jpg"
        result.save(output_path)  # save to disk


    return FileResponse(output_path)

