# Orin Robotics

## Label-Studio-Converter
```
(label-studio) root@94c756140b69:/orin-robotics# label-studio-converter import coco -h
usage: label-studio-converter import coco [-h] -i INPUT [-o OUTPUT] [--to-name TO_NAME] [--from-name FROM_NAME] [--out-type OUT_TYPE]
                                          [--image-root-url IMAGE_ROOT_URL] [--point-width POINT_WIDTH]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        directory with COCO where images, labels, notes.json are located
  -o OUTPUT, --output OUTPUT
                        output file with Label Studio JSON tasks
  --to-name TO_NAME     object name from Label Studio labeling config
  --from-name FROM_NAME
                        control tag name from Label Studio labeling config
  --out-type OUT_TYPE   annotation type - "annotations" or "predictions"
  --image-root-url IMAGE_ROOT_URL
                        root URL path where images will be hosted, e.g.: http://example.com/images
  --point-width POINT_WIDTH
                        key point width (size)
```

label-studio-converter import coco -i '/orin-robotics/datasets/coco' -o '/orin-robotics/datasets/coco_output' 