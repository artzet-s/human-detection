# Human video detection

Given a youtube commercial video, use any existing algorithms to generate a video that shows the existence of humans within the video by drawing boxes around them for each frame.

Exemple video : https://youtu.be/h4s0llOpKrU

[![MISS DIOR – The new Eau de Parfum](https://img.youtube.com/vi/h4s0llOpKrU/0.jpg)](https://youtu.be/h4s0llOpKrU)

## Computing ressources

All experimentation was done with Jupiter notebook on Google Colab or Kaggle platform :

* https://colab.research.google.com/
* https://www.kaggle.com/

## Install Prerequies

* youtube-dl - https://github.com/ytdl-org/youtube-dl
* YOLOv4 - https://github.com/AlexeyAB/darknet
* YOLOv5 - https://github.com/ultralytics/yolov5 
* python
    * opencv
    * numpy
    * pytorch
    * tensorflow


## 1. Prepare the data 

### 1.1 Download video

After installed youtube-dl following their documentation (https://github.com/ytdl-org/youtube-dl) use it to download the best quality video :

    #Check available video quality
    youtube-dl -F https://youtu.be/h4s0llOpKrU

    #Download the specific video
    youtube-dl -f 137 https://youtu.be/h4s0llOpKrU  -o input_video.mp4

#### 1.2 Extract video frames

Use scrit video_to_frames.py to extract video frames

    # python video_to_frames.py -h for any help
    python video_to_frames.py input_video.mp4

## 2. Use Deep learning models to detect person in frame video

### 2.1 Use Darknet (neural network framework) to test & compare several models

Reproduce results:

* YOLOv3 and YOLOv4 : https://colab.research.google.com/drive/13UpMnnmudRjPLaX28ScF2LUKpnPcK4WY?usp=sharing

* YOLOv5 : https://colab.research.google.com/drive/1DiHBjmMgDm6GzGXzp1d6HCZksA_itIdy?usp=sharing

Results : 

* YOLOv3 : https://youtu.be/5HiMff4vu0M
* YOLOv4-tiny : https://youtu.be/hWKdLXYgGJU
* YOLOv4-csp : https://youtu.be/pYhvZB0w0lU
* YOLOv4-mish : https://youtu.be/Ig7cP4zXzzA
* YOLOv4 : https://youtu.be/v8GX-pezqrQ
* YOLOv5l : https://youtu.be/dHLDnDcvKrA
* YOLOv5m : https://youtu.be/rFVeZWtG8I4
* YOLOv5s : https://youtu.be/5rk6XmB6lv4
* YOLOv5x : https://youtu.be/pjhPIMEefxw

## Appendix : Methodology history

### 1. Methods exploration

Try rapidly several models to validate proof of concept 

* YOLOv3 : https://youtu.be/vRf6-3-KAK8
* YOLOv4 : https://youtu.be/XVEwTaXnyEs
* YOLOv5x : https://youtu.be/pV8MPOm2TCE

### 2. Reading ressources :  

* YOLO V1 : https://arxiv.org/pdf/1506.02640v5.pdf
* YOLO V2 : https://arxiv.org/pdf/1612.08242v1.pdf
* YOLO V3 : https://arxiv.org/pdf/1804.02767.pdf
* YOLO V4 : https://arxiv.org/pdf/2004.10934.pdf
* Scaled-YOLOv4: : https://arxiv.org/pdf/2011.08036.pdf
* YOLO V5 : still no paper


### 3. Automate video prediction generation from YOLOv3 and YOLOv4* models

* Notebook for generate videos : https://colab.research.google.com/drive/13UpMnnmudRjPLaX28ScF2LUKpnPcK4WY?usp=sharing

* YOLOv3 : https://youtu.be/5HiMff4vu0M
* YOLOv4-tiny : https://youtu.be/hWKdLXYgGJU
* YOLOv4-csp : https://youtu.be/pYhvZB0w0lU
* YOLOv4-mish : https://youtu.be/Ig7cP4zXzzA
* YOLOv4 : https://youtu.be/v8GX-pezqrQ

### 4. Automate video prediction generation from YOLOv5* models

* Notebook for generate videos : https://colab.research.google.com/drive/1DiHBjmMgDm6GzGXzp1d6HCZksA_itIdy?usp=sharing

* YOLOv5l : https://youtu.be/dHLDnDcvKrA
* YOLOv5m : https://youtu.be/rFVeZWtG8I4
* YOLOv5s : https://youtu.be/5rk6XmB6lv4
* YOLOv5x : https://youtu.be/pjhPIMEefxw
