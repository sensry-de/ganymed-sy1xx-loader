## how to run in linux

prepare 

```
git clone git@github.com:sensry-de/ganymed-sy1xx-loader.git
cd ganymed-sy1xx-loader/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

start flashing the default images from ./bin folder
```
$ python main.py
2025-02-11 16:53:34,656		DEBUG		sy1xx loader process thread started
---generating ganymed image---
source file [bin/zephyr_demo_app.bin]
binary file loaded, size 393780 bytes
writing meta data to [bin/zephyr_demo_app.bin.meta]
destination file [bin/zephyr_demo_app.bin.gnm]
new ganymed image with header created [bin/zephyr_demo_app.bin.gnm]
2025-02-11 16:53:34,669		DEBUG		serial port receive thread started
2025-02-11 16:53:34,669		DEBUG		process response thread started



--- please press reset button if requested!! ---



2025-02-11 16:53:34,669		DEBUG		proc cmd request_loader
2025-02-11 16:53:34,770		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:34,971		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:35,172		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:35,373		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:35,574		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:35,774		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:35,975		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:36,176		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:36,377		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:36,578		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:36,779		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:36,979		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:37,181		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:37,381		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:37,582		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:37,782		DEBUG		reset cb from bootloader requested...
2025-02-11 16:53:37,810		DEBUG		proc cmd init
job done
entered loading mode
2025-02-11 16:53:37,830		DEBUG		proc cmd request_loader
2025-02-11 16:53:37,851		DEBUG		proc cmd image mram
2025-02-11 16:53:37,881		DEBUG		[select] success [ok]
2025-02-11 16:53:37,881		DEBUG		proc cmd clear_mram
job done
finished clearing MRAM
2025-02-11 16:53:48,485		DEBUG		proc cmd request_loader
2025-02-11 16:53:48,515		DEBUG		proc cmd image mram
2025-02-11 16:53:48,545		DEBUG		[select] success [ok]
2025-02-11 16:53:48,546		DEBUG		proc cmd mram_upload bin/coreguard-bl.bin  bin/zephyr_demo_app.bin.gnm
2025-02-11 16:53:48,546		DEBUG		Build MRAM header
2025-02-11 16:53:48,546		DEBUG		Size:          37760
2025-02-11 16:53:48,546		DEBUG		Header located at: 0x1D100000
2025-02-11 16:53:48,546		DEBUG		Image located at: 0x1D100010
2025-02-11 16:53:48,546		DEBUG		050203341000101d8093000001000000
2025-02-11 16:54:52,450		DEBUG		reset cb from bootloader requested...
job done
finished writing to MRAM
```


## run 

* connect USB
* open minicom / putty / ... 
* press reset button



```
$ minicom


Welcome to minicom 2.8

OPTIONS: I18n
Port /dev/serial/by-id/usb-FTDI_FT231X_USB_UART_D30FAJ09-if00-port0, 16:54:48

Press CTRL-A Z for help on special keys


***********************************************************
*                                                         *
* USoC Bootloader                                         *
*                                                         *
* Version :749-9f9bc839ba0632901979138e92d41492f808329e   *
* Build   :Fri, 06 Nov 2020 07:46:17 +0100                *
*                                                         *
***********************************************************

OTP 0x0 0x0
LCS EFUSE 0x101
LCS 0x1
Load image from MRAM
Kernel 0x1d020000
addr   0x1d100010
size   0x9380
Start boot process
Found usoc kernel
Jump to kernel
gpio port0 init started
gpio port0 init finished
i2c init started
i2c0 init done
i2c1 init done
i2c2 init done
i2c3 init done
spi init started
spi0 init done
spi1 init done
spi2 init done
spi3 init done
spi4 init done
spi5 init done
spi6 init done
eth init started
eth0 init done
trng0 configure start
trng0 init complete
trng0 test success - received 300 values

executing core#guard (compatible to openSBI) v1.5 ...
[gloabal mram] unexpected efuse data[0] at addr 0x1D070180
[gloabal mram] expected 0x0, but found 0x5
[gloabal mram] efuse[1] at addr 0x1D070184 is 0xFD798102
[gloabal mram] efuse[2] at addr 0x1D070188 is 0x6404905C
[gloabal mram] efuse[3] at addr 0x1D07018C is 0x440082E
[gloabal mram] efuse[4] at addr 0x1D070190 is 0x1F0001B
[gloabal mram] efuse[5] at addr 0x1D070194 is 0x0
[secure mram] efuse[0] at addr 0x1D070198 is 0x0
[secure mram] efuse[1] at addr 0x1D07019C is 0xFD798102
[secure mram] efuse[2] at addr 0x1D0701A0 is 0x6404905C
[secure mram] efuse[3] at addr 0x1D0701A4 is 0x440082E
[secure mram] efuse[4] at addr 0x1D0701A8 is 0x1F0001B
[secure mram] efuse[5] at addr 0x1D0701AC is 0x0
efuse trim data check -- failed
load from mram mode
MRAM app img> invalid image list header
MRAM app img> initialize image list ...
MRAM app img> found OTA image ...
initialized image list
loading image failed
load from mram mode
found bootable image
Load app image from secure MRAM
MRAM app img> start to copy image...
jumping tostarting sys_timer
timer [32768] expected 1000 (33)
*** Booting Zephyr OS build v3.6.0-18408-g71750fdc8b2b ***
entered main();
--- booted --- 12

uart:~$
```