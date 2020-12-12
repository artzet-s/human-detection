# Human video detection

Given a youtube commercial video, use any existing algorithms to generate a video that shows the existence of humans within the video by drawing boxes around them for each frame.

Exemple video : https://youtu.be/h4s0llOpKrU

[![MISS DIOR – The new Eau de Parfum](https://img.youtube.com/vi/h4s0llOpKrU/0.jpg)](https://youtu.be/h4s0llOpKrU)



## prerequies

* youtube-dl (https://github.com/ytdl-org/youtube-dl)
* YOLOV4 (https://github.com/AlexeyAB/darknet/tree/master)
* python
* opencv


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

## 2. Methods exploration

### 2.1 Result : First experimentation 

* YOLOv3 : https://youtu.be/vRf6-3-KAK8
* YOLOv4 : https://youtu.be/XVEwTaXnyEs
* YOLOv5x : https://youtu.be/pV8MPOm2TCE


### 2.2 Reading ressources : 

* YOLO V1 : 
    * https://arxiv.org/pdf/1506.02640v5.pdf
* YOLO V2 : 
    * https://arxiv.org/pdf/1612.08242v1.pdf
* YOLO V3 : 
    * https://arxiv.org/pdf/1804.02767.pdf
* YOLO V4 : 
    * https://arxiv.org/pdf/2004.10934.pdf
* Scaled-YOLOv4: : 
    * https://arxiv.org/pdf/2011.08036.pdf
* YOLO V5 : 
    * still no paper

