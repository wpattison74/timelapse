# timelapse
Timelapse scripts utilizing the Raspberry Pi platform and camera module.

Current specs:  Raspberry Pi Zero W (Rev. 1) and the Pi Camera Module
                
1. Create a mount point for a storage location at /mnt/timelapse.
2. Setup timelapse.py as a service. (Adjust WAIT_TIME in script for frequency.)
3. Use 'convert_to_mp4.sh' to process all the images into an MP4.

Output is ~1.1MB/photo when at 1920x1080 resolution.
