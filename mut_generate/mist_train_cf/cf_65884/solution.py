"""
QUESTION:
Implement a function `handle_smtp_reply` that takes a three-digit SMTP reply code as input and returns a corresponding explanatory phrase. The function should also handle instances of queued email status reports. The function should have a time complexity of O(1).
"""

def handle_smtp_reply(code):
    smtp_reply_codes = {
        250: "Requested mail action okay, completed",
        421: "Service not available, closing transmission channel",
        450: "Requested mail action not taken: mailbox unavailable",
        451: "Requested action aborted: error in processing",
        452: "Requested action not taken: insufficient system storage",
        500: "Syntax error, command unrecognized",
        501: "Syntax error in parameters or arguments",
        502: "Command not implemented",
        503: "Bad sequence of commands",
        504: "Command parameter not implemented",
        550: "Requested action not taken: mailbox unavailable",
        551: "User not local; please try <forward-path>",
        552: "Requested mail action aborted: exceeded storage allocation",
        553: "Requested action not taken: mailbox name not allowed",
        554: "Transaction failed"
    }
    
    if 400 <= code <= 499:
        return "Transient Negative Completion reply"
    elif 500 <= code <= 599:
        return "Permanent Negative Completion reply"
    elif code in smtp_reply_codes:
        return smtp_reply_codes[code]
    else:
        return "Unknown SMTP reply code"