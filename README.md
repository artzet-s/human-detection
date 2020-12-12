# Human video detection

Given a youtube commercial video, use any existing algorithms to generate a video that shows the existence of humans within the video by drawing boxes around them for each frame.

Exemple video : https://youtu.be/h4s0llOpKrU

<iframe width="853" height="480" src="https://www.youtube.com/embed/h4s0llOpKrU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## prerequies

* youtube-dl (https://github.com/ytdl-org/youtube-dl)
* YOLOV4 (https://github.com/AlexeyAB/darknet)
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

## 2. Try several methods

### 2.1 First experimentation and results : 

* YOLO V3 : https://youtu.be/vRf6-3-KAK8
* YOLO V4 : https://youtu.be/XVEwTaXnyEs




