import pexpect

#method to push a file to the board
def pushFileToBoard(filepath):
    output = runCommandOnBoard(f"/home/nick/venv_model_training/bin/mdt push {filepath}")
    return output

#method to run a classification model on the board
def runClassificationModelOnBoard(modelpath, labelpath):
    output = runCommandOnBoard(f"/home/nick/venv_model_training/bin/mdt exec edgetpu_classify_server --model {modelpath} --labels {labelpath}")
    return output

def runDetectionModelOnBoard(modelpath):
    output = runCommandOnBoard(f"/home/nick/venv_model_training/bin/mdt exec edgetpu_detect_server --model {modelpath}")
    return output


#method to run a command on the mdt board (subconsole, makes python module subprocess not usable)
def runCommandOnBoard(command):
    # start pexpect command
    #child = pexpect.spawn(command, encoding='utf-8')

    # wait for end of process
    #child.expect(pexpect.EOF, timeout=120)

    # return output as string
    #return child.before

    child = pexpect.spawn(command, encoding='utf-8')
    
    output = []
    while True:
        try:
            #joining the live output from subconsole
            child.expect('\n', timeout=None)
            print(child.before)  #printig live output
            output.append(child.before)
        except pexpect.EOF:
            break

    return "\n".join(output)

#method to run a continous command on the mdt board
def runCommandOnBoardContinuously(command):
    child = pexpect.spawn(command, encoding='utf-8')
    
    output = []
    while True:
        try:
            #joining the live output from subconsole
            child.expect('\n', timeout=None)
            print(child.before)  #printig live output
            output.append(child.before)
        except pexpect.EOF:
            break

    return "\n".join(output)