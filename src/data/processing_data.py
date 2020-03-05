from data.load_data import load_sms, load_emails, load_chats, mbox, emails_folder
from data.directory_root import path_file, MBOX, sms_folder, chats_folder


print(load_sms(sms_folder))

print(load_emails(emails_folder))

print(load_chats(chats_folder))



#serialize chats data json



#serialize sms data json



# Concat all three data to make a Corpus



# Save file on data folder





