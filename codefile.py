{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "21302815",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import os, shutil\n",
    "import cv2\n",
    "import matplotlib.image as mpimg\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "plt.style.use('ggplot')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b5ec71dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dataset\n",
    "import zipfile\n",
    "\n",
    "z = zipfile.ZipFile('archive.zip')\n",
    "\n",
    "z.extractall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a018ad1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All files are renamed in the yes dir.\n"
     ]
    }
   ],
   "source": [
    "folder = 'brain_tumor_dataset/yes/'\n",
    "count = 1\n",
    "\n",
    "for filename in os.listdir(folder):\n",
    "    source = folder + filename\n",
    "    destination = folder + \"Y_\" +str(count)+\".jpg\"\n",
    "    os.rename(source, destination)\n",
    "    count+=1\n",
    "print(\"All files are renamed in the yes dir.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b6066946",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All files are renamed in the no dir.\n"
     ]
    }
   ],
   "source": [
    "folder = 'brain_tumor_dataset/no/'\n",
    "count = 1\n",
    "\n",
    "for filename in os.listdir(folder):\n",
    "    source = folder + filename\n",
    "    destination = folder + \"N_\" +str(count)+\".jpg\"\n",
    "    os.rename(source, destination)\n",
    "    count+=1\n",
    "print(\"All files are renamed in the no dir.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2f9f8f85",
   "metadata": {},
   "outputs": [],
   "source": [
    "# EDA(Exploratory Data Analysis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3fcefd1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "155\n",
      "98\n"
     ]
    }
   ],
   "source": [
    "listyes = os.listdir(\"brain_tumor_dataset/yes/\")\n",
    "number_files_yes = len(listyes)\n",
    "print(number_files_yes)\n",
    "\n",
    "listno = os.listdir(\"brain_tumor_dataset/no/\")\n",
    "number_files_no = len(listno)\n",
    "print(number_files_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "382182c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "35d28e81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x504 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data = {'tumorous': number_files_yes, 'non-tumorous': number_files_no}\n",
    "\n",
    "typex = data.keys()\n",
    "values = data.values()\n",
    "\n",
    "fig = plt.figure(figsize=(5,7))\n",
    "\n",
    "plt.bar(typex, values, color=\"red\")\n",
    "\n",
    "plt.xlabel(\"Data\")\n",
    "plt.ylabel(\"No of Brain Tumor Images\")\n",
    "plt.title(\"Count of Brain Tumor Images\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58febde6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data Augmentation\n",
    "# 155(61%), 98(39%)\n",
    "# imbalance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3a56a756",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
    "from tensorflow.keras.models import Model\n",
    "from tensorflow.keras.layers import Flatten, Dense, Dropout\n",
    "from tensorflow.keras.applications.vgg19 import VGG19\n",
    "from tensorflow.keras.optimizers import SGD, Adam\n",
    "from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b1498e40",
   "metadata": {},
   "outputs": [],
   "source": [
    "def timing(sec_elapsed):\n",
    "    h = int(sec_elapsed / (60*60))\n",
    "    m = int(sec_elapsed % (60*60) / 60)\n",
    "    s = sec_elapsed % 60\n",
    "    return f\"{h}:{m}:{s}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e114ab2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def augmented_data(file_dir, n_generated_samples, save_to_dir):\n",
    "    data_gen = ImageDataGenerator(rotation_range=10, \n",
    "                      width_shift_range=0.1,\n",
    "                      height_shift_range=0.1,\n",
    "                      shear_range=0.1,\n",
    "                      brightness_range=(0.3, 1.0),\n",
    "                      horizontal_flip=True,\n",
    "                      vertical_flip=True,\n",
    "                      fill_mode='nearest')\n",
    "    for filename in os.listdir(file_dir):\n",
    "        image = cv2.imread(file_dir + '/' + filename)\n",
    "        image = image.reshape((1,) + image.shape)\n",
    "        save_prefix = 'aug_' + filename[:-4]\n",
    "        i=0\n",
    "        for batch in data_gen.flow(x = image, batch_size = 1, save_to_dir = save_to_dir, save_prefix = save_prefix, save_format = \"jpg\"):\n",
    "            i+=1\n",
    "            if i>n_generated_samples:\n",
    "                break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e4333ce9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0:1:53.09810137748718\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "start_time = time.time()\n",
    "\n",
    "yes_path = 'brain_tumor_dataset/yes' \n",
    "no_path = 'brain_tumor_dataset/no'\n",
    "\n",
    "augmented_data_path = 'augmented_data/'\n",
    "\n",
    "augmented_data(file_dir = yes_path, n_generated_samples=6, save_to_dir=augmented_data_path+'yes')\n",
    "augmented_data(file_dir = no_path, n_generated_samples=9, save_to_dir=augmented_data_path+'no')\n",
    "\n",
    "end_time = time.time()\n",
    "execution_time = end_time - start_time\n",
    "print(timing(execution_time))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1d36bf03",
   "metadata": {},
   "outputs": [],
   "source": [
    "def data_summary(main_path):\n",
    "    yes_path = \"augmented_data/yes/\" \n",
    "    no_path = \"augmented_data/no/\"\n",
    "    \n",
    "    n_pos = len(os.listdir(yes_path))\n",
    "    n_neg = len(os.listdir(no_path))\n",
    "    \n",
    "    n = (n_pos + n_neg)\n",
    "    \n",
    "    pos_per = (n_pos*100)/n\n",
    "    neg_per = (n_neg*100)/n\n",
    "    \n",
    "    print(f\"Number of sample: {n}\")\n",
    "    print(f\"{n_pos} Number of positive sample in percentage: {pos_per}%\")\n",
    "    print(f\"{n_neg} Number of negative sample in percentage: {neg_per}%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "62f13fd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of sample: 2064\n",
      "1085 Number of positive sample in percentage: 52.56782945736434%\n",
      "979 Number of negative sample in percentage: 47.43217054263566%\n"
     ]
    }
   ],
   "source": [
    "data_summary(augmented_data_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "930c420c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1085\n",
      "979\n"
     ]
    }
   ],
   "source": [
    "listyes = os.listdir(\"augmented_data/yes/\")\n",
    "number_files_yes = len(listyes)\n",
    "print(number_files_yes)\n",
    "\n",
    "listno = os.listdir(\"augmented_data/no/\")\n",
    "number_files_no = len(listno)\n",
    "print(number_files_no)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "d535d0c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x504 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data = {'tumorous': number_files_yes, 'non-tumorous': number_files_no}\n",
    "\n",
    "typex = data.keys()\n",
    "values = data.values()\n",
    "\n",
    "fig = plt.figure(figsize=(5,7))\n",
    "\n",
    "plt.bar(typex, values, color=\"red\")\n",
    "\n",
    "plt.xlabel(\"Data\")\n",
    "plt.ylabel(\"No of Brain Tumor Images\")\n",
    "plt.title(\"Count of Brain Tumor Images\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14b3df86",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d91bf16",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert BGR TO GRAY\n",
    "# GaussianBlur\n",
    "# Threshold\n",
    "# Erode\n",
    "# Dilate\n",
    "# Find Contours"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "0576e87c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import imutils\n",
    "def crop_brain_tumor(image, plot=False):\n",
    "    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "    gray = cv2.GaussianBlur(gray, (5,5), 0)\n",
    "    \n",
    "    thres = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]\n",
    "    thres =cv2.erode(thres, None, iterations = 2)\n",
    "    thres = cv2.dilate(thres, None, iterations = 2)\n",
    "    \n",
    "    cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n",
    "    cnts = imutils.grab_contours(cnts)\n",
    "    c = max(cnts, key = cv2.contourArea)\n",
    "    \n",
    "    extLeft = tuple(c[c[:,:,0].argmin()][0])\n",
    "    extRight = tuple(c[c[:,:,0].argmax()][0])\n",
    "    extTop = tuple(c[c[:,:,1].argmin()][0])\n",
    "    extBot = tuple(c[c[:,:,1].argmax()][0])\n",
    "    \n",
    "    new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]] \n",
    "    \n",
    "    if plot:\n",
    "        plt.figure()\n",
    "        plt.subplot(1, 2, 1)\n",
    "        plt.imshow(image)\n",
    "        \n",
    "        plt.tick_params(axis='both', which='both', \n",
    "                        top=False, bottom=False, left=False, right=False,\n",
    "                        labelbottom=False, labeltop=False, labelleft=False, labelright=False)\n",
    "        \n",
    "        plt.title('Original Image')\n",
    "            \n",
    "        plt.subplot(1, 2, 2)\n",
    "        plt.imshow(new_image)\n",
    "\n",
    "        plt.tick_params(axis='both', which='both', \n",
    "                        top=False, bottom=False, left=False, right=False,\n",
    "                        labelbottom=False, labeltop=False, labelleft=False, labelright=False)\n",
    "\n",
    "        plt.title('Cropped Image')\n",
    "        plt.show()\n",
    "    return new_image\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "684dd5b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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nMCuXbvW/QQCgfPXoH8FxXmGu6Ref/31rgyagwcP4pZbbnEZ/2uuuQbpdNqAEADI5/Ou4PGePXuQy+We0TWPPPII/uAP/sDl4VBmjh49ilqthqmpKdx2222uOt9+++3PqI3aDi3Dw8O4+uqr132mKPU73/kOfviHfxjj4+NIJpPGy1Vvbt++fS6vgp4fyyOPPILl5WVs2bLF1dbPfe5zOHr06LNqy3MtFzT347/9t/+G2267Dd/zPd+D3/7t38aVV16J2dlZ/P7v/z7uvvtu/N3f/R2i0egzeuZ//I//ET/2Yz+Gm266CXfeeSe++c1v4i//8i8BPHsEDKwi7kKhgE9/+tN4xStegfvuuw+f+tSnnvXznmvZu3cvPv/5z+P2229Ht9vFBz7wAXS7XfP97t278QM/8AP4pV/6JfzxH/8x8vk8Pv7xj6NWq5l+SCQSeN/73of3ve998Pl8eNWrXoVOp4MnnngCjz76qEEml8q5ld27d8Pv9+Opp57C6173urNef66e2wtRer0efv3Xfx1vfOMb1303PDzs8qqej/JMvblWq4VXv/rVuP322/EXf/EXGBoaArAKFNSbO9uc7vV6SKfTeOSRR9Z95+XZno9yQTnd7du349vf/jZuvvlm/MIv/AJ27tyJO++8E0tLS3jggQfwfd/3fc/4ma973evwe7/3e/jIRz6C/fv34/Of/zw++MEPAgAikcizrutrX/ta/MZv/Abe9773Yf/+/fjf//t/46Mf/eizft5zLX/xF3+BXq+Hm266CT/0Qz+E7/u+78ONN9647pqrrroKd955J17+8pdjy5Yt+N7v/V5XP7z//e/HJz7xCfzpn/4prrnmGtx+++34/d//fezYseM8t+i7vwwMDODOO+/EH/3RH3mmEq6srKDZbG54/5VXXokHH3zQpVQee+wxVKtVXHXVVeazQqGA48ePm/+PHDmChYUFF61xtmtuuOEGHDx40NPDSSQSSKVS2LJlC775zW+66nj//fc/gx559uXpp59GoVDA7/zO7+DlL3859u3bh3K57PImrrjiCjz99NOuvj58+DAqlYr5/4YbbkClUsHi4uK6dp4tPvSClQsWwjuP5bd+67ecbDZ7oatxwUun03F27drlvOtd77rQVflXW06fPu2MjY2Z7IGDBw86R48edT772c86V199tfPoo486jrM+wu84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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "array([[[ 2,  2,  2],\n",
       "        [ 2,  2,  2],\n",
       "        [ 2,  2,  2],\n",
       "        ...,\n",
       "        [10, 10, 10],\n",
       "        [ 8,  8,  8],\n",
       "        [ 6,  6,  6]],\n",
       "\n",
       "       [[ 3,  3,  3],\n",
       "        [ 3,  3,  3],\n",
       "        [ 3,  3,  3],\n",
       "        ...,\n",
       "        [10, 10, 10],\n",
       "        [ 7,  7,  7],\n",
       "        [ 5,  5,  5]],\n",
       "\n",
       "       [[ 4,  4,  4],\n",
       "        [ 4,  4,  4],\n",
       "        [ 4,  4,  4],\n",
       "        ...,\n",
       "        [ 4,  4,  4],\n",
       "        [ 3,  3,  3],\n",
       "        [ 2,  2,  2]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[ 7,  7,  7],\n",
       "        [ 3,  3,  3],\n",
       "        [ 3,  3,  3],\n",
       "        ...,\n",
       "        [ 1,  1,  1],\n",
       "        [ 1,  1,  1],\n",
       "        [ 2,  2,  2]],\n",
       "\n",
       "       [[11, 11, 11],\n",
       "        [ 6,  6,  6],\n",
       "        [ 4,  4,  4],\n",
       "        ...,\n",
       "        [ 2,  2,  2],\n",
       "        [ 2,  2,  2],\n",
       "        [ 3,  3,  3]],\n",
       "\n",
       "       [[11, 11, 11],\n",
       "        [12, 12, 12],\n",
       "        [11, 11, 11],\n",
       "        ...,\n",
       "        [ 3,  3,  3],\n",
       "        [ 3,  3,  3],\n",
       "        [ 1,  1,  1]]], dtype=uint8)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img = cv2.imread('augmented_data/yes/aug_Y_1_0_1760.jpg')\n",
    "crop_brain_tumor(img, True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5a27ddf2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "array([[[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]],\n",
       "\n",
       "       [[0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        ...,\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0],\n",
       "        [0, 0, 0]]], dtype=uint8)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img = cv2.imread('augmented_data/no/aug_N_1_0_109.jpg')\n",
    "crop_brain_tumor(img, True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "6d4ca9d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "folder1 = 'augmented_data/no/'\n",
    "folder2 = 'augmented_data/yes/'\n",
    "\n",
    "for filename in os.listdir(folder1):\n",
    "    img = cv2.imread(folder1 + filename)\n",
    "    img = crop_brain_tumor(img, False)\n",
    "    cv2.imwrite(folder1 + filename, img)\n",
    "for filename in os.listdir(folder2):\n",
    "    img = cv2.imread(folder2 + filename)\n",
    "    img = crop_brain_tumor(img, False)\n",
    "    cv2.imwrite(folder2 + filename, img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "689e8158",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "e409128d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# image loading"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b49efa95",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.utils import shuffle\n",
    "def load_data(dir_list, image_size):\n",
    "    X=[]\n",
    "    y=[]\n",
    "    \n",
    "    image_width, image_height=image_size\n",
    "    \n",
    "    for directory in dir_list:\n",
    "        for filename in os.listdir(directory):\n",
    "            image = cv2.imread(directory + '/' + filename)\n",
    "            image = crop_brain_tumor(image, plot=False)\n",
    "            image = cv2.resize(image, dsize=(image_width, image_height), interpolation = cv2.INTER_CUBIC)\n",
    "            image = image/255.00\n",
    "            X.append(image)\n",
    "            if directory[-3:] == \"yes\":\n",
    "                y.append(1)\n",
    "            else:\n",
    "                y.append(0)\n",
    "    X=np.array(X)\n",
    "    y=np.array(y)\n",
    "    \n",
    "    X,y = shuffle(X,y)\n",
    "    print(f\"Number of example is : {len(X)}\")\n",
    "    print(f\"X SHAPE is : {X.shape}\")\n",
    "    print(f\"y SHAPE is : {y.shape}\")\n",
    "    return X,y\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "aa0b69a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of example is : 2064\n",
      "X SHAPE is : (2064, 240, 240, 3)\n",
      "y SHAPE is : (2064,)\n"
     ]
    }
   ],
   "source": [
    "augmented_path = 'augmented_data/'\n",
    "augmeneted_yes = augmented_path + 'yes'\n",
    "augmeneted_no = augmented_path + 'no'\n",
    "\n",
    "IMAGE_WIDTH, IMAGE_HEIGHT = (240,240)\n",
    "\n",
    "X,y = load_data([augmeneted_yes, augmeneted_no], (IMAGE_WIDTH, IMAGE_HEIGHT))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f153af34",
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_sample_images(X, y, n=50):\n",
    "\n",
    "    for label in [0,1]:\n",
    "        images = X[np.argwhere(y == label)]\n",
    "        n_images = images[:n]\n",
    "        \n",
    "        columns_n = 10\n",
    "        rows_n = int(n/ columns_n)\n",
    "\n",
    "        plt.figure(figsize=(20, 10))\n",
    "        \n",
    "        i = 1        \n",
    "        for image in n_images:\n",
    "            plt.subplot(rows_n, columns_n, i)\n",
    "            plt.imshow(image[0])\n",
    "            \n",
    "            plt.tick_params(axis='both', which='both', \n",
    "                            top=False, bottom=False, left=False, right=False,\n",
    "                            labelbottom=False, labeltop=False, labelleft=False,\n",
    "                            labelright=False)\n",
    "            \n",
    "            i += 1\n",
    "        \n",
    "        label_to_str = lambda label: \"Yes\" if label == 1 else \"No\"\n",
    "        plt.suptitle(f\"Brain Tumor: {label_to_str(label)}\")\n",
    "        plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "5c497096",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 1440x720 with 50 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1440x720 with 50 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_sample_images(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "15293708",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data Spliting\n",
    "# Train\n",
    "# Test\n",
    "# Validation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "ebdc1900",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('tumorous_and_nontumorous'):\n",
    "    base_dir = 'tumorous_and_nontumorous'\n",
    "    os.mkdir(base_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "dbdfb5e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('tumorous_and_nontumorous/train'):\n",
    "    train_dir = os.path.join(base_dir , 'train')\n",
    "    os.mkdir(train_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/test'):\n",
    "    test_dir = os.path.join(base_dir , 'test')\n",
    "    os.mkdir(test_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/valid'):\n",
    "    valid_dir = os.path.join(base_dir , 'valid')\n",
    "    os.mkdir(valid_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "e8dd248f",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('tumorous_and_nontumorous/train/tumorous'):\n",
    "    infected_train_dir = os.path.join(train_dir, 'tumorous')\n",
    "    os.mkdir(infected_train_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/test/tumorous'):\n",
    "    infected_test_dir = os.path.join(test_dir, 'tumorous')\n",
    "    os.mkdir(infected_test_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/valid/tumorous'):\n",
    "    infected_valid_dir = os.path.join(valid_dir, 'tumorous')\n",
    "    os.mkdir(infected_valid_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "f9185e4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('tumorous_and_nontumorous/train/nontumorous'):\n",
    "    healthy_train_dir = os.path.join(train_dir, 'nontumorous')\n",
    "    os.mkdir(healthy_train_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/test/nontumorous'):\n",
    "    healthy_test_dir = os.path.join(test_dir, 'nontumorous')\n",
    "    os.mkdir(healthy_test_dir)\n",
    "if not os.path.isdir('tumorous_and_nontumorous/valid/nontumorous'):\n",
    "    healthy_valid_dir = os.path.join(valid_dir, 'nontumorous')\n",
    "    os.mkdir(healthy_valid_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98742ccd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "88af42d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "original_dataset_tumorours = os.path.join('augmented_data','yes/')\n",
    "original_dataset_nontumorours = os.path.join('augmented_data','no/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "2e167e5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/yes/')\n",
    "fnames = []\n",
    "for i in range(0,759):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_tumorours, fname)\n",
    "    dst = os.path.join(infected_train_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "9be665b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/yes/')\n",
    "fnames = []\n",
    "for i in range(759,922):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_tumorours, fname)\n",
    "    dst = os.path.join(infected_test_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "976173ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/yes/')\n",
    "fnames = []\n",
    "for i in range(922,1085):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_tumorours, fname)\n",
    "    dst = os.path.join(infected_valid_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "adb6d8ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 80% 10% 10%"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "be84376b",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/no/')\n",
    "fnames = []\n",
    "for i in range(0,686):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_nontumorours, fname)\n",
    "    dst = os.path.join(healthy_train_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "f1cf3830",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/no/')\n",
    "fnames = []\n",
    "for i in range(686,833):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_nontumorours, fname)\n",
    "    dst = os.path.join(healthy_test_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "b09693a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "files = os.listdir('augmented_data/no/')\n",
    "fnames = []\n",
    "for i in range(833,979):\n",
    "    fnames.append(files[i])\n",
    "for fname in fnames:\n",
    "    src = os.path.join(original_dataset_nontumorours, fname)\n",
    "    dst = os.path.join(healthy_valid_dir, fname)\n",
    "    shutil.copyfile(src, dst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "5364c363",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Model Buliding"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "dbb52104",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_datagen = ImageDataGenerator(rescale = 1./255,\n",
    "                  horizontal_flip=0.4,\n",
    "                  vertical_flip=0.4,\n",
    "                  rotation_range=40,\n",
    "                  shear_range=0.2,\n",
    "                  width_shift_range=0.4,\n",
    "                  height_shift_range=0.4,\n",
    "                  fill_mode='nearest')\n",
    "test_data_gen = ImageDataGenerator(rescale=1.0/255)\n",
    "valid_data_gen = ImageDataGenerator(rescale=1.0/255)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "e5170cef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 1445 images belonging to 2 classes.\n"
     ]
    }
   ],
   "source": [
    "train_generator = train_datagen.flow_from_directory('tumorous_and_nontumorous/train/', batch_size=32, target_size=(240,240), class_mode='categorical',shuffle=True, seed = 42, color_mode = 'rgb')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "2352c260",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 310 images belonging to 2 classes.\n"
     ]
    }
   ],
   "source": [
    "test_generator = train_datagen.flow_from_directory('tumorous_and_nontumorous/test/', batch_size=32, target_size=(240,240), class_mode='categorical',shuffle=True, seed = 42, color_mode = 'rgb')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "c6d8a4c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 309 images belonging to 2 classes.\n"
     ]
    }
   ],
   "source": [
    "valid_generator = train_datagen.flow_from_directory('tumorous_and_nontumorous/valid/', batch_size=32, target_size=(240,240), class_mode='categorical',shuffle=True, seed = 42, color_mode = 'rgb')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "a49d8efe",
   "metadata": {},
   "outputs": [],
   "source": [
    "class_labels = train_generator.class_indices\n",
    "class_name = {value: key for (key,value) in class_labels.items()}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "379b5577",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{0: 'nontumorous', 1: 'tumorous'}"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "396a4748",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "c33de9d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"model_2\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " input_4 (InputLayer)        [(None, 240, 240, 3)]     0         \n",
      "                                                                 \n",
      " block1_conv1 (Conv2D)       (None, 240, 240, 64)      1792      \n",
      "                                                                 \n",
      " block1_conv2 (Conv2D)       (None, 240, 240, 64)      36928     \n",
      "                                                                 \n",
      " block1_pool (MaxPooling2D)  (None, 120, 120, 64)      0         \n",
      "                                                                 \n",
      " block2_conv1 (Conv2D)       (None, 120, 120, 128)     73856     \n",
      "                                                                 \n",
      " block2_conv2 (Conv2D)       (None, 120, 120, 128)     147584    \n",
      "                                                                 \n",
      " block2_pool (MaxPooling2D)  (None, 60, 60, 128)       0         \n",
      "                                                                 \n",
      " block3_conv1 (Conv2D)       (None, 60, 60, 256)       295168    \n",
      "                                                                 \n",
      " block3_conv2 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv3 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv4 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_pool (MaxPooling2D)  (None, 30, 30, 256)       0         \n",
      "                                                                 \n",
      " block4_conv1 (Conv2D)       (None, 30, 30, 512)       1180160   \n",
      "                                                                 \n",
      " block4_conv2 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv3 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv4 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_pool (MaxPooling2D)  (None, 15, 15, 512)       0         \n",
      "                                                                 \n",
      " block5_conv1 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv2 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv3 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv4 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         \n",
      "                                                                 \n",
      " flatten_2 (Flatten)         (None, 25088)             0         \n",
      "                                                                 \n",
      " dense_6 (Dense)             (None, 4608)              115610112 \n",
      "                                                                 \n",
      " dropout_2 (Dropout)         (None, 4608)              0         \n",
      "                                                                 \n",
      " dense_7 (Dense)             (None, 1152)              5309568   \n",
      "                                                                 \n",
      " dense_8 (Dense)             (None, 2)                 2306      \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 140,946,370\n",
      "Trainable params: 120,921,986\n",
      "Non-trainable params: 20,024,384\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "base_model = VGG19(input_shape = (240,240,3), include_top=False, weights='imagenet')\n",
    "\n",
    "for layer in base_model.layers:\n",
    "    layer.trainable=False\n",
    "\n",
    "x=base_model.output\n",
    "flat = Flatten()(x)\n",
    "\n",
    "class_1 = Dense(4608, activation = 'relu')(flat)\n",
    "drop_out = Dropout(0.2)(class_1)\n",
    "class_2 = Dense(1152, activation = 'relu')(drop_out)\n",
    "output = Dense(2, activation = 'softmax')(class_2)\n",
    "\n",
    "model_01 = Model(base_model.input, output)\n",
    "model_01.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "31c18533",
   "metadata": {},
   "outputs": [],
   "source": [
    "# callback\n",
    "filepath = 'model.h5'\n",
    "es = EarlyStopping(monitor='val_loss', verbose = 1, mode='min',patience=4)\n",
    "cp = ModelCheckpoint(filepath, monitor='val_loss', verbose = 1, save_best_only=True, save_weights_only=False, mode='auto',save_freq='epoch')\n",
    "lrr = ReduceLROnPlateau(monitor='val_accuarcy', patience=3, verbose = 1, factor = 0.5, min_lr = 0.0001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "25389e9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "sgd = SGD(learning_rate=0.0001, decay = 1e-6, momentum = 0.9, nesterov = True)\n",
    "model_01.compile(loss='categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "c33e1ff3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/2\n",
      "10/10 [==============================] - ETA: 0s - loss: 0.7502 - accuracy: 0.4906\n",
      "Epoch 1: val_loss improved from 0.73107 to 0.68776, saving model to model.h5\n",
      "WARNING:tensorflow:Learning rate reduction is conditioned on metric `val_accuarcy` which is not available. Available metrics are: loss,accuracy,val_loss,val_accuracy,lr\n",
      "10/10 [==============================] - 195s 21s/step - loss: 0.7502 - accuracy: 0.4906 - val_loss: 0.6878 - val_accuracy: 0.5340 - lr: 1.0000e-04\n",
      "Epoch 2/2\n",
      "10/10 [==============================] - ETA: 0s - loss: 0.7238 - accuracy: 0.5031 \n",
      "Epoch 2: val_loss improved from 0.68776 to 0.68627, saving model to model.h5\n",
      "WARNING:tensorflow:Learning rate reduction is conditioned on metric `val_accuarcy` which is not available. Available metrics are: loss,accuracy,val_loss,val_accuracy,lr\n",
      "10/10 [==============================] - 196s 21s/step - loss: 0.7238 - accuracy: 0.5031 - val_loss: 0.6863 - val_accuracy: 0.5340 - lr: 1.0000e-04\n"
     ]
    }
   ],
   "source": [
    "history_01 = model_01.fit(train_generator, steps_per_epoch=10, epochs = 2, callbacks=[es,cp,lrr], validation_data=valid_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "c6bda9a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtoAAAGhCAYAAABf4xOsAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAAsTAAALEwEAmpwYAAByRElEQVR4nO3dd3gU5drH8e9m0wskm4WEEopBQOUAQmihk5CgIiIiqBQRRBEsgAVRig1FATs25IAgKnbkKEoXIQjhVVBAlCAiAqaSnk3bff/IYQ8RAgkk2ezm97kurmtn9pmZ+9kJT+59cs+MwWaz2RARERERkUrl5ugARERERERckRJtEREREZEqoERbRERERKQKKNEWEREREakCSrRFRERERKqAEm0RERERkSqgRFtEaoU//vgDg8FAUVHRedsuXbqUHj16VHlM/v7+/P7775XetqL2799PREQEuttr2W644QbWrFnj6DBExMko0RaRGqdZs2Z4enqSkpJSav2VV16JwWDgjz/+cEhc3333Hf7+/vj7++Pn54fBYLAv+/v78+eff1Zof9nZ2VxyySWV3raiZs6cyQMPPIDBYABKPn8fH59SfTt+/HiVHLsyvPfee0RERODv70+DBg246qqr2Lp1KwCPPfYYBoOBDz/80N6+qKio1M/RmDFjMBgM7Ny5094mISHB/nkATJs2jRkzZlRPh0TEZSjRFpEaqXnz5rz//vv25Z9//pnc3FwHRgQ9e/YkOzub7Oxs9u3bB0B6erp9XZMmTextyzNzXhOcOHGCTZs2MXjw4FLrV69ebe9XdnY2DRs2LPV+Tenf888/z+TJk3nkkUdITEzkzz//ZOLEiaxatcrexmQyMXv2bIqLi8vcj8lkOmci3blzZzIzM9m1a1elxi8irk2JtojUSKNGjWLZsmX25XfeeYfRo0eXapORkcHo0aOpV68eTZs25amnnsJqtQJQXFzMAw88gNls5pJLLuHLL788Y9tx48bRoEEDGjVqxIwZM86ZiJ3PY489xtChQxk5ciR16tRh6dKl7Ny5k27duhEYGEiDBg24++67KSgosG9jMBhISEgASmZVJ02axDXXXENAQABdunTh0KFDF9R27dq1tGrVirp16zJx4kR69+7N22+/fda4161bR4cOHfD29j5vHw0GAwsXLuTSSy/l0ksvBWDRokW0aNECk8nE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168v1/FERGqzvXv3lvme6rNFRKpPuRLt6Oho/Pz82LhxI6mpqQQHBzN69Gi6du1aroMkJCQQGhpqLz+JjIwkPj7+jES7LP/617/Yt29fudqKiNR2r7/++jnf1zMQRESqR7mfDNmtW7cLviVUWloawcHB9uXg4GAOHjx4RrsdO3bwyy+/0KBBA2699dYK/TJYv369fcZ77ty5F/SLxN3d3aV/Ably/9Q35+XK/XNU3xYuXFjtxxQRkTOVK9H+97//Tffu3WnVqpV93a+//sr27dsr7eliHTt2pHv37nh4eLBu3ToWLlzI7Nmzy719dHQ00dHR9uWUlJQKx3DqPrOuypX7p745L1fu34X2rWHDhlUQjYiIVLdy3XVk27ZthIeHl1p3ySWXsHXr1nIdxGQykZqaal9OTU21X/R4SkBAAB4eHgBERUXx+++/l2vfIiIiIiI1UbkSbYPBgNVqLbXOarWW+/G+4eHhnDhxgqSkJIqKioiLiyMiIqJUm5MnT9pf79q1q9z12yIiIiIiNVG5Skdat27NBx98wMiRI3Fzc8NqtfLhhx/SunXrch3EaDQyduxY5syZg9VqpW/fvoSFhbFy5UrCw8OJiIhgzZo17Nq1C6PRiL+/PxMnTrRvP2vWLI4dO4bFYmHChAlMmDCB9u3bX1CHRURERESqg8FWjmnp1NRU5s6dS3p6ur3mMCgoiGnTppW6yLEmOX78eIW3ceVaUXDt/qlvzsuV+6ca7YrRuF2a+ua8XLl/6tuZzjVml2tGOzg4mGeffZaEhARSU1OpW7cu8fHxPPLII7z55psVDkhERERExNWV+/Z+2dnZJCQksHnzZo4cOcJll11WaXccERERERFxNedMtIuKiti1axebN29mz549hIaG0r17d1JSUpgyZQp169atrjhFRERERJzKORPt8ePH4+bmRu/evRk2bBiXXHIJAGvXrq2W4EREREREnNU5b+/XtGlTcnJySEhI4NChQ2RnZ1dXXCIiIiIiTu2cM9qPPfYYycnJfPvtt6xevZolS5bQtm1b8vPzKS4urq4YRUREREScznkvhqxXrx5Dhw5l6NChHDhwgG+//RaDwcCDDz5I3759GTlyZHXEKSIiIiLiVMp91xEoeXBN69atue2229i5cydbtmypqrhERERERJxahRLtUzw9PenRowc9evSo7HhERERERFzCOS+GFBERERGRC6NEW0RERESkCijRFhERERGpAkq0RURERESqgBJtEREREZEqcEF3HREREde2e/dulixZgtVqJSoqisGDB5d6f+nSpezbtw+AgoICMjIyWLp0KQBz5szh4MGDtG7dmocffriaIxcRqTmUaIuISClWq5XFixczY8YMgoODmT59OhERETRu3NjeZsyYMfbXa9as4fDhw/blQYMGkZ+fz/r166szbBGRGkelIyIiUkpCQgKhoaGEhITg7u5OZGQk8fHxZbbftm1bqecq/Otf/8LHx6c6QhURqdE0oy0iIqWkpaURHBxsXw4ODubgwYNnbZucnExSUhJt2rSp8HHWr19vn/WeO3cuZrO5wvtwd3e/oO2cgfrmvFy5f+pbBfdZqXsTEZFaZdu2bXTt2hU3t4r/gTQ6Opro6Gj7ckpKSoX3YTabL2g7Z6C+OS9X7p/6dqaGDRuW+Z5KR0REpBSTyURqaqp9OTU1FZPJdNa2cXFxdO/evbpCExFxKkq0RUSklPDwcE6cOEFSUhJFRUXExcURERFxRrtjx46Rk5NDy5YtHRCliEjNp9IREREpxWg0MnbsWObMmYPVaqVv376EhYWxcuVKwsPD7Un3tm3biIyMxGAwlNp+1qxZHDt2DIvFwoQJE5gwYQLt27d3QE9ERBxLibaIiJyhQ4cOdOjQodS64cOHl1oeNmzYWbd94oknqiwuERFnotIREREREZEqoERbRERERKQKKNEWEREREakCSrRFRERERKqAEm0RERERkSqgRFtEREREpAoo0RYRERERqQJKtEVEREREqoASbRERERGRKqBEW0RERESkCijRFhERERGpAkq0RURERESqgBJtEREREZEqoERbRERERKQKKNEWEREREakCSrRFRERERKqAEm0RERERkSqgRFtEpAokJBiJjzc4OgwREXEgd0cHICLiCqxW+L//82DtWm+++cabQ4c86NbNyscfOzoyERFxFCXaIiIXKC8PvvvOi7VrvVm3zpuUFCPu7jYiI/MZOzaH4cN9HR2iiIg4kBJtEZEKSEtzY/36kuR682Yv8vLcCAiw0q+fhdhYC3375lOnjg0As9mXlBQHBywiIg6jRFtE5Dz++MPIN994s3atNzt3emK1GmjQoJhhw/IYMMBC1675eHo6OkoREalplGiLiPyD1Qp79njYk+tff/UA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qKgovv32W9q0acOGDRsYOXIkDRs2BKBZs2aljjd48GD8/Pzw8/Pjiiuu4I8//qB9+/a4u7uTnJzMyZMnCQ4OpnXr1tX5MYiIOA2N2+IKlGhLrfDggw+eUeu3efNmTCYTBoPBvq5evXqkpaVx8uRJ/P398fHxsb9nNps5dOgQAKmpqYSEhJR5vMDAQPtrLy8vLBYLUPKL4oMPPuCRRx7Bz8+PgQMH0q9fv8roooiIS9G4La5AibbUamlpadhsNvugnZKSQkREBEFBQWRnZ5OXl2cftFNSUjCZTAAEBweTmJhIkyZNKnS8wMBAJkyYAMCBAwd48sknufzyywkNDa3EXomIuC6N2+JMdB9tqdUyMjJYs2YNRUVFbN++nWPHjnHllVdiNptp1aoV7733HgUFBRw5coRNmzbRs2dPAKKioli5ciUnTpzAZrNx5MgRsrKyznu87du3k5qaCoCfnx9AqZkZERE5N43b4kw0oy21wrPPPlvqfqxt27alU6dOXHrppZw4cYJx48YRGBjI1KlTCQgIAOC+++5j0aJF3Hnnnfj7+3PjjTfa/4w5cOBACgsLeeqpp8jKyqJRo0Y88MAD543j0KFDLF26lNzcXAIDA7ntttvO+adMEZHaSuO2uAKDzWazOToIEUc4dZuoJ5980tGhiIhIOWjcFmej0hERERERkSqgRFtEREREpAqodEREREREpApoRltEREREpAoo0RYRERERqQJKtEVEREREqoASbRERERGRKqBEW0RERESkCvw/+jTS00QB6XUAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 864x432 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot performance\n",
    "fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,6))\n",
    "fig.suptitle(\"Model Training (Frozen CNN)\", fontsize=12)\n",
    "max_epoch = len(history_01.history['accuracy'])+1\n",
    "epochs_list = list(range(1, max_epoch))\n",
    "\n",
    "ax1.plot(epochs_list, history_01.history['accuracy'], color='b', linestyle='-', label='Training Data')\n",
    "ax1.plot(epochs_list, history_01.history['val_accuracy'], color='r', linestyle='-', label='Validation Data')\n",
    "ax1.set_title('Training Accuracy', fontsize=12)\n",
    "ax1.set_xlabel('Epochs', fontsize=12)\n",
    "ax1.set_ylabel('Accuracy', fontsize=12)\n",
    "ax1.legend(frameon=False, loc='lower center', ncol=2)\n",
    "\n",
    "ax2.plot(epochs_list, history_01.history['loss'], color='b', linestyle='-', label='Training Data')\n",
    "ax2.plot(epochs_list, history_01.history['val_loss'], color='r', linestyle='-', label='Validation Data')\n",
    "ax2.set_title('Training Loss', fontsize=12)\n",
    "ax2.set_xlabel('Epochs', fontsize=12)\n",
    "ax2.set_ylabel('Loss', fontsize=12)\n",
    "ax2.legend(frameon=False, loc='upper center', ncol=2)\n",
    "plt.savefig(\"training_frozencnn.jpeg\", format='jpeg', dpi=100, bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "014e47dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('model_weights/'):\n",
    "    os.mkdir('model_weights/')\n",
    "model_01.save_weights(filepath=\"model_weights/vgg19_model_01.h5\", overwrite=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e484eb7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "d80d8286",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 86s 9s/step - loss: 0.6123 - accuracy: 0.6958\n",
      "10/10 [==============================] - 87s 9s/step - loss: 0.7236 - accuracy: 0.4968\n"
     ]
    }
   ],
   "source": [
    "model_01.load_weights(\"model_weights/vgg19_model_01.h5\")\n",
    "vgg_val_eval_01 = model_01.evaluate(valid_generator)\n",
    "vgg_test_eval_01 = model_01.evaluate(test_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "e01a08a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Validation Loss: 0.6123003363609314\n",
      "Validation Acc: 0.6957928538322449\n",
      "Testing Loss: 0.72361820936203\n",
      "Testing Acc: 0.49677419662475586\n"
     ]
    }
   ],
   "source": [
    "print(f'Validation Loss: {vgg_val_eval_01[0]}')\n",
    "print(f'Validation Acc: {vgg_val_eval_01[1]}')\n",
    "print(f'Testing Loss: {vgg_test_eval_01[0]}')\n",
    "print(f'Testing Acc: {vgg_test_eval_01[1]}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa80dcaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "filenames = test_generator.filenames\n",
    "nb_sample = len(filenames)\n",
    "\n",
    "vgg_prediction_01 = model_01.predict(test_generator, steps=nb_sample, verbose = 1)\n",
    "y_pred = np.argmax(vgg_prediction_01, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfe1379a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Increamental unfreezing and fine tuning"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "cdd6b499",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['input_6',\n",
       " 'block1_conv1',\n",
       " 'block1_conv2',\n",
       " 'block1_pool',\n",
       " 'block2_conv1',\n",
       " 'block2_conv2',\n",
       " 'block2_pool',\n",
       " 'block3_conv1',\n",
       " 'block3_conv2',\n",
       " 'block3_conv3',\n",
       " 'block3_conv4',\n",
       " 'block3_pool',\n",
       " 'block4_conv1',\n",
       " 'block4_conv2',\n",
       " 'block4_conv3',\n",
       " 'block4_conv4',\n",
       " 'block4_pool',\n",
       " 'block5_conv1',\n",
       " 'block5_conv2',\n",
       " 'block5_conv3',\n",
       " 'block5_conv4',\n",
       " 'block5_pool']"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "base_model = VGG19(include_top=False, input_shape=(240,240,3))\n",
    "base_model_layer_names = [layer.name for layer in base_model.layers] \n",
    "base_model_layer_names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "e6948ff5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"model_5\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " input_9 (InputLayer)        [(None, 240, 240, 3)]     0         \n",
      "                                                                 \n",
      " block1_conv1 (Conv2D)       (None, 240, 240, 64)      1792      \n",
      "                                                                 \n",
      " block1_conv2 (Conv2D)       (None, 240, 240, 64)      36928     \n",
      "                                                                 \n",
      " block1_pool (MaxPooling2D)  (None, 120, 120, 64)      0         \n",
      "                                                                 \n",
      " block2_conv1 (Conv2D)       (None, 120, 120, 128)     73856     \n",
      "                                                                 \n",
      " block2_conv2 (Conv2D)       (None, 120, 120, 128)     147584    \n",
      "                                                                 \n",
      " block2_pool (MaxPooling2D)  (None, 60, 60, 128)       0         \n",
      "                                                                 \n",
      " block3_conv1 (Conv2D)       (None, 60, 60, 256)       295168    \n",
      "                                                                 \n",
      " block3_conv2 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv3 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv4 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_pool (MaxPooling2D)  (None, 30, 30, 256)       0         \n",
      "                                                                 \n",
      " block4_conv1 (Conv2D)       (None, 30, 30, 512)       1180160   \n",
      "                                                                 \n",
      " block4_conv2 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv3 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv4 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_pool (MaxPooling2D)  (None, 15, 15, 512)       0         \n",
      "                                                                 \n",
      " block5_conv1 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv2 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv3 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv4 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         \n",
      "                                                                 \n",
      " flatten_5 (Flatten)         (None, 25088)             0         \n",
      "                                                                 \n",
      " dense_15 (Dense)            (None, 4608)              115610112 \n",
      "                                                                 \n",
      " dropout_5 (Dropout)         (None, 4608)              0         \n",
      "                                                                 \n",
      " dense_16 (Dense)            (None, 1152)              5309568   \n",
      "                                                                 \n",
      " dense_17 (Dense)            (None, 2)                 2306      \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 140,946,370\n",
      "Trainable params: 125,641,602\n",
      "Non-trainable params: 15,304,768\n",
      "_________________________________________________________________\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "base_model = VGG19(include_top=False, input_shape=(240,240,3))\n",
    "base_model_layer_names = [layer.name for layer in base_model.layers] \n",
    "base_model_layer_names\n",
    "\n",
    "x=base_model.output\n",
    "flat = Flatten()(x)\n",
    "\n",
    "class_1 = Dense(4608, activation = 'relu')(flat)\n",
    "drop_out = Dropout(0.2)(class_1)\n",
    "class_2 = Dense(1152, activation = 'relu')(drop_out)\n",
    "output = Dense(2, activation = 'softmax')(class_2)\n",
    "\n",
    "model_02 = Model(base_model.inputs, output)\n",
    "model_02.load_weights('model_weights/vgg19_model_01.h5')\n",
    "\n",
    "set_trainable=False\n",
    "for layer in base_model.layers:\n",
    "    if layer.name in ['block5_conv4','block5_conv3']:\n",
    "        set_trainable=True\n",
    "    if set_trainable:\n",
    "        layer.trainable=True\n",
    "    else:\n",
    "        layer.trainable=False\n",
    "\n",
    "print(model_02.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "ddbc17a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "sgd = SGD(learning_rate=0.0001, decay = 1e-6, momentum = 0.9, nesterov = True)\n",
    "model_02.compile(loss='categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "ef5b1d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/2\n",
      "10/10 [==============================] - ETA: 0s - loss: 0.5995 - accuracy: 0.7000 \n",
      "Epoch 1: val_loss improved from 0.68627 to 0.60054, saving model to model.h5\n",
      "WARNING:tensorflow:Learning rate reduction is conditioned on metric `val_accuarcy` which is not available. Available metrics are: loss,accuracy,val_loss,val_accuracy,lr\n",
      "10/10 [==============================] - 196s 20s/step - loss: 0.5995 - accuracy: 0.7000 - val_loss: 0.6005 - val_accuracy: 0.6667 - lr: 1.0000e-04\n",
      "Epoch 2/2\n",
      "10/10 [==============================] - ETA: 0s - loss: 0.6371 - accuracy: 0.6438 \n",
      "Epoch 2: val_loss improved from 0.60054 to 0.59865, saving model to model.h5\n",
      "WARNING:tensorflow:Learning rate reduction is conditioned on metric `val_accuarcy` which is not available. Available metrics are: loss,accuracy,val_loss,val_accuracy,lr\n",
      "10/10 [==============================] - 185s 20s/step - loss: 0.6371 - accuracy: 0.6438 - val_loss: 0.5986 - val_accuracy: 0.6990 - lr: 1.0000e-04\n"
     ]
    }
   ],
   "source": [
    "history_02 = model_02.fit(train_generator, steps_per_epoch=10, epochs = 2, callbacks=[es,cp,lrr], validation_data=valid_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "7221a694",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAtoAAAGhCAYAAABf4xOsAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAAsTAAALEwEAmpwYAACeS0lEQVR4nOzdeVxU9f7H8dcMA7INAzMIoqIlWpalVmhmixupZbmluYB77itlKaWiIYqKmfue+4Lmlm23tMzbxcq6ablUYmWmlDIDM+wwc+b3h1d+kUugwAzD5/l43MdtZr7nzPs7gzOf+Z7v+R6V3W63I4QQQgghhChTakcHEEIIIYQQwhVJoS2EEEIIIUQ5kEJbCCGEEEKIciCFthBCCCGEEOVACm0hhBBCCCHKgRTaQgghhBBClAMptIUQVcKvv/6KSqXCarX+Y9v169fz2GOPlXsmX19ffv755zJvW1qnTp0iPDwcWe31xp577jk++OADR8cQQlQyUmgLIZzOHXfcgYeHB2lpacXuf+CBB1CpVPz6668OyfXvf/8bX19ffH198fHxQaVSFd329fXlt99+K9X+srKyqFevXpm3La2pU6cyceJEVCoVcOX19/LyKta3ixcvlstzl4WtW7cSHh6Or68vISEhPPXUU3z++ecATJ8+HZVKxY4dO4raW63WYn9HAwcORKVS8dVXXxW1SUlJKXo9ACZNmsSUKVMqpkNCCJchhbYQwindeeedbNu2rej2999/T05OjgMTweOPP05WVhZZWVmcPHkSgIyMjKL76tSpU9S2JCPnziA1NZVPP/2Url27Frt///79Rf3KysqiZs2axR53lv698cYbTJgwgVdffZU///yT3377jVGjRrFv376iNnq9ntjYWGw22w33o9frb1pIN2/eHIvFwtdff12m+YUQrk0KbSGEU+rXrx8bN24sur1hwwb69+9frI3ZbKZ///5Ur16dunXrMnPmTBRFAcBmszFx4kQCAwOpV68e77333jXbDhkyhJCQEGrVqsWUKVNuWoj9k+nTp9OjRw+ioqLw8/Nj/fr1fPXVVzzyyCP4+/sTEhLCmDFjKCgoKNpGpVKRkpICXBlVHT16NJ06dUKr1fLwww9z9uzZW2r70Ucfcffdd6PT6Rg1ahStWrVizZo118398ccf8+CDD+Lp6fmPfVSpVCxdupQGDRrQoEEDAFavXk39+vXR6/V07ty5aOR77ty5xUbE3d3dGThwIHDz1/7qtJ2JEycSEBDAnXfeecMpG2azmWnTprF06VK6d++Oj48P7u7uPPvss8ybN6+oXceOHfHw8GDz5s037NuAAQP47rvv+Oyzz27YpnXr1tf8HQkhxM1IoS2EcEotWrTAYrFw+vRpbDYb27dvJyoqqlibsWPHYjab+fnnn/nss8/YuHEj69atA64UgO+++y7ffvstX3/9NW+//XaxbQcOHIhGoyElJYVvv/2Wjz766IbFaEnt27ePHj16kJGRQWRkJG5ubixYsIC0tDSOHDnCwYMHWbZs2Q233759O7GxsaSnp1O/fn1ee+21UrdNS0ujR48ezJ49G6PRyN13301ycvIN9/P9999z9913l7iPe/fu5csvv+TUqVN88sknxMTEsGPHDlJTU6lbty69e/cG4JVXXikaDT99+jTVq1enV69ewD+/9l9++SV33303aWlpvPLKKwwZMuS688ePHDlCXl4e3bp1u2lmlUpFXFwcM2bMoLCw8LptvL29efXVV2/6mt9zzz0cP378H18jIYS4SgptIYTTujqq/fHHH3PPPfdQq1atoseuFt+zZ89Gq9Vyxx138NJLL7Fp0yYAduzYwYQJEwgNDUWv1xMTE1O07Z9//sn777/Pm2++iY+PD0FBQURHR7N9+/bbyvvII4/QtWtX1Go1Xl5ePPTQQ7Ro0QKNRsMdd9zB8OHDbzpi2q1bN5o3b45GoyEyMpJjx46Vuu37779Po0aN6N69OxqNhnHjxlGjRo0b7icjIwOtVnvN/V27dsXf3x9/f/9i00piYmLQ6/V4eXmxZcsWBg8ezIMPPki1atWYPXs2R44cKTaHPjc3l65duzJ+/HieeuqpEr32devWZejQobi5uTFgwABSU1P5888/r8loNBoJDAxEo9HcsH9Xde7cmerVq9/0x9Tw4cP57bffbjiCrtVqycjI+MfnEkKIq/7500kIIRykX79+PPHEE/zyyy/XTBtJS0ujsLCQunXrFt1Xt25dLly4AMDFixcJDQ0t9thV586do7CwkJCQkKL7FEUp1v5W/H37n376iRdffJGvv/6anJwcrFYrDz300A23/2tB7O3tTVZWVqnb/r3fKpWK2rVr33A/AQEBZGZmXnP/3r17iYiIuOb+v+774sWLPPjgg0W3fX19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\n",
      "text/plain": [
       "<Figure size 864x432 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot performance\n",
    "fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,6))\n",
    "fig.suptitle(\"Model Training (Frozen CNN)\", fontsize=12)\n",
    "max_epoch = len(history_01.history['accuracy'])+1\n",
    "epochs_list = list(range(1, max_epoch))\n",
    "\n",
    "ax1.plot(epochs_list, history_02.history['accuracy'], color='b', linestyle='-', label='Training Data')\n",
    "ax1.plot(epochs_list, history_02.history['val_accuracy'], color='r', linestyle='-', label='Validation Data')\n",
    "ax1.set_title('Training Accuracy', fontsize=12)\n",
    "ax1.set_xlabel('Epochs', fontsize=12)\n",
    "ax1.set_ylabel('Accuracy', fontsize=12)\n",
    "ax1.legend(frameon=False, loc='lower center', ncol=2)\n",
    "\n",
    "ax2.plot(epochs_list, history_02.history['loss'], color='b', linestyle='-', label='Training Data')\n",
    "ax2.plot(epochs_list, history_02.history['val_loss'], color='r', linestyle='-', label='Validation Data')\n",
    "ax2.set_title('Training Loss', fontsize=12)\n",
    "ax2.set_xlabel('Epochs', fontsize=12)\n",
    "ax2.set_ylabel('Loss', fontsize=12)\n",
    "ax2.legend(frameon=False, loc='upper center', ncol=2)\n",
    "plt.savefig(\"training_frozencnn.jpeg\", format='jpeg', dpi=100, bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "fc7762e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "if not os.path.isdir('model_weights/'):\n",
    "    os.mkdir('model_weights/')\n",
    "model_02.save_weights(filepath=\"model_weights/vgg19_model_02.h5\", overwrite=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "4a6f951b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 99s 10s/step - loss: 0.5543 - accuracy: 0.6990\n",
      "10/10 [==============================] - 95s 9s/step - loss: 0.6874 - accuracy: 0.5742\n"
     ]
    }
   ],
   "source": [
    "model_02.load_weights(\"model_weights/vgg19_model_02.h5\")\n",
    "vgg_val_eval_02 = model_02.evaluate(valid_generator)\n",
    "vgg_test_eval_02 = model_02.evaluate(test_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e892888a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Unfreezing the entire network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "c1e4d270",
   "metadata": {},
   "outputs": [],
   "source": [
    "base_model = VGG19(include_top=False, input_shape=(240,240,3))\n",
    "base_model_layer_names = [layer.name for layer in base_model.layers] \n",
    "base_model_layer_names\n",
    "\n",
    "x=base_model.output\n",
    "flat = Flatten()(x)\n",
    "\n",
    "class_1 = Dense(4608, activation = 'relu')(flat)\n",
    "drop_out = Dropout(0.2)(class_1)\n",
    "class_2 = Dense(1152, activation = 'relu')(drop_out)\n",
    "output = Dense(2, activation = 'softmax')(class_2)\n",
    "\n",
    "model_03 = Model(base_model.inputs, output)\n",
    "model_03.load_weights('model_weights/vgg19_model_02.h5')\n",
    "\n",
    "sgd = SGD(learning_rate=0.0001, decay = 1e-6, momentum = 0.9, nesterov = True)\n",
    "model_03.compile(loss='categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "8cc485dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"model_7\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " input_11 (InputLayer)       [(None, 240, 240, 3)]     0         \n",
      "                                                                 \n",
      " block1_conv1 (Conv2D)       (None, 240, 240, 64)      1792      \n",
      "                                                                 \n",
      " block1_conv2 (Conv2D)       (None, 240, 240, 64)      36928     \n",
      "                                                                 \n",
      " block1_pool (MaxPooling2D)  (None, 120, 120, 64)      0         \n",
      "                                                                 \n",
      " block2_conv1 (Conv2D)       (None, 120, 120, 128)     73856     \n",
      "                                                                 \n",
      " block2_conv2 (Conv2D)       (None, 120, 120, 128)     147584    \n",
      "                                                                 \n",
      " block2_pool (MaxPooling2D)  (None, 60, 60, 128)       0         \n",
      "                                                                 \n",
      " block3_conv1 (Conv2D)       (None, 60, 60, 256)       295168    \n",
      "                                                                 \n",
      " block3_conv2 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv3 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_conv4 (Conv2D)       (None, 60, 60, 256)       590080    \n",
      "                                                                 \n",
      " block3_pool (MaxPooling2D)  (None, 30, 30, 256)       0         \n",
      "                                                                 \n",
      " block4_conv1 (Conv2D)       (None, 30, 30, 512)       1180160   \n",
      "                                                                 \n",
      " block4_conv2 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv3 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_conv4 (Conv2D)       (None, 30, 30, 512)       2359808   \n",
      "                                                                 \n",
      " block4_pool (MaxPooling2D)  (None, 15, 15, 512)       0         \n",
      "                                                                 \n",
      " block5_conv1 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv2 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv3 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_conv4 (Conv2D)       (None, 15, 15, 512)       2359808   \n",
      "                                                                 \n",
      " block5_pool (MaxPooling2D)  (None, 7, 7, 512)         0         \n",
      "                                                                 \n",
      " flatten_7 (Flatten)         (None, 25088)             0         \n",
      "                                                                 \n",
      " dense_21 (Dense)            (None, 4608)              115610112 \n",
      "                                                                 \n",
      " dropout_7 (Dropout)         (None, 4608)              0         \n",
      "                                                                 \n",
      " dense_22 (Dense)            (None, 1152)              5309568   \n",
      "                                                                 \n",
      " dense_23 (Dense)            (None, 2)                 2306      \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 140,946,370\n",
      "Trainable params: 140,946,370\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "model_03.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9421bc81",
   "metadata": {},
   "outputs": [],
   "source": [
    "# history_03 = model_03.fit(train_generator, steps_per_epoch=10, epochs = 2, callbacks=[es,cp,lrr], validation_data=valid_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "e59bf8e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 91s 9s/step - loss: 0.4964 - accuracy: 0.8155\n",
      "10/10 [==============================] - 89s 9s/step - loss: 0.4410 - accuracy: 0.8161\n"
     ]
    }
   ],
   "source": [
    "model_03.load_weights(\"model_weights/vgg_unfrozen.h5\")\n",
    "vgg_val_eval_03 = model_03.evaluate(valid_generator)\n",
    "vgg_test_eval_03 = model_03.evaluate(test_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6abc2b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Google Colab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66f842f2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}