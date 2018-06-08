from imapclient import IMAPClient, SEEN
  
class UserEmail:
    def __init__(self):
        #JujuPi Gmail Login Credentials
        self.host = 'imap.gmail.com'
        self.userName = "JujuPi2018@gmail.com"
        self.password = "Juju2018"
        self.login()
 
    def login(self):
        server = IMAPClient(self.host, use_uid=True, ssl=True)
        server.login(self.userName, self.password)
        self.server = server
 
        #   Searches thru the Email's Inbox and returns an ID number corresponding to
        #   the ID number of the email if found, if it doesnt find anything then it returns empty
    def checkEmailSubjects(self, subject):
        #   search within Inbox
        self.server.select_folder('INBOX')  
 
        #   build the search criteria (e.g. unread emails with the given subject)
        self.searchCriteria = ['UNSEEN', 'SUBJECT', subject]
 
        #   Conduct the search and return the resulting Ids
        return self.server.search(self.searchCriteria)

        #   Mark specic email as read using the ID
    def markAsRead(self, mailIds, folder='INBOX'):
        self.server.select_folder('INBOX')  
        self.server.set_flags(mailIds, [SEEN])

