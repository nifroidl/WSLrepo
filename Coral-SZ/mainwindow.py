# This Python file uses the following encoding: utf-8
import sys
from subprocess import Popen, PIPE, CalledProcessError
import subprocess #New S.Z. 20.08.2023
import threading
import os
import time
import webbrowser #TNe

## Scripts for Onclick actions in the GUI workflow
from scripte.png2jpg import png2jpg
from scripte.replace_file_format import convertFileFormatString
from scripte.split_dataset import split_dataset
from scripte.run_training_efficientdetlite import trainModel, testModel
from scripte.quantize_model import quantizeModel
from scripte.compile_edge_tpu import compileEdgeTPU

from scripte.getBoardIpAddress import getBoardIpAddress #TNe
from scripte.runOnBoard import runClassificationModelOnBoard, runDetectionModelOnBoard, pushFileToBoard

import tensorflow as tf
assert tf.__version__.startswith('2')

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QListWidgetItem
from PySide6.QtCore import Slot
from PySide6 import QtCore
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from dialogConnectDevice import Ui_DialogConnectDevice #New S.Z. 19.08.2023

PNG_FILE = 0

mainWindowAbsDir = os.path.split(os.path.abspath(__file__))[0] #to be independent from the location where the mainwindow.py script was started

class MainWindow(QMainWindow):
    writeProgress = QtCore.Signal((str,))
    enableButtons = QtCore.Signal((bool,))

    model = None
    train_data = None
    validation_data = None
    test_data = None
    tflite_filename = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton_TrainImages.clicked.connect(self.getTrainImagesFolder)
        self.ui.toolButton_TrainAnnotations.clicked.connect(self.getTrainAnnotationsFolder)
        self.ui.toolButton_TrainLabels.clicked.connect(self.getTrainLabelsFile)

        self.ui.toolButton_TestAnnotations.clicked.connect(self.getTestAnnotationsFolder)
        self.ui.toolButton_TestImages.clicked.connect(self.getTestImagesFolder)

        self.ui.toolButton_ValidateAnnotations.clicked.connect(self.getValidateAnnotationsFolder)
        self.ui.toolButton_ValidateImages.clicked.connect(self.getValidateImagesFolder)

        self.ui.toolButton_ModelOutput.clicked.connect(self.getModelOutput) # Folder

        self.ui.checkBox_FileFormat.currentIndexChanged.connect(self.activeTrainButton)

        self.ui.pB_PrepareDataset.clicked.connect(self.onPrepareDataset)
        self.ui.pB_Train.clicked.connect(self.onTrainModel)
        self.ui.pB_Test.clicked.connect(self.onTest)
        self.ui.pB_RunModel.clicked.connect(self.onRunModel)
        self.ui.pB_RunModel.setEnabled(True)
        self.ui.toolButton_ModelToRun.clicked.connect(self.getModelToRunOnBoard)
        self.ui.toolButton_ModelToRun.setEnabled(True)
        self.ui.toolButton_LabelsForModel.clicked.connect(self.getLabelForModelOnBoard)
        self.ui.toolButton_LabelsForModel.setEnabled(True)

        self.ui.doubleSpinBox_TestSplitRate.valueChanged.connect(self.onDoubleSpinBox_TestSplitRateChanged)
        self.ui.doubleSpinBox_ValidateSplitRate.valueChanged.connect(self.onDoubleSpinBox_ValidateSplitRateChanged)

        self.ui.checkBox_SplitDataset.toggled.connect(self.onCheckboxEvent)

        self.ui.actionConnect_Device.triggered.connect(self.showConnectDevice) #New S.Z. 19.08.2023

        self.ui.actionDark.triggered.connect(self.onActionDark)
        self.ui.actionWhite.triggered.connect(self.onActionWhite)
        self.writeProgress.connect(self.textOutput, QtCore.Qt.QueuedConnection)
        self.enableButtons.connect(self.onEnableButtons, QtCore.Qt.QueuedConnection)
        sys.stdout = self

    def excuteSubProcess(self, args):
        with Popen(args, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='') # process line here
                self.textOutput("\t"+line)

        if p.returncode != 0:
            errorText = """Error in {errorArgs}\n============================================================================
            """.format(errorArgs = p.args)
            self.textOutput(errorText)
            raise CalledProcessError(p.returncode, p.args)

    def flush(self):
        pass

    def write(self, data):
        self.writeProgress.emit(data)
        

    @Slot(bool)
    def onEnableButtons(self, value):
        self.ui.Buttons_Widget.setEnabled(value)

    @Slot(str)
    def textOutput(self, text):
        #Callback function for text ouput
        self.ui.textBrowserProgess.append(text)
        self.ui.textBrowserProgess.repaint()

    @Slot()
    def onCheckboxEvent(self):
        if(self.ui.checkBox_SplitDataset.isChecked()):
            self.ui.label_11.setText("Train Images Folder")
            self.ui.checkBox_FileFormat.setEnabled(False)
            self.ui.pB_PrepareDataset.setEnabled(False)
        else:
            self.ui.label_11.setText("Dataset Images Folder")
            self.ui.checkBox_FileFormat.setEnabled(True)
            self.ui.pB_PrepareDataset.setEnabled(True)
        

    @Slot()
    def onPrepareDataset(self):
        self.ui.Buttons_Widget.setEnabled(False)
        startText = """===============================================================================================\nDataset preparation started\n"""
        self.textOutput(startText)
        self.textOutput("Convert Images/Annotations: Started")

        #Required Dataset Structure before dataset spliitting:
        #DATASET_DIR
        #├── annotations            : Folder that contains all annotations in .xml format 
        #├── images                 : Folder that contains all images in .jpg OR .png format
        #└── LABELS.txt             : Simple file including one labelclass per line

        #ToDo: Bug - If checkbox "Is your dataset already split" is checked - Prepare does not work because it expects all pictures/annotations to be in one folder for conversion, GH 01.03.23

        path_to_images = self.ui.textBrowser_TrainImages.toPlainText()
        path_to_annotations = self.ui.textBrowser_TrainAnnotations.toPlainText()
        if(self.ui.checkBox_FileFormat.currentIndex() == PNG_FILE): # Convert from PNG to JPG
            output_dir_images = os.path.join(os.path.dirname(path_to_images), 'images_jpg')
            output_dir_annotations = os.path.join(os.path.dirname(path_to_annotations), 'annotations_jpg')
            #Convert images
            png2jpg(path_to_images, output_dir_images, self.textOutput)
            #Convert annotations files
            convertFileFormatString(path_to_annotations, output_dir_annotations, "png", "jpg", self.textOutput)

            path_to_images = output_dir_images
            path_to_annotations = output_dir_annotations
        else:             
            print("data already in .jpg format")            
            #Alternativly rename images folder to images_jpg
            
        self.textOutput("Convert Images/Annotations: Finished")

        #Dataset Structure after .png --> .jpg conversion:
        #DATASET_DIR
        #├── annotations            : Folder that contains all annotations in .xml format (png references internally)
        #├── annotations_jpg        : New folder that contains all annotations in .xml format (jpg references internally)
        #├── images                 : Folder that contains all images in .png format
        #├── images_jpg             : New folder that contains all images in .jpg format    
        #└── LABELS.txt             : Simple file including one labelclass per line

        if(not self.ui.checkBox_SplitDataset.checkState()): #changed to check the state of "is your dataset already split" here: DK 20.02.23
            self.textOutput("\nSplit dataset: Started")

            #TODO: Splitrates of validate and test can be 100%. That means you will have 0 train images... GH 20.02.23

            train_dir, val_dir, test_dir = split_dataset(path_to_images,
                path_to_annotations,
                self.ui.doubleSpinBox_ValidateSplitRate.value(),
                self.ui.doubleSpinBox_TestSplitRate.value())

            self.textOutput(f"\tTrain directory:\t\t{train_dir}")
            self.textOutput(f"\tValidation directory:\t\t{val_dir}")
            self.textOutput(f"\tTest directory:\t\t{test_dir}")
            
            # Take output directories from split_dataset and show them in the GUI
            self.ui.label_11.setText("Train-Images")
            self.ui.textBrowser_TrainImages.setText(os.path.join(train_dir,"images"))
            self.ui.textBrowser_TrainImages.setToolTip(os.path.join(train_dir,"images"))
            
            self.ui.textBrowser_TrainAnnotations.setText(os.path.join(train_dir,"annotations"))
            self.ui.textBrowser_TrainAnnotations.setToolTip(os.path.join(train_dir,"annotations"))
            
            self.ui.textBrowser_ValidateImages.setText(os.path.join(val_dir,"images"))
            self.ui.textBrowser_ValidateImages.setToolTip(os.path.join(val_dir,"images"))

            self.ui.textBrowser_ValidateAnnotations.setText(os.path.join(val_dir,"annotations"))
            self.ui.textBrowser_ValidateAnnotations.setToolTip(os.path.join(val_dir,"annotations"))

            self.ui.textBrowser_TestImages.setText(os.path.join(test_dir,"images"))
            self.ui.textBrowser_TestImages.setToolTip(os.path.join(test_dir,"images"))

            self.ui.textBrowser_TestAnnotations.setText(os.path.join(test_dir,"annotations"))
            self.ui.textBrowser_TestAnnotations.setToolTip(os.path.join(test_dir,"annotations"))

            train_images_dir = os.path.join(train_dir, 'images')
            validation_images_dir = os.path.join(val_dir, 'images')#
            test_images_dir = os.path.join(test_dir, 'images')

            self.textOutput(f"\ttrain images count:\t\t{len([entry for entry in os.listdir(train_images_dir) if os.path.isfile(os.path.join(train_images_dir, entry))])}")
            self.textOutput(f"\tvaildation images count:\t{len([entry for entry in os.listdir(validation_images_dir) if os.path.isfile(os.path.join(validation_images_dir, entry))])}")
            self.textOutput(f"\ttest images count:\t\t{len([entry for entry in os.listdir(test_images_dir) if os.path.isfile(os.path.join(test_images_dir, entry))])}")

            self.textOutput("Split dataset: Completed")

        #Final Dataset structure after dataset splitting:
        #DATASET_DIR
        #├── train                  : New folder for training sub-dataset  
        #|   ├── annotations        : New folder that contains all training annotations in .xml format
        #|   └── images             : New folder that contains all training images in .jpg format
        #├── test                   : New folder for test sub-dataset
        #|   ├── annotations        : New folder that contains all annotations in .xml format
        #|   └── images             : New folder that contains all images in .jpg format
        #├── validation             : new Folder for validation sub-dataset
        #|   ├── annotations        : New folder that contains all annotations in .xml format
        #|   └── images             : New folder that contains all images in .jpg format        
        #├── annotations            : Folder that contains all annotations in .xml format (png references internally)
        #├── annotations_jpg        : New folder that contains all annotations in .xml format (jpg references internally)
        #├── images                 : Folder that contains all images in .png format
        #├── images_jpg             : New folder that contains all images in .jpg format    
        #└── LABELS.txt             : Simple file including one labelclass per line



        endText = """\nDataset preparation: Completed\n"""
        self.textOutput(endText)
        self.ui.Buttons_Widget.setEnabled(True)

