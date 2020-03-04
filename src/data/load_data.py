
"""
LOAD THE RAW DATA AND CONVERT TO DATAFRAME FORMAT

 """
import os
import re
import json
import email
import pickle
import mailbox
import pandas as pd
from time import asctime
from bs4 import BeautifulSoup
from dateutil.parser import parse

from data.directory_root import path_file, MBOX, sms_folder, chats_folder

# Converting the raw data folder to a standardized mbox format

# Create a file handle that we'll be writing into...
mbox = open(MBOX, 'w+')

# Walk the directories and process all folders
for (root, dirs, file_names) in os.walk(path_file):

    if root.split(os.sep)[-1].lower() != 'inbox':
        continue

    # Process each message in 'inbox'

    for file_name in file_names:
        file_path = os.path.join(root, file_name)
        message_text = open(file_path, errors='ignore').read()

        # Compute fields for the From_ line in a traditional mbox message
        _from = re.search(r"From: ([^\r\n]+)", message_text).groups()[0]
        _date = re.search(r"Date: ([^\r\n]+)", message_text).groups()[0]

        # Convert _date to the asctime representation for the From_ line
        _date = asctime(parse(_date).timetuple())

        msg = email.message_from_string(message_text)
        msg.set_unixfrom('From {0} {1}'.format(_from, _date))

        mbox.write(msg.as_string(unixfrom=True) + "\n\n")

mbox.close()


# ############################################################ #
#      Loading emails (Inbox folder only) data                 #
# ############################################################ #

mbox = mailbox.mbox(MBOX)

def load_emails(mbox):

    mbox_dict = {}
    for i, msg in enumerate(mbox):
        mbox_dict[i] = {}
        for header in msg.keys():
            mbox_dict[i][header] = msg[header]
            mbox_dict[i]['Body'] = msg.get_payload().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').strip()

    data_emails = pd.DataFrame.from_dict(mbox_dict, orient='index')
    return data_emails


# ############################################################ #
#      Loading the sms data                                    #
# ############################################################ #

def load_sms(sms_folder):

    for filename in os.listdir(sms_folder):
        if filename.endswith('.html'):
            fname = os.path.join(sms_folder, filename)
            with open(fname, 'r') as f:

                soup = BeautifulSoup(open(fname), "html.parser")
                sms = [p.text for p in soup.findAll("div", class_="text")]

                data_sms = json.dumps(sms, indent=4)
                return data_sms


# ############################################################ #
#      Loading the chats data                                  #
# ############################################################ #

def load_chats(chats_folder):

    for filenames in os.listdir(chats_folder):
        if filenames.endswith('.xml.html'):
            f_name = os.path.join(chats_folder, filenames)
            with open(f_name, 'r') as f:

                makesoup = BeautifulSoup(open(f_name), "html.parser")
                chats = [i.text for i in makesoup.findAll("div", class_="text")]

                data_chats = json.dumps(chats, indent=4)
                return data_chats