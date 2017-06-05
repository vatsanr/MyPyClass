"""utility that merges three files into a simgle file"""

import datetime
import glob2

filenames=glob2.glob("*.txt")
with open (datetime.datetime.now().strftime("%Y-%m-%d-%h-%M-%S-%f")+".txt",'w') as file:
      for filename in filenames:
          with open(filename,'r') as f:
                file.write(f.read()+"\n")
