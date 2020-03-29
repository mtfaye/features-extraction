from __PATH_FILES__ import communications_samples, MBOX
import os
import re
import email
import mailbox
from time import asctime
from dateutil.parser import parse

# Create a file handle that we'll be writing into...
mbox = open(MBOX, 'w+')

# Walk the directories and process all folders
for (root, dirs, file_names) in os.walk(communications_samples):
    if root.split(os.sep)[-1].lower() != 'inbox':
        continue

    # Process each message in 'inbox'.
    for file_name in file_names:
        file_path = os.path.join(root, file_name)
        message_text = open(file_path, errors='ignore').read()

        # Compute fields for the From_ line in a traditional mbox message.
        _from = re.search(r"From: ([^\r\n]+)", message_text).groups()[0]
        _date = re.search(r"Date: ([^\r\n]+)", message_text).groups()[0]

        # Convert _date to the asctime representation for the From_ line.
        _date = asctime(parse(_date).timetuple())

        msg = email.message_from_string(message_text)
        msg.set_unixfrom('From {0} {1}'.format(_from, _date))

        mbox.write(msg.as_string(unixfrom=True) + "\n\n")

mbox.close()

# Loading emails (Inbox folder only)
inbox_folder = mailbox.mbox
