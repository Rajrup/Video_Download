import os 
from tqdm import tqdm
import re
import pickle
import datetime
import multiprocessing as mp

N_CPU = 7
DURATION = '20:00'

def oscall(command):
    print("Command: ", command)
    try:
        os.system(command) #download file 
    except:
        print("Failed Command: ", command)

def download_data(url_file, out_folder):

    with open('stream_urls.txt') as f:
        urls = f.read().splitlines()
        url_tags = [re.split('/|\.', l)[-4] for l in urls]
    print("URLS: ", urls)
    print("URL TAGS: ", url_tags)

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    failed_file_list=[]
    for url, url_tag in tqdm(zip(urls, url_tags), total=len(url_tags)):
        out_file = os.path.join(out_folder, url_tag + ".mp4")
        try:
            command = ['streamlink', 
                    '--verbose',
                    '-o', '"%s"' % out_file, '-f',
                    '--hls-duration', '01:30',
                    '"%s"' % url, 'best']
            command = ' '.join(command)
            print(command)
            os.system(command) #download file 
        except:
            failed_file_list.append(url_tag)
    print("Failed files: ", failed_file_list)

    with open(os.path.join(out_folder,"failed_url_tags.pkl"),"wb") as f:
        pickle.dump(failed_file_list,f)


# Download parallely
def download_data_mp(url_file, out_folder, folder_timestamp=False):

    with open('stream_urls.txt') as f:
        urls = f.read().splitlines()
        url_tags = [re.split('/|\.', l)[-4] for l in urls]
    print("URLS: ", urls)
    print("URL TAGS: ", url_tags)

    if folder_timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
        out_folder = os.path.join(out_folder, timestamp)

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    command_list = []
    for url, url_tag in zip(urls, url_tags):
        out_file = os.path.join(out_folder, url_tag + ".mp4")

        command = ['streamlink', 
                '--verbose',
                '-o', '"%s"' % out_file, '-f',
                '--hls-duration', DURATION,
                '"%s"' % url, 'best']
        command = ' '.join(command)
        command_list.append(command)
    pool = mp.Pool(N_CPU)
    pool.map(oscall, command_list)

if __name__ == '__main__':
    out_folder="/data/rajrup/Project/D2/Video_Download/out_videos"
    url_file="stream_urls.txt"
    download_data_mp(url_file, out_folder, folder_timestamp=True)