#=====================================================================================

    @Slot()
    def onTrainModel(self):
        self.ui.Buttons_Widget.setEnabled(False)

        startText = """===============================================================================================\nModel Training started"""
        self.textOutput(startText)

                
        #example: C:/Git/googlecoralki/Qt/Coral_AI_GUI/images_jpg/train/--images--
        #Split images path and remove last directory --images--

        train_dir = os.path.dirname(self.ui.textBrowser_TrainImages.toPlainText())
        self.textOutput(f"\tTrain directory:\t{train_dir}")

        val_dir = os.path.dirname(self.ui.textBrowser_ValidateImages.toPlainText())
        self.textOutput(f"\tValidation directory:\t{val_dir}")

        test_dir = os.path.dirname(self.ui.textBrowser_TestImages.toPlainText())
        self.textOutput(f"\tTest directory:\t{test_dir}")

        output_dir = os.path.dirname((f"{self.ui.textBrowser_ModelOutput.toPlainText()}/"))
        self.textOutput(f"\tModel directory:\t{output_dir}")

        efficientDetLiteVersion = self.ui.comboBox_Model.currentText()[-1]  
        self.textOutput(f"\tEfficientDet-Lite selected:\t{efficientDetLiteVersion}")

        epochs = self.ui.spinBox_Epochs.value()
        self.textOutput(f"\tNumber of epochs selected:\t{epochs}")
        batches = self.ui.spinBox_Batch.value()
        self.textOutput(f"\tNumber of batches selected:\t{batches}")

        t = threading.Thread(target=self.asyncTrainModel, args=(
            efficientDetLiteVersion, 
            train_dir, 
            val_dir, 
            test_dir, 
            self.ui.textBrowser_TrainLabels.toPlainText(), #trainLabels
            epochs, 
            batches, 
            output_dir)
            )
        t.start()
        
    def asyncTrainModel(self, efficientDetLiteVersion, train_dir, val_dir, test_dir, trainLabels, batches, epoches, modelOutput):
        try:
            model, train_data, validation_data, test_data, tflite_filename = trainModel(efficientDetLiteVersion, train_dir, val_dir, test_dir, trainLabels, batches, epoches, modelOutput)
            print("""Model training: Completed\n""")

            self.model = model
            self.train_data = train_data
            self.validation_data = validation_data
            self.test_data = test_data
            self.tflite_filename = tflite_filename

            if(self.ui.checkBox_Quantization.checkState()):
                print("(Optional) Start TFLite model quantization")
                quantized = quantizeModel(self.model, self.tflite_filename, modelOutput)
                print("TFLite model quantization completed")
            else:
                quantized = False
	
            if(self.ui.checkBox_CompileForEdgeTPU.checkState()):
                print("(Optional) Start TFLite compile for EdgeTPU")
                compileEdgeTPU(self.model, self.tflite_filename, modelOutput, quantized)
                print("TFLite model comilation for EdgeTPU completed")

            self.ui.pB_Test.setEnabled(True)
            self.ui.pB_RunModel.setEnabled(True)
        except Exception as e:
            print(e)
            print("""Model training failed\n===============================================================================================""")
        self.enableButtons.emit(True)


