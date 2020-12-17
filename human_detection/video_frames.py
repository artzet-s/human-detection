import argparse
import cv2
import os
import glob


def video_to_frames(path, output_dir="frames", verbose=True):

    cap = cv2.VideoCapture(path)
    
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    i_frame = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            output_name = os.path.join(output_dir, '{}.jpg'.format(i_frame))
            cv2.imwrite(output_name, frame)

            if verbose:
                print("Extract video frame {} - shape : {}".format(
                    i_frame, frame.shape))
        else: 
            break

        i_frame += 1

    # When everything done, release the video capture object
    cap.release()

    if verbose:
        print("Extraction done, with a total of {} frames"
              "saved in \"{}\" folder".format(i_frame, output_dir))
        

def write_txt_list_of_filename(input_dir, filename):

  filenames = glob.glob(os.path.join(input_dir, "*"))
  str_filenames = '\n'.join(filenames)

  file = open(filename, 'w')
  file.write(str_filenames)
  file.close()

def frames_to_video(frame_dir, 
                    video_filename="output_video.mp4", 
                    fps=25):

    img_array = []
    filenames = glob.glob(os.path.join(frame_dir, "*.jpg"))
    for i in range(len(filenames)):
        filename = os.path.join(frame_dir, "{}.jpg".format(i))
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
    
    out = cv2.VideoWriter(
        video_filename,
        cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])

    out.release()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("video_filename", 
                        type=str,
                        help="Video filename for extract frame")

    parser.add_argument("--output_dir", 
                        type=str,
                        default="frames",
                        help="Folder name where saving the video frames")

    parser.add_argument("--verbose", 
                        type=int,
                        default="1")

    args = parser.parse_args()
    print(args)
    video_to_frames(args.video_filename, 
                    output_dir=args.output_dir, 
                    verbose=args.verbose)

if __name__ == "__main__":
    main()
