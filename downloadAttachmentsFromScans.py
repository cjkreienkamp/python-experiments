import ezgmail

searchCriteria = input('Enter search: ')

threads = ezgmail.search(searchCriteria)

if len(threads) == 0:
    print('No emails found matching your search')
    
else:    
    
    while (len(threads)):
        for thread in threads:
            if thread.messages[0].subject == '':
                thread.messages[0].downloadAllAttachments(downloadFolder=thread.messages[0].body)
            else:    
                thread.messages[0].downloadAllAttachments(downloadFolder=thread.messages[0].subject)
    
        ezgmail.markAsRead(threads)
        threads = ezgmail.search(searchCriteria)

print('COMPLETED')    
