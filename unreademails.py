#!/usr/bin/env python3
from services import IMAPAuthService

class Email:
    def __init__(self, webmails):
        self.webclients = IMAPAuthService().get_clients(webmails)

    def colorize(self, label, unread):
        color = 'F#e60053' if unread >= 1 else 'F#49be25'
        return f"{label} %{{{color}}}{unread}%{{F-}}"

    def get_all_unread_emails(self):
        print(self.get_unread_emails())

    def get_inbox_unread_emails(self):
        print(self.get_unread_emails('INBOX'))

    def get_unread_emails(self, folder=None, status=[]):
        for label, webclient in self.webclients.items():
            webclient.select(folder) if folder else webclient.select()
            unread = len(webclient.search(None, 'UNSEEN')[1][0].split())
            status.append(self.colorize(label, unread))
        return f'{folder if folder else "ALL"} [{" | ".join(status)}]'

webmails = [
    {
        'imap': 'your.imap.server.com', # set your email server
        'port': 993,
        'username': 'your_username_or_email',
        'password': 'your_password',
        'label': 'my@email.com' # show email label on polybar
    }, {
        'imap': 'imap.gmail.com',
        'port': 993,
        'username': 'your.email@gmail.com',
        'password': 'your_password',
        'label': '' # show icon on polybar (fontawesome)
    }
]

Email(webmails).get_all_unread_emails()
