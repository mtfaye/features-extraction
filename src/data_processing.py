"""
The result of our scrapped data above are actually a list of text
We are going to change for each result into one giant string of text.
                                                                      """
import json
from root import *
from data_loading import sms_folder, chats_folder, emails_folder, __load_emails__, __load_chats__, __load_sms__


def combine(list_of_text):
    # Takes a list of text and combines them into one large chunk of text.

    combined_text = ' '.join(list_of_text)
    return combined_text


raw_sms = combine(__load_sms__(sms_folder))
raw_chats = combine(__load_chats__(chats_folder))
raw_emails = combine(__load_emails__(emails_folder))

# Concat data
my_dict = {'SMS': raw_sms, 'CHATS': raw_chats, 'EMAILS': raw_emails}

# Save result in data folder.
with open(outfiles + 'raw_data' + '.json', 'w') as outfile:
    json.dump(my_dict, outfile)
