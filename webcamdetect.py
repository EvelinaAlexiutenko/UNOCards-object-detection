import cv2
import numpy as np
import PIL
import io
import html
import time
import matplotlib.pyplot as plt
import threading
import queue
import torch
from torchvision import transforms
import torch.backends.cudnn as cudnn
from numpy import random
from IPython.display import display, Javascript, Image
from google.colab.output import eval_js
from google.colab.patches import cv2_imshow
from base64 import b64decode, b64encode

from string import str_javascript


def video_stream():
    js = Javascript(str_javascript)
    display(js)


def video_frame(label, bbox):
    data = eval_js(f'stream_frame("{label}", "{bbox}")')
    return data


def js_to_image(js_reply):
    image_bytes = b64decode(js_reply.split(',')[1])
    # convert bytes to numpy array
    jpg_as_np = np.frombuffer(image_bytes, dtype=np.uint8)
    # decode numpy array into OpenCV BGR image
    img = cv2.imdecode(jpg_as_np, flags=1)
    return img


def bbox_to_bytes(bbox_array):
    """Function to convert OpenCV Rectangle bounding box image
    into base64 byte string to be overlayed on video stream
    """
    bbox_PIL = PIL.Image.fromarray(bbox_array, 'RGBA')
    iobuf = io.BytesIO()
    # format bbox into png for return
    bbox_PIL.save(iobuf, format='png')
    # format return string
    bbox_bytes = f'data:image/png;base64,{(str(b64encode(iobuf.getvalue())))}'
    return bbox_bytes
