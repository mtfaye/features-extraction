"""
The result of our scrapped data above are actually a list of text
We are going to change for each result into one giant string of text.
                                                                      """

from data.root import *
from data.data_loading import *


# Takes a list of text and combines them into one large chunk of text.
def combine_text(list_of_text):
    combined_text = ' '.join(list_of_text)
    return combined_text


raw_sms = combine_text(load_sms(sms_folder))
raw_chats = combine_text(load_chats(chats_folder))
raw_emails = combine_text(load_emails(emails_folder))

# Concat data
my_dict = {'SMS': raw_sms, 'CHATS': raw_chats, 'EMAILS': raw_emails}


# Save result in data folder.
with open(data_folder_path + 'raw_data' + '.json', 'w') as outfile:
    json.dump(my_dict, outfile)