#===================================================================================
    @Slot()
    def onRunModel(self): #TNe
        self.ui.Buttons_Widget.setEnabled(False)
        self.ui.Buttons_Widget.setEnabled(True)
        try:
            ipAddress = getBoardIpAddress()
            print(ipAddress, flush=True)

        except:
            print("IP address could not be found", flush=True)

        pushFileToBoard(self.ui.textBrowser_ModelToRun.toPlainText())
        pushFileToBoard(self.ui.textBrowser_LabelsForModel.toPlainText())

        webbrowser.open(f"http://{ipAddress}:4664")
        runClassificationModelOnBoard(os.path.basename(self.ui.textBrowser_ModelToRun.toPlainText()), os.path.basename(self.ui.textBrowser_LabelsForModel.toPlainText()))


#=====================================================================================
    @Slot()
    def onTest(self):
        self.ui.Buttons_Widget.setEnabled(False)

        startText = """===============================================================================================\nModel Test started"""
        self.textOutput(startText)

        efficientDetLiteVersion = self.ui.comboBox_Model.currentText()[-1]
        self.textOutput(f"\tEfficientDet-Lite selected:\t{efficientDetLiteVersion}")

        output_dir = os.path.dirname((f"{self.ui.textBrowser_ModelOutput.toPlainText()}/"))
        self.textOutput(f"\tModel directory:\t{output_dir}")

        t = threading.Thread(target=self.asyncTestModel, args=(
            efficientDetLiteVersion,
            self.model,
            self.test_data,
            output_dir)
            )
        t.start()

    def asyncTestModel(self, efficientDetLiteVersion, model, test_data, modelOutput):
        try:
            testModel(efficientDetLiteVersion, model, test_data, modelOutput)
            print("""Model Test: Completed\n""")
        except Exception as e:
            print(e)
            print("""Model Test failed\n===============================================================================================""")

        self.ui.Buttons_Widget.setEnabled(True)

