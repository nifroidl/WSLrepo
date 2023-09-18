# Tools for TFlite model training
Tools to convert Dataset-formats and to train custom TFlite-models using different model architectures for\
object detection and image classification.

## Getting Started
Its recommended to use **Ubuntu 20.04.4 LTS** and **Python3.8**. Everything is tested with these Version.

To setup a python virtual environment with all required modules installed, run:
~~~bash
python3.8 -m venv venv_model_training
source venv_model_training/bin/activate
pip install -r requirements.txt
~~~

Now you should see the following in your terminal window which means that the venv is activated.
~~~bash
(venv_model_training) <USERNAME>@Ubuntu:<PATH>/coraldevboardmini/5_tflite_training
~~~

To deactivate the venv run:
~~~bash
deactivate
~~~

If you want to compile your models for edgetpu run additionally:
~~~bash
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
sudo apt-get update
sudo apt-get install edgetpu-compiler
~~~



## General Tools
Tools to convert datasets to the required formats. F.e.
- **png2jpg.py**: Tool for converting images inside a directory from .png-format to .jpg-format.\
Run following command to see how to use the script:
    ~~~bash
  ./png2jpg.py -h
    ~~~
- **string_replacer.py**: Tool for replacing a specific string inside specific files inside a directory.\
Run following command to see how to use the script:
    ~~~bash
  ./string_replacer.py -h
    ~~~
## object detection model architectures

### EfficientDet-Lite using TFlite-Model-Maker 
Easy to use script for trainig tflite models based on EfficientDet-Lite 0-4 finished and succesfully tested.\
Run following command to see how to use the script:
~~~bash
./run_training_efficientdetlite.py -h
~~~

https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_efficientdet_model_maker_tf2.ipynb




### SSDLite MobileDet - object detection
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_ssdlite_mobiledet_qat_tf1.ipynb
- TODO

### SSD MobileNetV1 - object detection
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_detection_qat_tf1.ipynb
- TODO

### EfficientDet-Lite - object detection
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_efficientdet_model_maker_tf2.ipynb
- TODO


## image classification model architectures

### MobileNetV2 - classification
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_ptq_tf2.ipynb
- TODO

### MobileNetV1 - classification
https://colab.research.google.com/github/google-coral/tutorials/blob/master/retrain_classification_qat_tf1.ipynb
- TODO



## TODO:
- Add further formatting tools based if required
- Train models using all the different methods/architectures
- Develop easy to use scripts for model training for all architectures
(conform with the existing script for EfficientDet-Lite)
- Compare TFlite-models trained based on different architectures
