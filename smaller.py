import cv2
import os

cwd = os.getcwd()
g = os.walk(cwd)
created_dir = False
SCALE_PERCENT = 50
DIR_NAME = 'smaller'

for path, dir_list, file_list in g:
  for file_name in file_list:
    if file_name[-3:] == "JPG":
      if not created_dir:
        created_dir = True
        # Creates a "smaller" folder if not existed.
        if not os.path.exists(DIR_NAME):
          os.mkdir(DIR_NAME)
      print(file_name)
      # Uses IMREAD_COLOR for auto-rotation rather than IMREAD_UNCHANGED.
      img = cv2.imread(file_name, cv2.IMREAD_COLOR)
      width = int(img.shape[1] * SCALE_PERCENT / 100)
      height = int(img.shape[0] * SCALE_PERCENT / 100)
      dim = (width, height)
      # Resizes the image.
      resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
      cv2.imwrite("%s/%s" % (DIR_NAME, file_name), resized)
