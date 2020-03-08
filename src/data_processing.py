"""
The result of our scrapped data above are actually a list of text
We are going to change for each result into one giant string of text.
                                                                      """
import json
from root import *
from data_loading import sms_folder, load_sms, chats_folder, load_chats, emails_folder, load_emails


def combine_text(list_of_text):
    # Takes a list of text and combines them into one large chunk of text.

    combined_text = ' '.join(list_of_text)
    return combined_text


raw_sms = combine_text(load_sms(sms_folder))
raw_chats = combine_text(load_chats(chats_folder))
raw_emails = combine_text(load_emails(emails_folder))

# Concat data
my_dict = {'SMS': raw_sms, 'CHATS': raw_chats, 'EMAILS': raw_emails}

# Save result in data folder.
with open(outfiles + 'raw_data' + '.json', 'w') as outfile:
    json.dump(my_dict, outfile)
