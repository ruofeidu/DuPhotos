"""Renames folder based on their original name of Sony DSLRs"""
import cv2
import threading
import os

if __name__ == '__main__':
  cwd = os.getcwd()
  path_dir_files = os.walk(cwd)
  created_dir = False

  export_threads = []

  for path, dir_list, file_list in path_dir_files:
    for d in dir_list:
      if len(d) == 8 and d.isnumeric():
        src = os.path.join(path, d)
        dst = os.path.join(path, d[4:])
        print(src, dst)
        os.rename(src, dst)
