"""Saves all photos in the current folder into smaller files in smaller/."""
import cv2
import threading
import os


# Percentage of the scaling.
SCALE_PERCENT = 50
# Name of the directory.
DIR_NAME = 'smaller'


class ExportSmaller(threading.Thread):
  """Exports a smaller file using OpenCV."""
  def __init__(self, filename, scale=SCALE_PERCENT):
    threading.Thread.__init__(self)
    self.filename = filename
    self.scale = scale

  def run(self):
    # Uses IMREAD_COLOR for auto-rotation rather than IMREAD_UNCHANGED.
    img = cv2.imread(self.filename, cv2.IMREAD_COLOR)
    width = int(img.shape[1] * self.scale / 100)
    height = int(img.shape[0] * self.scale / 100)
    dim = (width, height)
    # Resizes the image.
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite("%s/%s" % (DIR_NAME, self.filename), resized)
    print(self.filename + ' completed.')

if __name__ == '__main__':
  cwd = os.getcwd()
  path_dir_files = os.walk(cwd)
  created_dir = False

  export_threads = []

  for path, dir_list, file_list in path_dir_files:
    for filename in file_list:
      if len(path) > len(DIR_NAME) and path[-len(DIR_NAME):] == DIR_NAME:
        continue
      if filename[-3:] == "JPG":
        # Creates a "smaller" folder if not existed.
        if not created_dir:
          created_dir = True
          if not os.path.exists(DIR_NAME):
            os.mkdir(DIR_NAME)
        # Runs the exporting thread.
        export_threads.append(ExportSmaller(filename))
        export_threads[-1].start()

  for thread in export_threads:
    thread.join()
