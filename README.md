
BLELS - Bluetooth Low Energy (BLE) List Python Script
=====================================================

This is a simple python CLI script to scan for BLE devices and print out their attributes (and values if readable).
This has been tested on Linux and depends on *bluepy* - so most likely won't run on Windows


Installation
------------
1. Install `python3`, `pip3`
2. Install `bluepy` using pip3: `pip3 install bluepy`
3. Mark ble-ls.py as executable: `chmod +x ble-ls.py`


Usage
-----
1. Run the script with sudo to enable BLE scanning: `sudo ./ble-ls.py`. If you prefer not to run the app with sudo, find out the MAC addresses of your devices from bluetoothctl then use option #2 directly
2. Use `scan` to scan for devices (defaults to 10 seconds, or pass in a duration), and use `ls` to read the attributes (Lists services and tries to read characteristics)

scan will show you something formatted like this:
```
> 1
scan: starting scan for 10s
scan: Device 54:bd:00:00:00:00 [[TV] LT320000] (public), Connect=True, RSSI=-88 dB
scan: Device 24:c5:00:00:00:00 [None] (random), Connect=False, RSSI=-90 dB
scan: Device 71:5c:00:00:00:00 [None] (random), Connect=True, RSSI=-92 dB
scan: Complete, found 6 devices, 1 public
> 
```

If you like one of those *Connect=True* devices, go ahead and use ls with that MAC address. You should see the output formatted like so:
```
Listing services...
   -- SERVICE: 00001800-0000-1000-8000-00805f9b34fb [Generic Access]
   --   --> CHAR: 00002a00-0000-1000-8000-00805f9b34fb, Handle: 3 (0x0003) - READ WRITE  - [Device Name]
   --   --> CHAR: 00002a01-0000-1000-8000-00805f9b34fb, Handle: 5 (0x0005) - READ  - [Appearance]
   --   --> CHAR: 00002a04-0000-1000-8000-00805f9b34fb, Handle: 7 (0x0007) - READ  - [Peripheral Preferred Connection Parameters]
   -- SERVICE: 00001801-0000-1000-8000-00805f9b34fb [Generic Attribute]
   -- SERVICE: 0000180a-0000-1000-8000-00805f9b34fb [Device Information]
   --   --> CHAR: 00002a23-0000-1000-8000-00805f9b34fb, Handle: 11 (0x000b) - READ  - [System ID]
   --   --> CHAR: 00002a26-0000-1000-8000-00805f9b34fb, Handle: 13 (0x000d) - READ  - [Firmware Revision String]
   --   --> CHAR: 00002a29-0000-1000-8000-00805f9b34fb, Handle: 15 (0x000f) - READ  - [Manufacturer Name String]
   -- SERVICE: 0000ffe0-0000-1000-8000-00805f9b34fb [ffe0]
   --   --> CHAR: 0000ffe4-0000-1000-8000-00805f9b34fb, Handle: 18 (0x0012) - NOTIFY  - [ffe4]
   -- SERVICE: 0000ffe5-0000-1000-8000-00805f9b34fb [ffe5]
   --   --> CHAR: 0000ffe9-0000-1000-8000-00805f9b34fb, Handle: 23 (0x0017) - WRITE NO RESPONSE WRITE  - [ffe9]
... etc ...
Listing descriptors...
   --  DESCRIPTORS: 00002800-0000-1000-8000-00805f9b34fb, [Primary Service Declaration], Handle: 1 (0x0001)
   --  DESCRIPTORS: 00002803-0000-1000-8000-00805f9b34fb, [Characteristic Declaration], Handle: 2 (0x0002)
   --  DESCRIPTORS: 00002a00-0000-1000-8000-00805f9b34fb, [Device Name], Handle: 3 (0x0003)
   --  DESCRIPTORS: 00002803-0000-1000-8000-00805f9b34fb, [Characteristic Declaration], Handle: 4 (0x0004)
   --  DESCRIPTORS: 00002a01-0000-1000-8000-00805f9b34fb, [Appearance], Handle: 5 (0x0005)
   --  DESCRIPTORS: 00002803-0000-1000-8000-00805f9b34fb, [Characteristic Declaration], Handle: 6 (0x0006)
   --  DESCRIPTORS: 00002a04-0000-1000-8000-00805f9b34fb, [Peripheral Preferred Connection Parameters], Handle: 7 (0x0007)
... etc ...
Reading characteristics...
  -- READ: 00002a00-0000-1000-8000-00805f9b34fb [Device Name] (0x0003), None, Value: b'REV-90000'
  -- READ: 00002a01-0000-1000-8000-00805f9b34fb [Appearance] (0x0005), None, Value: b'\x00\x00'
  -- READ: 00002a04-0000-1000-8000-00805f9b34fb [Peripheral Preferred Connection Parameters] (0x0007), None, Value: b'\x10\x00 \x00\x00\x00\x90\x01'
  -- READ: 00002a23-0000-1000-8000-00805f9b34fb [System ID] (0x000b), None, Value: b'\x1c\x0f1\x00\x00\x00\x00!'
  -- READ: 00002a26-0000-1000-8000-00805f9b34fb [Firmware Revision String] (0x000d), None, Value: b'V0.20_V0.0\x00\x00'
  -- READ: 00002a29-0000-1000-8000-00805f9b34fb [Manufacturer Name String] (0x000f), None, Value: b'REV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
  -- READ: 0000ffe4-0000-1000-8000-00805f9b34fb [ffe4] (0x0012), None, Value: 
... etc ...
```

