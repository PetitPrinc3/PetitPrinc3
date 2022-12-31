#!/usr/bin/python3.10


################################################################################


# A simple python library to print things beautifully.
# This library is not licensed


################################################################################


from datetime import datetime

# Print green
def success(text, style = "classic", time = False):  
    
    if time: time = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    else: time = ''
    if style == 'classic': text = '[+]' + time + ' \033[92m' + str(text) + '\033[0m'
    if style == 'discreet': text = '[\033[92m\033[1m+\033[0m]' + time + ' ' + str(text)
    
    print(text)

# Print blue
def info(text, style = "classic", time = False):  
    if time: time = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    else: time = ''
    if style == 'classic': text = '[*]' + time + ' \033[96m' + str(text) + '\033[0m'
    if style == 'discreet': text = '[\033[96m\033[1m*\033[0m]' + time + ' ' + str(text)
    
    print(text)

# Print blue updating current row
def infor(text, style = "classic", time = False):  
    if time: time = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    else: time = ''
    if style == 'classic': text = '[*]' + time + ' \033[96m' + str(text) + '\033[0m'
    if style == 'discreet': text = '[\033[96m\033[1m*\033[0m]' + time + ' ' + str(text)
    
    print(text)

# Print orange
def warning(text, style = "classic", time = False):  
    if time: time = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    else: time = ''
    if style == 'classic': text = '[!]' + time + ' \033[93m' + str(text) + '\033[0m'
    elif style == 'discreet': text = '[\033[93m\033[1m!\033[0m]' + time + ' ' + str(text)

    print(text)

# Print red
def fail(text, style = "classic", time = False):  
    if time: time = "[" + str(datetime.now().strftime("%H:%M:%S")) + "]"
    else: time = ''
    if style == 'classic': text = '[-]' + time + ' \033[91m' + text + '\033[0m'
    elif style == 'discreet': text = '[\033[91m\033[1m-\033[0m]' + time + ' ' + str(text)

    print(text)


################################################################################


if __name__ == "__main__":
    fail('Please run main.py or read software documentation')
    exit()

