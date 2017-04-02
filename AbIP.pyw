from tkinter import *
from tkinter import ttk
import requests
import time
'''



'''

def send():
    try:
        status.set("sending")
        root.update_idletasks()
        ipvalue = str(ip_address.get())
        value = str(categories.get())
        commentval = str(COMMENT.get())
        r = requests.get('https://www.abuseipdb.com/report/json?key=' + API_KEY + '&category=' + value + '&comment=' + commentval + '&ip=' + ipvalue)
        #print('https://www.abuseipdb.com/report/json?key=' + API_KEY + '&category=' + value + '&comment=' + commentval + '&ip=' + ipvalue)
        time.sleep(2)
        r.text
        exit()
    except ValueError:
        pass

API_KEY = '00000000000000000000000000'
root = Tk()
root.title("abuseIPdb")
root.iconbitmap('favicon.ico')
mainframe = ttk.Frame(root, padding="4 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ip_address = StringVar()
status = StringVar()
COMMENT = StringVar()
categories = StringVar()
ip_address_entry = ttk.Entry(mainframe, width=20, textvariable=ip_address)
ip_address_entry.grid(column=2, row=2, sticky=(W, E))
categories_entry = ttk.Entry(mainframe, width=20, textvariable=categories)
categories_entry.grid(column=2, row=1, sticky=(W, E))
COMMENT_entry = ttk.Entry(mainframe, width=20, textvariable=COMMENT)
COMMENT_entry.grid(column=2, row=4, sticky=(W, E))
status.set("waiting")
ttk.Label(mainframe, textvariable=status).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="send", command=send).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="IP to report").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="comment").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="IPV4").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="status").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="categories").grid(column=1, row=1, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

ip_address_entry.focus()
categories_entry.focus()
COMMENT_entry.focus()
root.bind('<Return>', send)

root.mainloop()
