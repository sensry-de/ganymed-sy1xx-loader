import os
from sry_gnm_sy1xx_bl import SryGnmSy1xxBL

# define the file to be uploaded
coreguard_bin = os.path.join("bin", "coreguard-bl.bin")
application_bin = os.path.join("bin", "zephyr_demo_app.bin")

# create the loader
flash = SryGnmSy1xxBL()

# connect to serial
flash.connect("/dev/ttyUSB0")

# convert binary to application ganymed image
application_gnm = flash.convert_zephyr_bin(application_bin)

# set the controller into bootloader mode
flash.enter_loading_mode()

# clear the internal flash
flash.clear_mram()

# write the new binaries
flash.write_mram(coreguard_bin, application_gnm)

print("done")
