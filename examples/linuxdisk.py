from littlefs import LittleFS, UserContextLinuxDisk

disk_path = 'examples/img'


fs = LittleFS(block_size=512, block_count=302, mount=False, context= UserContextLinuxDisk(disk_path))

fs.format()
fs.mount()

fs.mkdir('/test')
fs.mkdir('/test/dir')
fs.mkdir('/test/dir/subdir')
    