#====================================================================================
    @Slot()
    def onActionDark(self):
        app.setStyleSheet(open(f"{mainWindowAbsDir}/DarkStyle.qss", "r").read())

    @Slot()
    def onActionWhite(self):
        app.setStyleSheet(open(f"{mainWindowAbsDir}/WhiteStyle.qss", "r").read())

#=====================================================================================

    @Slot(int)
    def onDoubleSpinBox_ValidateSplitRateChanged(self,i):
        self.ui.doubleSpinBox_TestSplitRate.blockSignals(True)                            
        if (i + self.ui.doubleSpinBox_TestSplitRate.value() >= 1):
            self.ui.doubleSpinBox_TestSplitRate.setValue(1-i)
        self.textOutput(f"ValidateSplitRate: {round(i,2)}\tTestsplitRate: {round(self.ui.doubleSpinBox_TestSplitRate.value(),2)}")    
        self.ui.doubleSpinBox_TestSplitRate.blockSignals(False)

    @Slot(int)
    def onDoubleSpinBox_TestSplitRateChanged(self,i):
        self.ui.doubleSpinBox_ValidateSplitRate.blockSignals(True)
        if (i + self.ui.doubleSpinBox_ValidateSplitRate.value() >= 1):
                self.ui.doubleSpinBox_ValidateSplitRate.setValue(1-i)        
        self.textOutput(f"TestSplitRate: {round(i,2)}\tValidateSplitRate: {round(self.ui.doubleSpinBox_ValidateSplitRate.value(),2)}")
        self.ui.doubleSpinBox_ValidateSplitRate.blockSignals(False)

    @Slot(str)
    def activeTrainButton(self,s):
        if s:
            self.ui.pB_Train.setEnabled(True)
        else:
            self.ui.pB_Train.setEnabled(False)

    @Slot()
    def getTrainImagesFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_TrainImages.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_TrainImages.setToolTip(dialog.selectedFiles()[0])

    @Slot()
    def getTrainAnnotationsFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_TrainAnnotations.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_TrainAnnotations.setToolTip(dialog.selectedFiles()[0])

    @Slot()
    def getTrainLabelsFile(self):
        dialog = QFileDialog(self)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_TrainLabels.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_TrainLabels.setToolTip(dialog.selectedFiles()[0])
        with open(dialog.selectedFiles()[0], 'r') as f:
            label_map = [line.strip() for line in f.readlines()]
        self.ui.textBrowser_NumberOfClasses.setPlainText(f"{len(label_map)}")
