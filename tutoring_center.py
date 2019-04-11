#!/usr/bin/python
import subprocess
import time
import datetime
import psutil
import numpy as np

def killTutorProc():
    for proc in psutil.process_iter():
        if proc.name() == 'soffice.bin':
            proc.kill()

nt = "./Shell/nt.sh" #No tutor. Run generic tutoring center message.
kr = "./Shell/kr.sh"
jc = "./Shell/jc.sh"
fh = "./Shell/fh.sh"
mb = "./Shell/mb.sh"
rn = "./Shell/rn.sh"
re = "./Shell/re.sh"
# 5 rows x 18 columns
tutors = np.array([
    [kr, kr, nt, nt, jc, jc, jc, jc, fh, fh, fh, rn, rn, rn, nt, nt, nt, rn],
    [fh, fh, jc, jc, jc, jc, jc, jc, jc, jc, jc, jc, mb, mb, mb, mb, mb, mb],
    [kr, kr, nt, nt, jc, jc, jc, jc, fh, fh, fh, rn, rn, rn, nt, nt, nt, rn],
    [kr, kr, mb, mb, mb, mb, mb, mb, nt, nt, nt, nt, nt, jc, jc, jc, nt, nt],
    [fh, fh, fh, fh, nt, kr, kr, nt, nt, fh, fh, fh, fh, rn, rn, rn, rn, rn],
])

while(True):
	# Figure out the weekday.
	now = datetime.datetime.now()
	day = now.isoweekday()
	day = day-1# Arrays start at index 0!

	# Figure out whose shift it is.
	# MAKRE SURE TO HANDLE 0/30!
	# EX: (9 % 9)*2 + (1/30) = 0.3 -> 0
	#     (9 % 9)*2 + (31/30) = 1.03 -> 1
	hour = now.hour
	hour = (hour % 9) * 2
	minute = now.minute
	if minute == 0:
		minute += 1
	minute = minute / 30
	shift = hour + minute
	shift = int(shift)

	#Display tutor's powerpoint.
        #       Within working hours                Within working days
	if ((now.hour >= 9 and now.hour < 18) and (day >= 0 and day < 5)):
		tutor = tutors[day][shift]
                # Display powerpoint every 30 minutes.
		if (now.minute == 0 and now.second == 1 or now.minute == 30 and now.second == 1):
			killTutorProc()
			time.sleep(5)
			process = subprocess.Popen(tutor, shell=True)
