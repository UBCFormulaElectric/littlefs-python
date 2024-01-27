from littlefs import LittleFS, UserContextWinDisk

disk_path = r"\\.\D: " # assume F drive is your storage device for littlefs


fs = LittleFS(block_size=512, block_count=30228480, mount=False, context=UserContextWinDisk(disk_path))

fs.mount()
fs.format()

files = fs.listdir('/')
for file in files:    
    with fs.open(file, 'rb') as fh:
        data = fh.read(1000)
        print(file)
        print(data)
    
with fs.open("canMsg", 'rb') as fh:
    # dump all can messages to a binary file to another storage devic
    with open("canMsg", 'wb+') as f:
        f.write(fh.read())