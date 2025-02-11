import os
from lib.flash import Flash


flash = Flash()

zephyr_gnm = flash.convert_zephyr_bin(os.path.join("bin", "zephyr_demo_app.bin"))

flash.connect("/dev/ttyUSB0")

flash.enter_loading_mode()

flash.clear_mram()

info = {
    "kernel_file": os.path.join("bin", "coreguard-bl.bin"),
    "ota_app_file": zephyr_gnm,
    "toc_file": "",
    "user_file": "",
}

flash.write_mram(info)
