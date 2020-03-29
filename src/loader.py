import os
import pandas as pd
from bs4 import BeautifulSoup
from mailbox import inbox_folder
from __PATH_FILES__ import *


def combine(sms, chats, inbox):
    """Takes a list of texts and combines them into one large chunk of text."""
    sms = ' '.join(sms)
    chats = ' '.join(chats)
    inbox = ' '.join(inbox)
    return {'SMS': sms, 'CHATS': chats, 'EMAILS': inbox}


class Loader(object):
    """Scrapes the body of messages for each folder."""

    def __init__(self, sms_folder, chats_folder, inbox_folder):
        self.sms_folder = sms_folder
        self.chats_folder = chats_folder
        self.inbox_folder = inbox_folder

    def sms(self):
        """Scrapes sms and stores in a list."""

        data_sms = []
        for filename in os.listdir(sms_folder):
            if filename.endswith('.html'):
                fname = os.path.join(sms_folder, filename)
                with open(fname, 'r') as f:
                    soup = BeautifulSoup(open(fname), "html.parser")
                    sms = [k.text for k in soup.findAll("div", class_="text")]
                    data_sms.append(sms)
                    list_sms = []
                    for items in data_sms:
                        list_sms.extend(items)
        return list_sms

    def chats(self):
        """Scrapes chats and stores in a list."""

        data_chats = []
        for filenames in os.listdir(chats_folder):
            if filenames.endswith('.xml.html'):
                f_name = os.path.join(chats_folder, filenames)
                with open(f_name, 'r') as f:
                    makesoup = BeautifulSoup(open(f_name), "html.parser")
                    chats = [p.text for p in makesoup.findAll("div", class_="text")]
                    data_chats.append(chats)
                    list_chats = []
                    for item in data_chats:
                        list_chats.extend(item)
        return list_chats

    def inbox(self):
        """Scrapes Inbox and stores in a list."""

        emails_dict = {}
        for i, msg in enumerate(inbox_folder):
            emails_dict[i] = {}
            for header in msg.keys():
                emails_dict[i][header] = msg[header]
                emails_dict[i]['Body'] = msg.get_payload().replace('\n', ' ').replace('\t', ' ').replace('\r',' ').strip()
        data = pd.DataFrame.from_dict(emails_dict, orient='index')
        list_emails = data.Body.tolist()
        return list_emails


loader = Loader(sms_folder, chats_folder, inbox_folder)
