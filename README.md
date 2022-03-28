# UNOCards-object-detection
## This repository about UNO object detection with YOLOv5 and real-time webcam bbox draw.

<img src="https://user-images.githubusercontent.com/58363847/160474362-899bea5b-90a0-4ea9-95ad-85eb65dd67e3.png" data-canonical src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="300" height="300" />

To see the video of webcam real-time detection click:<br>
[Real-time detection without GPU](https://youtu.be/l3xqD581TQc)

<p float="left">
  <img src="https://user-images.githubusercontent.com/58363847/160476719-13fa8850-4a6b-4691-8b5a-b79a6f38fd14.jpg" width="200" height="200" />
  <img src="https://user-images.githubusercontent.com/58363847/160477051-813470d6-4059-47d0-ab1e-89456c4a2255.jpg" width="200" height="200" />
  <img src="https://user-images.githubusercontent.com/58363847/160476703-c8b7141b-b872-4965-bf10-49c661ea4b10.jpg" width="200" height="200" />
</p>

<details>
  <summary><em>Data preparation</em></summary>
  Using the reference materials, you can find a link to the dataset. 
  You can preprocess dataset in roboflow. As you know YOLOv5 еakes image size 416x416, so I resized it to this size. 
  To use the dataset you need to click as in the following photos:<br>
  
  <img src="https://user-images.githubusercontent.com/58363847/160475585-1f60c6a0-4c6f-411b-bed2-532f7fa10b84.png" width="300" height="300" />
  
  <img src="https://user-images.githubusercontent.com/58363847/160475594-29a19d80-57c2-4d2f-91d2-d869d3a397c6.png" width="300" height="300" />
  
</details>
<details>
  <summary><em>Train and test the model</em></summary>
  To see how to define model configuration and architecture, train and detect model you need to clone my repo and open file "Train_Yolov5.ipynb".
  In folder weights I saved my post-train weights. You can use them or save your.
  
  </details>
<details>
  <summary><em>Real-time webcam detection</em></summary>
  To see how to define model configuration and architecture, train and detect model you need to clone my repo and open file Real_time_webcam_Yolov5.ipynb.
  This notebook is using file webcamdetect.py where you may find necessary functions.
  </details>
<details>
  <summary><em>References</em></summary>
  1. https://public.roboflow.com/object-detection/uno-cards - Uno cards dataset;
  2. https://github.com/ultralytics/yolov5 - Original repo of YOLOv5;
  3. https://models.roboflow.com/ - Model zoo from roboflow;
  4. https://www.youtube.com/watch?v=nDPWywWRIRo&t=3256s&ab_channel=StanfordUniversitySchoolofEngineering - Basic Object Detection knowledge;
  5. https://www.youtube.com/watch?v=MdF6x6ZmLAY&t=1508s - Yolov5 tutorial;
  6. https://www.youtube.com/watch?v=NU9Xr_NYslo&t=607s - Yolov5 tutorial;
  7. https://www.youtube.com/watch?v=yfDjsuxIKA4&t=2718s - Training other models using Tensorflow Object Detection;
  8. https://www.youtube.com/watch?v=pnntrewH0xg&t=151s - Example of web-app for testing your model;
  9. https://www.youtube.com/watch?v=TB-fdISzpHQ&t=3717s - Another Basic Object Detection knowledge;
  10. https://towardsdatascience.com/yolo-v4-or-yolo-v5-or-pp-yolo-dad8e40f7109 - Difference between the last YOLO-type models
  11. https://techzizou.com/category/object-detection/ - Web app on tf2;
  12. https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md - model zoo(tf2);
</details>