#===================================================================

    @Slot()
    def getTestImagesFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_TestImages.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_TestImages.setToolTip(dialog.selectedFiles()[0])

    @Slot()
    def getTestAnnotationsFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_TestAnnotations.setText( dialog.selectedFiles()[0])
            self.ui.textBrowser_TestAnnotations.setToolTip( dialog.selectedFiles()[0])

#===================================================================

    @Slot()
    def getValidateImagesFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_ValidateImages.setText( dialog.selectedFiles()[0])
            self.ui.textBrowser_ValidateImages.setToolTip( dialog.selectedFiles()[0])

    @Slot()
    def getValidateAnnotationsFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_ValidateAnnotations.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_ValidateAnnotations.setToolTip(dialog.selectedFiles()[0])

#==================================================================

    @Slot()
    def getModelOutput(self):

        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_ModelOutput.setText(dialog.selectedFiles())
            self.ui.textBrowser_ModelOutput.setToolTip(dialog.selectedFiles())

    @Slot()
    def getModelToRunOnBoard(self):
        dialog = QFileDialog(self)
        #dialog.setFileMode(QFileDialog.Directory)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_ModelToRun.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_ModelToRun.setToolTip(dialog.selectedFiles()[0])

    @Slot()
    def getLabelForModelOnBoard(self):
        dialog = QFileDialog(self)
        #dialog.setFileMode(QFileDialog.File)
        dialog.open()
        if dialog.exec():
            self.ui.textBrowser_LabelsForModel.setText(dialog.selectedFiles()[0])
            self.ui.textBrowser_LabelsForModel.setToolTip(dialog.selectedFiles()[0])

#==================================================================

    @Slot() #New S.Z. 19.08.2023
    def showConnectDevice(self):
        dialog = DialogConnectDevice()
        result = dialog.exec()
        #if result == QDialog.Accepted:
        #    print("Dialog accepted")
        #else:
        #    print("Dialog rejected")            

#==================================================================

