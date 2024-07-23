import os
import json
import pickle as pkl

fold_path = "/media/SSD1/srodriguezr2_2/phakir_challenge/annotations/phases/annotations_1fps/fold1"

with open(os.path.join(fold_path, "train_anns.json"), "r") as file:
    train_anns = json.load(file)

with open(os.path.join(fold_path, "test_anns.json"), "r") as file:
    test_anns = json.load(file)

dataset_path = "/media/SSD1/srodriguezr2_2/phakir_challenge/Frames"

all_info = []

train_img_path = [
    os.path.join(dataset_path, img_info["file_name"])
    for img_info in train_anns["images"]
]
test_img_path = [
    os.path.join(dataset_path, img_info["file_name"])
    for img_info in test_anns["images"]
]

all_info.append(train_img_path)
all_info.append(test_img_path)

train_labels = []
for train_ann in train_anns["annotations"]:
    train_label = [0] * 7
    train_label[train_ann["phases"]] = 1
    train_labels.append(train_label)

test_labels = []
for test_ann in test_anns["annotations"]:
    test_label = [0] * 7
    test_label[test_ann["phases"]] = 1
    test_labels.append(test_label)

all_info.append(train_labels)
all_info.append(test_labels)

train_num_each = []
first = True

for img_info in train_anns["images"]:
    if first:
        video_name = img_info["video_name"]
        first = False
        count = 1
    else:
        if video_name == img_info["video_name"]:
            count += 1
        else:
            train_num_each.append(count)
            video_name = img_info["video_name"]
            count = 1

train_num_each.append(count)

test_num_each = []
first = True
for img_info in test_anns["images"]:
    if first:
        video_name = img_info["video_name"]
        first = False
        count = 1
    else:
        if video_name == img_info["video_name"]:
            count += 1
        else:
            test_num_each.append(count)
            video_name = img_info["video_name"]
            count = 1

test_num_each.append(count)

all_info.append(train_num_each)
all_info.append(test_num_each)

with open("train_val_paths_labels1.pkl", "wb") as file:
    pkl.dump(all_info, file)
