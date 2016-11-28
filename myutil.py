__version__ = '0.1.1'

import os
import errno
import json
import shutil
import urllib2
from PIL import Image

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def make_dirs(folders_list):
    for f in folders_list:
        make_sure_path_exists(f)

def clean(folder):
    shutil.rmtree(folder)
    
def clean_folders(folders_list):
    for f in folders_list:
        shutil.rmtree(f)
    
def empty(folder):
    shutil.rmtree(folder)
    make_sure_path_exists(folder)
    
def empty_folders(folders_list):
    for f in folders_list:
        empty(f)
        
def copy(src, dst):
    make_sure_path_exists(dst)
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

def copytree(src, dst, symlinks=False, ignore=None):
    make_sure_path_exists(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
            
def copy_folder(src, dst, SKIP_FILES=[], check_dst=True):
    if check_dst:
        make_sure_path_exists(dst)
    for fn in os.listdir(src):
        if fn not in SKIP_FILES:
            infile = os.path.join(src, fn)
            if os.path.isfile(src + fn):
                outfile = os.path.join(dst, fn)
                shutil.copy2(infile, outfile)

def resize(src, dst, fn, size, check_dst=True):
    if check_dst:
        make_sure_path_exists(dst)
    infile = os.path.join(src, fn)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    outfile = os.path.join(dst, fn)
    im.save(outfile)

def resize_folder(src, dst, size, check_dst=True):
    if check_dst:
        make_sure_path_exists(dst)
    for fn in os.listdir(src):
        resize(src, dst, fn, size, False)

def crop(src, dst, fn, bounds, check_dst=True):
    if check_dst:
        make_sure_path_exists(dst)
    infile = os.path.join(src, fn)
    outfile = os.path.join(dst, fn)
    im = Image.open(infile)
    im.crop(bounds).save(outfile)

def crop_folder(src, dst, bounds, check_dst=True):
    if check_dst:
        make_sure_path_exists(dst)
    for fn in os.listdir(src):
        crop(src, dst, fn, bounds, False)

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def format_num(x):
    if x == int(x):
        return int(x)
    else:
        return x

def download_file_from(url, dst):
    response = urllib2.urlopen(url)
    with open(dst, 'w') as f:
        f.write(response.read())

def open_json(src):
    with open(src, 'r') as f:
        return json.loads(f.read())

def write_json(data, dst):
    with open(dst, 'w') as f:
        f.write(json.dumps(data, indent=1, sort_keys=True))
        
def subset(KEYS, bigdict):
    output = {k: bigdict[k] for k in KEYS if k in bigdict and bigdict[k]}
    return output
