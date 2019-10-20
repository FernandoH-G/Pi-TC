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

#kr = "./Shell/kr.sh"
#rn = "./Shell/rn.sh"
nt = "./Shell/nt.sh" #No tutor. Run generic tutoring center message.
ap = "./Shell/ap.sh"
jc = "./Shell/jc.sh"
fh = "./Shell/fh.sh"
mb = "./Shell/mb.sh"
rr = "./Shell/rr.sh"
# Double covers
jm = "./Shell/jm.sh"
fa = "./Shell/fa.sh"
rf = "./Shell/fa.sh"
fj = "./Shell/fj.sh"
ma = "./Shell/ma.sh"
ra = "./Shell/ra.sh"
rb = "./Shell/rb.sh"

# 5 rows x 18 columns
tutors = np.array([
#   9am                      12pm                                    5pm
    [jc, jc, jc, jc, jm, jm, ap, ap, fa, fa, fa, fa, rf, rf, rr, rr, rr, rr],
    [jc, jc, jc, jc, jc, jc, jc, jc, mb, mb, mb, mb, mb, mb, mb, mb, mb, mb],
    [fh, fh, fj, fj, fj, fj, ap, ap, ma, ma, ma, ma, ra, ra, ra, ra, ra, ra],
    [ap, ap, ap, ap, ap, ap, ap, fh, fh, fh, fh, jc, jc, jc, rr, rr, rr, rr],
    [rr, rr, rr, rr, rb, rb, rr, nt, mb, mb, mb, mb, mb, mb, mb, mb, nt, nt],
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
