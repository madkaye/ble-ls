#!/usr/bin/env python3

import datetime
from bluepy import btle
from bluepy.btle import Scanner, Peripheral, Characteristic, ScanEntry, UUID

class BLELS:

    SCAN_TIMEOUT = 10
    scanner = None
    publicdevices = []

    def scan(self, duration=SCAN_TIMEOUT):
        try:
            print("scan: starting scan for {}s".format(duration))
            self.scanner = Scanner()
            devices = self.scanner.scan(duration)
            foundDevices = 0
            for dev in devices:
                devname = dev.getValueText(btle.ScanEntry.COMPLETE_LOCAL_NAME)
                if devname is None:
                    devname = dev.getValueText(btle.ScanEntry.SHORT_LOCAL_NAME)

                print("scan: Device {} [{}] ({}), Connect={}, RSSI={} dB".format(dev.addr, devname, dev.addrType,
                                                                                 dev.connectable, dev.rssi))

                # for (adtype, desc, value) in dev.getScanData():
                #    print("  %s = %s" % (desc, value))
                
                if dev.addrType == btle.ADDR_TYPE_PUBLIC:
                    foundDevices = foundDevices + 1
                    self.publicdevices.append(dev)

            print("scan: Complete, found {} devices, {} public".format(len(devices), len(self.publicdevices)))

        except Exception as e:
            print("scan: Error, ", e)

    def connectandread(self, addr):
        try:

            peri = Peripheral()
            peri.connect(addr)

            print("Listing services...")
            services = peri.getServices()
            for serv in services:
                print("   -- SERVICE: {} [{}]".format(serv.uuid, UUID(serv.uuid).getCommonName()))
                characteristics = serv.getCharacteristics()
                for chara in characteristics:
                    print("   --   --> CHAR: {}, Handle: {} (0x{:04x}) - {} - [{}]".format(chara.uuid,
                                                                                    chara.getHandle(),
                                                                                    chara.getHandle(),
                                                                                    chara.propertiesToString(),
                                                                                    UUID(chara.uuid).getCommonName()))
            print("Listing descriptors...")
            descriptors = peri.getDescriptors()
            for desc in descriptors:
                print("   --  DESCRIPTORS: {}, [{}], Handle: {} (0x{:04x})".format(desc.uuid, 
                                                                                    UUID(desc.uuid).getCommonName(),
                                                                                    desc.handle, desc.handle))
            
            print("Reading characteristics...")
            chars = peri.getCharacteristics()
            for c in chars:
                print("  -- READ: {} [{}] (0x{:04x}), {}, Value: {}".format(c.uuid, UUID(c.uuid).getCommonName(),
                                                                c.getHandle(), c.descs, c.read() if c.supportsRead() else ""))


        except Exception as e:
            print("connectandread: Error,", e)


if __name__ == '__main__':


    print("BLE LS Script ---")
    print("--------------------")
    print("scan [duration]     : Scan")
    print("ls <ADDRESS>        : Read attributes for device")
    print("q                   : Quit")

    while True:
        choice = input("> ")
        choice = choice.lower()
        
        
        if choice.startswith('q'):
            print("exiting...")
            break
        elif choice.startswith('scan'):
            duration = 10
            if len(choice) > 2: 
                args = choice.split(' ', 2)
                if len(args) == 2 and 0 < int(args[1]) < 60:
                    duration = int(args[1])
            BLELS().scan(duration)
            continue
        elif choice.startswith('ls'):
            addr = ''
            if len(choice) > 2: 
                args = choice.split(' ', 2)
                if len(args) == 2:
                    addr = args[1]
            if len(addr) != 17:
                print ("Bad address, expecting 17 characters, got:", addr)
                continue
            BLELS().connectandread(addr)
            continue
        elif choice.startswith('t'):
            print("time is {}".format(datetime.date.isoformat(datetime.date.today())))
            continue
        else:
            print("Unknown option:", choice)
            continue
        
    print("--------------------")
    print("Goodbye!")

    






