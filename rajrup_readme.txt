conda create --name vid_download python=3.7
sudo apt-get install streamlink


streamlink -o output.mp4 --hls-duration 01:30 https://58cc2dce193dd.streamlock.net/live/16_E_Madison_EW.stream/playlist.m3u8 best -> Downloads stream to file output.mp4 for duration ~ [hh:]:mm:ss
