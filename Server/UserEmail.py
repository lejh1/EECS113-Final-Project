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
 
    #   The IMAPClient search returns a list of Id's that match the given criteria.
    #   An Id in this case identifies a specific email
    def checkEmailSubjects(self, subject):
        #   search within Inbox
        self.server.select_folder('INBOX')  
 
        #   build the search criteria (e.g. unread emails with the given subject)
        self.searchCriteria = ['UNSEEN', 'SUBJECT', subject]
 
        #   conduct the search and return the resulting Ids
        return self.server.search(self.searchCriteria)

     #  Mark specic email as read
    def markAsRead(self, mailIds, folder='INBOX'):
        self.server.select_folder('INBOX')  
        self.server.set_flags(mailIds, [SEEN])

