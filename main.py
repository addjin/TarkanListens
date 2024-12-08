import gmailUtil
import util


mastersEmails = util.readLinesToList('./masters.txt')
service = gmailUtil.getGmailService()

response = gmailUtil.getUnreadMessages(service)

print(response)