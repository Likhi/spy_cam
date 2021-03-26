## What is this?

People were stealing stuff from my office desk overnight. AND they were messing up my desk's cleanliness.

Im'ma take their picture.

## Maybe run these

python -m venv .venv 
^if that doesn't work the first time, run it again, maybe add on a 'sudo' or maybe run it in PowerShell.

.\.venv\scripts\activate

python -m pip install --upgrade pip

## Then, definitely run this:

python -m pip install -r requirements.txt

## Now what?

Run the script using: python spy_cam.py

## Anything else?

LOG.log notes when the script has taken a picture, including the webcam capture's filename (which has a timestamp in it).

The algorithm is simple! It just uses scikit image's structural similarity calculation, scoring it on a 
scale of -1 to 1; 1 is identical, decreasing with more differences. If the similiarity falls below 0.9, the script saves the webcam capture.
