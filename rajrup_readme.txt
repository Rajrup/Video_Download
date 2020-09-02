# Repo Setup
conda create --name vid_download python=3.7
sudo apt-get install streamlink


streamlink -o output.mp4 --hls-duration 01:30 https://58cc2dce193dd.streamlock.net/live/16_E_Madison_EW.stream/playlist.m3u8 best -> Downloads stream to file output.mp4 for duration ~ [hh:]:mm:ss

URL from Video DownloadHelper addon in firefox. Video link -> Details -> masterManifest field (ending with playlist)

State cameras
Seattle cameras: https://web6.seattle.gov/travelers/
NJ Traffic Cameras: https://511nj.org/home

STREETS: A Novel Camera Network Dataset for Traffic Flow (Direct Download but only images every 10 sec) -> https://databank.illinois.edu/datasets/IDB-3671567

Earth Cam:
https://www.earthcam.com/usa/california/losangeles/hollywoodblvd/?cam=hollywoodblvd -> LA, Hollywood Blvd
https://www.earthcam.com/usa/newyork/timessquare/?cam=tsstreet -> NYC
https://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1 -> NYC
https://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo3 -> NYC
https://www.earthcam.com/usa/newjersey/seasideheights/?cam=seasideheights2 -> NJ
https://www.earthcam.com/usa/louisiana/neworleans/bourbonstreet/?cam=catsmeow2 -> louisiana
https://www.earthcam.com/usa/louisiana/neworleans/bourbonstreet/?cam=bourbonstreet -> louisiana
https://www.earthcam.com/usa/kentucky/hyden/?cam=hyden -> kentucky
https://www.earthcam.com/usa/illinois/chicago/wrigleyfield/?cam=wrigleyfield_hd -> chicago
https://www.earthcam.com/usa/illinois/chicago/wrigleyville/?cam=wrigleyville -> chicago
https://www.earthcam.com/usa/florida/watersound/?cam=watersoundbeach -> florida beach
https://www.earthcam.com/usa/florida/miamiandthebeaches/?cam=miamibeach9 -> miamibeach
https://www.earthcam.com/usa/florida/keywest/?cam=irishkevins > keywest, florida

https://www.earthcam.com/search/ft_search.php?term=traffic -> list of all traffic cameras
https://www.earthcam.com/search/ft_search.php?term=pedestrian -> list of all pedestrian cameras