class DialogConnectDevice(QDialog): #New S.Z. 19.08.2023
    hostIp = " "
    google_coral_devices = []
    device = {"name": " ", "manufacturer":" ", "busId":" ", "vid":" ", 
              "pid":" ", "port":" "} #Attached device information
    deviceName = " "
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogConnectDevice()
        self.ui.setupUi(self)

        self.ui.pb_Search.clicked.connect(self.buttonSearchDevices)
        self.ui.pb_Attach.clicked.connect(self.buttonAttachDevice)
        self.ui.listWidget.itemClicked.connect(self.chooseDevice)

        self.buttonSearchDevices()

    @Slot() 
    def buttonSearchDevices(self):
        self.hostIp = self.readHostIp()
        self.google_coral_devices = self.searchDevices(self.hostIp)
        self.listDevices(self.google_coral_devices)

    @Slot()
    def chooseDevice(self, item): 
        self.deviceName = item.text()   

    @Slot()
    def buttonAttachDevice(self):
        # Connect the chosen device with WSL distribution. 
        # With the kernelmessages before and after the attachement the respective network adapter is 
        # figured out. 
        # Assigns IP-Adress to the respective adpater. 
        # Prerequisite for using MDT from an WSL distribution
        ip_address = self.hostIp
        deviceFound = False
        for device in self.google_coral_devices: 
            if device["name"] == self.deviceName: 
                self.device = device
                busId = device["busId"]
                deviceFound = True
        if deviceFound == False: 
            print("Please choose device!")
            return
        filteredKernelMessages = self.getFilteredKernelMessages("cdc_ether")
        try:
            subprocess.run(["sudo", "usbip", "attach", "-r", ip_address, "-b", busId], check=True)
            time.sleep(2)
            latestFilteredKernelMessages = self.getFilteredKernelMessages("cdc_ether")
            deviceKernelMessages = latestFilteredKernelMessages.replace(filteredKernelMessages, "")
            adapterName = self.extractAdapterName(deviceKernelMessages)
            self.attachInterfaceIp(adapterName)
            print("USB device attached successfully.")
            self.assignAttachedDeviceLabels()
        except subprocess.CalledProcessError:
            print("USB device attachment failed.")

    def readHostIp(self):
        #reads the WSl2 host ip address
        try:
            output = subprocess.check_output(["ip", "route"]).decode()
            lines = output.split("\n")
            for line in lines:
                if "default" in line:
                    gateway_ip = line.split()[2]
                    return gateway_ip
            print("Default gateway IP address not found.")
            sys.exit(1)
        except subprocess.CalledProcessError:
            print("Error retrieving default gateway IP address.")
            sys.exit(1)
        
    def searchDevices(self, ip_address):
        # Uses the host ip address for searching devices which are available to attach
        # At that moment just Google Coral Dev. Board Mini Devices are supported 
        # (fixed manufacturer & vid:pid) 
        
        try:
            output = subprocess.check_output(["usbip", "list", "-r", ip_address]).decode()
            lines = output.split("\n")
            google_coral_devices = []
            device = {"name": " ", "manufacturer":" ", "busId":" ", "vid":" ", 
              "pid":" ", "port":" "}

            for line in lines:
                if (len(line) - len(line.lstrip()) == 8) and "Google Inc." in line and "18d1:9304" in line:
                    parts = line.lstrip().split(":", 2)
                    device["busId"] = parts[0].lstrip()
                    device["manufacturer"] = "Google Inc."
                    device["vid"] = "18d1"
                    device["pid"] = "9304"
                        
                elif ("VID_" + device["vid"] + "&PID_" + device["pid"]).upper() in line:
                    parts = line.lstrip().split("\\", 2)
                    device["name"] = parts[2].lstrip()
                    google_coral_devices.append(device)
            
            return google_coral_devices
        
        except subprocess.CalledProcessError:
            print("Error searching for Google Coral devices.")
            return []
    
    def listDevices(self, devices):
        # Add found devices to the list in the window
        for device in devices:
            newDevice = QListWidgetItem(device["name"])
            self.ui.listWidget.addItem(newDevice)

    def attachInterfaceIp(self, interfaceName): 
        # Uses DHCP to assign IP-Adress to new network adapter
        try:
            subprocess.run(["sudo", "dhclient", interfaceName], check=True)
            print("Attach interface ip succeeded")
        except subprocess.CalledProcessError:
            print("Attach interface ip failed")

    def getFilteredKernelMessages(self, filterName):
        # Get Kernelmessages with a specific key word as filter
        try:
            output = subprocess.check_output(["dmesg"])
            filteredKernelMessages = subprocess.check_output(["grep","-F" , filterName], input=output).decode()
            return filteredKernelMessages
        except subprocess.CalledProcessError:
            print("USB device attachment failed.")
            
    def extractAdapterName (self, deviceKernelMessages):
        # Uses the latest kernelmessages (Those which contain only the attachement of device)
        # Return adapter name of newly attached adapter related to device 
        lines = deviceKernelMessages.split("\n")
        adapterName = ""
        for message in lines: 
            if "register" in message: 
                part = message.lstrip().split()
                adapterName = part[3].replace(":", "")
            elif ("renamed" and adapterName) in message and adapterName != "": 
                part = message.lstrip().split()
                adapterName = part[3].replace(":", "")
        return adapterName
    
    def assignAttachedDeviceLabels(self):
        self.ui.label_Name.setText(self.device["name"])
        self.ui.label_Manufacturer.setText(self.device["manufacturer"])
        self.ui.label_BusId.setText(self.device["busId"])
        self.ui.label_VIDPID.setText(self.device["vid"] + ":" +self.device["pid"])
        self.ui.label_Port.setText(self.device["port"])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open(f"{mainWindowAbsDir}/WhiteStyle.qss", "r").read())            
    widget = MainWindow()
    widget.showMaximized()
    sys.exit(app.exec())
