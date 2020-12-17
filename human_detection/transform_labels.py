import glob 
import os
import json

def labels_dir_to_json(frames_dir, 
                       labels_dir, 
                       json_result):

  classes_cvt = {0: "person"}

  data = list()
  for filename in glob.glob(os.path.join(frames_dir, "*.jpg")):
    d = dict()
    d["filename"] = filename
    d["objects"] = list()

    path = os.path.join(labels_dir, os.path.basename(filename)[:-4] + ".txt")
    if os.path.exists(path):
      with open(path) as file_in:
        for line in file_in:
          r = list(map(float, line.split(" ")))

          obj = dict()
          obj["name"] = classes_cvt[r[0]]
          obj["confidence"] = 1.0

          rc = dict()
          rc["center_x"] = r[1]
          rc["center_y"] = r[2]
          rc["width"] = r[3]
          rc["height"] = r[4]

          obj["relative_coordinates"] = rc
          
          d["objects"].append(obj)
 
    data.append(d)

    with open(json_result, 'w') as outfile:
      json.dump(data, outfile, indent=4)
