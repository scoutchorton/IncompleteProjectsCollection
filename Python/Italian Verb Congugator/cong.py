class cong(object):
    def __init__(self, verb):
        self.verb = verb.lower()
        self.text = ""
        self.irregular = ["avere", "stare", "fare"]

    def are(self):
        print "-are verb"
        self.text = self.text  + self.verb

    def ere(self):
        print "-ere verb"
        self.text = self.text  + self.verb

    def ire(self):
        print "-ire verb"
        self.text = self.text  + self.verb

    def ret(self):
        return self.text

    def run(self):
        print self.verb[-3:]
        if self.verb[-3:] == "are":
            self.are()
        elif self.verb[-3:] == "ere":
            self.ere()
        elif self.verb[-3:] == "ire":
            self.ire()
        else:
            return "Not an are/ere/ire verb."
        self.ret()
