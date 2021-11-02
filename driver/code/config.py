import numpy as np

turning_offset = 0
tpu_available = False
logging = False
use_pid = False

camera_mid_offset_percent = 0.063
min_threshold = 20 # minimal of votes

#blue
#lower_color = np.array([30, 40, 0])
#upper_color = np.array([150, 255, 255])

#red
lower_color = np.array([0, 60, 40])
upper_color = np.array([5, 255, 255])