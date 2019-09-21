
class Worker():

    # Worker parameterized constructor
    def __init__(self, name, title, team, id, branch, phoneNumber, email, manager, specialties, knownSites, helpfulNotes):
        self.name = name
        self.title = title
        self.team = team
        self.id = id
        self.branch = branch
        self.phoneNumber = phoneNumber
        self.email = email
        self.manager = manager
        self.specialties = specialties
        self.knownSites = knownSites
        self.helpfulNotes = helpfulNotes

    def scheduleMeeting(self, time, location, date):

