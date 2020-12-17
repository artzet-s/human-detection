# Human video detection

Given a youtube commercial video, use any existing algorithms to generate a video that shows the existence of humans within the video by drawing boxes around them for each frame.

Exemple video : https://youtu.be/h4s0llOpKrU

[![MISS DIOR – The new Eau de Parfum](https://img.youtube.com/vi/h4s0llOpKrU/0.jpg)](https://youtu.be/h4s0llOpKrU)

# Exemple result : 

* Best prediction : **YOLOv4-mish** : **https://youtu.be/Ig7cP4zXzzA**

Low confidence is choose according low false positive detection for person class.

|        name              | confidence | precision | recall | mAP  |  F1  |
| -------------------------| ---------- | --------- | ------ | ---- | ---- |
| yolov3_result.json       | 0.25	    | 0.90	    | 0.80	 | 0.79	| 0.84 |
| yolov4-tiny_result.json  | 0.25	    | 0.90	    | 0.69	 | 0.69	| 0.79 |
| yolov5s_result.json      | 0.25	    | 0.92	    | 0.78	 | 0.75	| 0.84 |
| yolov4-csp_result.json   | 0.25	    | 0.94	    | 0.86	 | 0.86	| 0.90 |
| yolov5m_result.json	   | 0.25	    | 0.93	    | 0.85	 | 0.84	| 0.89 |
| yolov4x-mish_result.json | 0.25	    | **0.95**	    | **0.87**	 | **0.87**	| **0.91** |
| yolov4_result.json	   | 0.25	    | 0.94	    | **0.87**	 | **0.87**	| 0.90 |
| yolov5l_result.json	   | 0.25	    | 0.94	    | 0.85	 | 0.84	| 0.89 |
| yolov5x_result.json	   | 0.25	    | 0.93	    | 0.84	 | 0.84	| 0.88 |

* Ref : https://youtu.be/CGyuHgEWQgc

Other results : 

* YOLOv3 : https://youtu.be/5HiMff4vu0M
* YOLOv4-tiny : https://youtu.be/hWKdLXYgGJU
* YOLOv4-csp : https://youtu.be/pYhvZB0w0lU
* YOLOv4 : https://youtu.be/v8GX-pezqrQ
* YOLOv5l : https://youtu.be/dHLDnDcvKrA
* YOLOv5m : https://youtu.be/rFVeZWtG8I4
* YOLOv5s : https://youtu.be/5rk6XmB6lv4
* YOLOv5x : https://youtu.be/pjhPIMEefxw


# How to reproduce result

Note : All the experimentation was done under colab research notebook.

## Reproduce online with Colab Research Notebook (Open Acces)

To reproduce the result, you can follow the specified notebook :

* YOLOv3 and YOLOv4* models: https://colab.research.google.com/drive/13UpMnnmudRjPLaX28ScF2LUKpnPcK4WY?usp=sharing

* YOLOv5* models : https://colab.research.google.com/drive/1DiHBjmMgDm6GzGXzp1d6HCZksA_itIdy?usp=sharing

* Models comparison : https://colab.research.google.com/drive/1AdHsK9sIvwVtTpXm0LlrTD6enwQwRdMd?usp=sharing

There are also saved locally in the notebook directory.

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


### 3. Automate video prediction generation from YOLOv3 and YOLOv4* models using Darknet (neural network framework) 

* Notebook for generate videos : https://colab.research.google.com/drive/13UpMnnmudRjPLaX28ScF2LUKpnPcK4WY?usp=sharing

* YOLOv3 : https://youtu.be/5HiMff4vu0M
* YOLOv4-tiny : https://youtu.be/hWKdLXYgGJU
* YOLOv4-csp : https://youtu.be/pYhvZB0w0lU
* YOLOv4-mish : https://youtu.be/Ig7cP4zXzzA
* YOLOv4 : https://youtu.be/v8GX-pezqrQ

Bounding box prediction on save on json format (darknet format) in predictions directory 

### 4. Automate video prediction generation from YOLOv5* models

* Notebook for generate videos : https://colab.research.google.com/drive/1DiHBjmMgDm6GzGXzp1d6HCZksA_itIdy?usp=sharing

* YOLOv5l : https://youtu.be/dHLDnDcvKrA
* YOLOv5m : https://youtu.be/rFVeZWtG8I4
* YOLOv5s : https://youtu.be/5rk6XmB6lv4
* YOLOv5x : https://youtu.be/pjhPIMEefxw

Bounding box prediction on save on json format (darknet format) in predictions directory

### 5. Ref video and pred models comparison

* Create manual reference bouding box from "YOLOv5x prediction" initialization  : 
    * build use : https://www.makesense.ai/
    * Result : predictions/ref.json
    * https://youtu.be/CGyuHgEWQgc

* Notebook for comparing models : https://colab.research.google.com/drive/1AdHsK9sIvwVtTpXm0LlrTD6enwQwRdMd?usp=sharing


|        name              | confidence | precision | recall | mAP  |  F1  |
| -------------------------| ---------- | --------- | ------ | ---- | ---- |
| yolov3_result.json       | 0.25	    | 0.90	    | 0.80	 | 0.79	| 0.84 |
| yolov4-tiny_result.json  | 0.25	    | 0.90	    | 0.69	 | 0.69	| 0.79 |
| yolov5s_result.json      | 0.25	    | 0.92	    | 0.78	 | 0.75	| 0.84 |
| yolov4-csp_result.json   | 0.25	    | 0.94	    | 0.86	 | 0.86	| 0.90 |
| yolov5m_result.json	   | 0.25	    | 0.93	    | 0.85	 | 0.84	| 0.89 |
| yolov4x-mish_result.json | 0.25	    | 0.95	    | 0.87	 | 0.87	| 0.91 |
| yolov4_result.json	   | 0.25	    | 0.94	    | 0.87	 | 0.87	| 0.90 |
| yolov5l_result.json	   | 0.25	    | 0.94	    | 0.85	 | 0.84	| 0.89 |
| yolov5x_result.json	   | 0.25	    | 0.93	    | 0.84	 | 0.84	| 0.88 |

### 6. Difficult case 

#### Case 1 : Under water view

![Difficult case 1](/doc/211.jpg "Under water view")

#### Case 2 : Top view

![Difficult case 2](/doc/736.jpg "Top view")

#### Case 3 : Distant view

![Difficult case 3](/doc/833.jpg "Distant view")

#### Prototype - Conceivable solution

* Augment image resolution :
    * Split the image into (24) small ones and make prediction from them :
        * Take very long time (1 hour) to process
        * Notebook : https://colab.research.google.com/drive/1CHCEzLOPO-TBysDNVSLHEZdOvPm2C3CQ?usp=sharing
        * Raw result : https://youtu.be/vNYbKrATUwY
        * Don't improve difficult case as expected  
    * Improve small images with VideoSuperResolution model
        * WIP - Google Collab GPU limit exceed ...

* Post processing :
    * Track person box according image part similarity
    * Merge person box along the video
