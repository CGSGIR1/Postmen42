class Email:
    def __init__(self, recipient, subject, body, source_path):
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.source_path = source_path