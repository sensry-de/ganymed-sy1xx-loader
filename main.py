import os
from lib.flash import Flash

coreguard_bin = os.path.join("bin", "coreguard-bl.bin")
application_bin = os.path.join("bin", "zephyr_demo_app.bin")

flash = Flash()

flash.connect("/dev/ttyUSB0")

# convert binary to application ganymed image
application_gnm = flash.convert_zephyr_bin(application_bin)

flash.enter_loading_mode()

flash.clear_mram()

flash.write_mram(coreguard_bin, application_gnm)
