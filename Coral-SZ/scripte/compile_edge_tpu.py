import os, subprocess

import tensorflow as tf
assert tf.__version__.startswith('2')

def compileEdgeTPU(model, tflite_filename, model_export_path, quantized):

    TFLITE_FILENAME = tflite_filename
    QUANTIZE = quantized
    MODEL_EXPORT_DIR = model_export_path

    print(f"Compile TFLite model:\n")
    result = subprocess.run(["edgetpu_compiler", "-s", "-o", MODEL_EXPORT_DIR, f"{MODEL_EXPORT_DIR}/{TFLITE_FILENAME + '.tflite'}"], stdout=subprocess.PIPE, text=True)
    print(result.stdout)

    if QUANTIZE:
        print(f"Compile quantized TFLite model:\n")
        result = subprocess.run(["edgetpu_compiler", "-s", "-o", MODEL_EXPORT_DIR, f"{MODEL_EXPORT_DIR}/{TFLITE_FILENAME + '_fp16.tflite'}"], stdout=subprocess.PIPE, text=True)
        print(result.stdout)

    print(f"MODEL: {MODEL_EXPORT_DIR}/{TFLITE_FILENAME}_fp16_edgeTPU.tflite")

    return 1
