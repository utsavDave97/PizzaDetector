# Pizza Detector Dataset

This is a dataset that I collected to train my own Pizza detector with [TensorFlow's Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection). Images are from Google and Pixabay. In total, there are 200 images (160 are used for training and 40 for validation).

## Getting Started

##### Folder Structure:
```
+ annotations: contains the input file for the TF object detection API and the label files (csv)
+ output_inference_graph_v1.pb: contains the result of the model
+ images: contains the image data in jpg format along with the xml files in PASCAL VOC format
+ training: contains the pipeline configuration file, frozen model and labelmap
- a few handy scripts: generate_tfrecord.py is used to generate the input files
for the TF API and xml_to_csv.py is used to convert the xml files into one csv
- train.py: this python file is used to train the model
- detect.tflite: this tflite file could be used in Android Pizza Detector App.
```

## Copyright

See [LICENSE](LICENSE) for details.
