### 📁 File: segmenter.py

import torch
import numpy as np
import cv2
from PIL import Image
from segment_anything import sam_model_registry, SamPredictor

# Load model
sam_checkpoint = "D:/AI_BASED_SOLOR_SYSTEM/models/sam_vit_b_01ec64.pth"  # Must be downloaded separately
model_type = "vit_b"

device = "cuda" if torch.cuda.is_available() else "cpu"
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device)
predictor = SamPredictor(sam)

def segment_rooftop(image_file):
    image_pil = Image.open(image_file).convert("RGB")
    image_np = np.array(image_pil)
    predictor.set_image(image_np)

    h, w, _ = image_np.shape
    input_point = np.array([[w // 2, h // 2]])
    input_label = np.array([1])

    masks, _, _ = predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=False
    )

    mask = masks[0]
    result = image_np.copy()
    result[~mask] = 0

    return Image.fromarray(result), np.sum(mask)
