# seven_segment_reader
When using a PID controller you often use seven segment displays, this code will obtain the data from the PID (temperature)controller

simply extract the files into a folder, in reader.py change the needed variables (line 12 to 22).
then run the code and proceed. 
First it asks you to crop the (first) image manually and then select where the segments are. 
The code will loop over the rest for the same location.
If you get an error about the segment placement, it may be due to lighting.
Enable troubleshooting (by setting it to True) and play with the alpha and beta parameters for contrast.
Enjoy :)
