import imaplib as mail

class IMAPAuthService:

    def get_clients(self, webmails, clients={}):
        for webmail in webmails:
            client = mail.IMAP4_SSL(webmail['imap'], webmail['port'])
            client.login(webmail['username'], webmail['password'])
            clients.update({webmail['label']: client})
        return clients
