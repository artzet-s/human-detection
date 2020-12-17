# -*- python -*-
#
#       Copyright 2020 - SIMON ARTZET
#
# ==============================================================================
import cv2
import os
import os.path
import json

def draw_box(image, 
             relative_coordinates, 
             box_color=(0, 0, 255),
             box_thickness=3):
  """Draw box on the image according relative coordinate

  Args:
      image (numpy array): image 
      relative_coordinates (dict): dict(center_x, center_y, width, height) in relative image coordinates
      box_color (tuple, optional): color of the box. Defaults to (0, 0, 255).
      box_thickness (int, optional): thickness of the box. Defaults to 3.

  Returns:
      numpy array: image with the box drawed 
  """

  rc = relative_coordinates

  img_height, img_width = (image.shape[0], image.shape[1])

  relative_start_point = ((rc["center_x"] - rc["width"] / 2), 
                          (rc["center_y"] - rc["height"] / 2))

  start_point =  (int(img_width * relative_start_point[0]),
                  int(img_height * relative_start_point[1]))

  size_box = (int(img_width * rc["width"]),
              int(img_height * rc["height"]))    

  end_point = (start_point[0] + size_box[0], 
               start_point[1] + size_box[1])

  image = cv2.rectangle(image, 
                        start_point, 
                        end_point, 
                        box_color, 
                        box_thickness) 
  return image


def draw_person_box_on_frames(result_filename,
                              output_dir,
                              confidence=0.20,
                              box_color=(0, 0, 255),
                              box_thickness=3):
  """draw box on the images according json file predictions coordinate 

  Args:
      result_filename ([str]): json prediction file
      output_dir (str): output directory where are saved images 
      confidence (float, optional): minimum confidence value for draw perso box. Defaults to 0.20.
      box_color (tuple, optional): color of the box. Defaults to (0, 0, 255).
      box_thickness (int, optional): thickness of the box. Defaults to 3.
  """
  
  with open(result_filename) as f:
    data = json.load(f)

  if not os.path.exists(output_dir):
    os.mkdir(output_dir)

  for d in data:
    filename = d["filename"] 

    img = cv2.imread(filename)

    for obj in d["objects"]:
      if obj["name"] == "person" and obj["confidence"] > confidence:
        img = draw_box(img, 
                       obj["relative_coordinates"],
                       box_color=box_color,
                       box_thickness=box_thickness)
            
    img_filename = os.path.join(output_dir, 
                                os.path.basename(filename))
    cv2.imwrite(img_filename, img)
