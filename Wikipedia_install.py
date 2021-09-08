"""   This module will install Wikipedia module using pip.
     To install wikipedia module run this code."""
import sys,time
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install','wikipedia'])

#To check if installed
reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if "wikipedia" in installed_packages:
    print("Wikipedia installed Successfully")
else:
    print("Unsuccessful")
time.sleep(0.7)
  
