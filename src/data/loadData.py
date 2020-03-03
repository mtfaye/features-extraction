"""
LOAD THE RAW DATA AND CONVERT TO DATAFRAME FORMAT
 """

import os
import re
import sys
import json
import email
import mailbox
import pandas as pd
from time import asctime
from dateutil.parser import parse
from email.parser import Parser


# ############################################################ #
# Converting the raw data folder to a standardized mbox format #
# ############################################################ #

# path file data
path_file= '/Users/mouhamethtakhafaye/Desktop/behavox_assignment/data/immutable_input_data'


def parse_data(inputfile, msg_body, msg_subject_list):
    with open(inputfile, "rb") as f:
        data = f.read()

    messages = Parser().parsestr(data)

    msg_body.append(messages.get_payload())
    msg_subject_list.append(messages["subject"])


msg_body = []
msg_subject_list = []

for directory, subdirectory, filesnames in os.walk(path_file):
    for filesname in filesnames:
        parse_data(os.path.join(directory, filesname), msg_body, msg_subject_list)

with open("msg_body.txt", "w") as f:
    for msg_bod in msg_body:
        if msg_bod:
            f.write(msg_bod)
            f.write("\n")

with open("msg_subject_list.txt", "w") as f:
    for msg_subject in msg_subject_list:
        if msg_subject:
            f.write(msg_subject)
            f.write("\n")
