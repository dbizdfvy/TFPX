noise-threshold.py - gets a before and after histogram of noise and threshold values of recently masked pixels
This program can be used to check if NoiseScan tests are working as intended - if done correctly, the noise and threshold should both go to zero for the masked pixels.

To run this program, run the python file with 4 arguments:
1st argument should be the path to the old CMSIT.txt file
2nd argument should be the path to the new CMSIT.txt file
3rd argument should be the path to the old SCurve.root file
4th argument should be the path to the new SCurve.root file
