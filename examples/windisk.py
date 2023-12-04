from littlefs import LittleFS, UserContextWinDisk

disk_path = r"\\.\F: " # assume F drive is your storage device for littlefs


fs = LittleFS(block_size=512, block_count=30228480, mount=False, context=UserContextWinDisk(disk_path))

fs.mount()

print(fs.listdir('/'))
with fs.open('deadbeef.txt', 'rb') as fh:
    data = fh.read()
    # save data to as binary file
    with open('deadbeef.bin', 'wb') as f:
        f.write(data)
    