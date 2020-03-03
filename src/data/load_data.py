
"""
LOAD THE RAW DATA AND CONVERT TO DATAFRAME FORMAT
 """

import re
import os
import sys
import json
import email
import mailbox
import pandas as pd
from time import asctime
from dateutil.parser import parse

# ############################################################ #
# Converting the raw data folder to a standardized mbox format #
# ############################################################ #

# path file data
path_file= '/Users/mouhamethtakhafaye/Desktop/behavox_assignment/data/immutable_input_data'

# Where to write the converted mbox
MBOX = '/Users/mouhamethtakhafaye/Desktop/behavox_assignment/data/immutable_input_data.mbox'

# Create a file handle that we'll be writing into...
mbox = open(MBOX, 'w+')

# Walk the directories and process any folder named 'inbox'
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
#      Loading the mailbox data into Pandas                    #
# ############################################################ #

mbox = mailbox.mbox(MBOX)

mbox_dict = {}
for i, msg in enumerate(mbox):
    mbox_dict[i] = {}
    for header in msg.keys():
        mbox_dict[i][header] = msg[header]
    mbox_dict[i]['Body'] = msg.get_payload().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').strip()

df = pd.DataFrame.from_dict(mbox_dict, orient='index')

df.to_pickle('01_raw.pkl')
