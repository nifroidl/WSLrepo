import pexpect
import re

#method to get wlan0 interface ip of mdt board
def getBoardIpAddress():
    output = runCommandOnBoard(f"/home/nick/venv_model_training/bin/mdt exec ip a")
    ip_adress = extractInterfaceIp(output, "wlan0")
    return ip_adress

#method to run a command on the mdt board (subconsole, makes python module subprocess not usable)
def runCommandOnBoard(command):
    # start pexpect command
    child = pexpect.spawn(command, encoding='utf-8')

    # wait for end of process
    child.expect(pexpect.EOF)

    # return output as string
    return child.before

#method to extract interface ip from output string of "ip a command"
def extractInterfaceIp(text, interface):
    # Search for IP of {interface} with regular expression
    pattern = rf'{interface}:.*?inet (\d{{1,3}}\.\d{{1,3}}\.\d{{1,3}}\.\d{{1,3}})'
    match = re.search(pattern, text, re.DOTALL)

    # if found: return ip adress
    if match:
        return match.group(1)

    return None  # no ip of specified interface found
