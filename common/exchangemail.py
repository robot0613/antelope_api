from exchangelib import  DELEGATE, Account, Credentials, Message, Mailbox, HTMLBody, FileAttachment

class  ExchangeMail():

    def __init__(self,username,password):

        self.username=username
        self.password=password


    def sendmail(self,subject,body,filename,receiver):

        creds = Credentials(
            username=self.username,
            password=self.password
        )

        account = Account(
            primary_smtp_address=self.username,
            credentials=creds,
            autodiscover=True,
            access_type=DELEGATE
        )
        to_recipients=[]
        for to in receiver:
            to_recipients.append(Mailbox(email_address=to))

        m = Message(
            account=account,
            subject=subject,
            body=HTMLBody(body),
            to_recipients=to_recipients,
        )

        file= FileAttachment(name='Test_report.html', content=open(filename, 'rb').read())
        m.attach(file)
        m.send()



