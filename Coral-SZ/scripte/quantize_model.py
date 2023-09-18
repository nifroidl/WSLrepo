import os

import tensorflow as tf
assert tf.__version__.startswith('2')

#from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig

def quantizeModel(model, tflite_filename, model_export_path):

    TFLITE_FILENAME = tflite_filename
    MODEL_EXPORT_DIR = model_export_path

    config = QuantizationConfig.for_float16()
    model.export(export_dir=MODEL_EXPORT_DIR, tflite_filename=TFLITE_FILENAME + '_fp16.tflite', quantization_config=config)

    print(f"MODEL: {MODEL_EXPORT_DIR}/{TFLITE_FILENAME}_fp16.tflite")
    return 1
