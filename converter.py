from ultralytics.data.converter import convert_coco

convert_coco(
    labels_dir="/Volumes/Extreme SSD/coco128/labels/train2017",
    save_dir="/Volumes/Extreme SSD/coco128_labels/",
    use_keypoints=True,
    use_segments=True,
    cls91to80=False
)