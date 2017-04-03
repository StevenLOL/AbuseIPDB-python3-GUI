from tkinter import *
from tkinter import ttk
import requests
import time


def test_test_send():
    try:
        status.set("test_sending")
        root.update_idletasks()
        ip_value = str("1")
        cat_value = str("1")
        comment_value = str(1)
        url = 'https://www.abuseipdb.com/report/json?key='
        final_value = url + api_key + '&category=' + cat_value + '&comment=' + comment_value + '&ip=' + ip_value
        # requests.get(final_value)
        print(final_value)
    except ValueError:
        pass
    assert final_value == "https://www.abuseipdb.com/report/json?key=0000000000000000000000000000&category=1&comment=1&ip=1"

api_key = '0000000000000000000000000000'
root = Tk()
root.title("abuseIPdb")
#root.iconbitmap('favicon.ico')
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
ttk.Button(mainframe, text="test_send", command=test_send).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="IP to report").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="comment").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="IPV4").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="status").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="categories").grid(column=1, row=1, sticky=W)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

ip_address_entry.focus()
categories_entry.focus()
COMMENT_entry.focus()
root.bind('<Return>', test_send)

root.mainloop()





def test_pass():
    val = 1 * 1

    assert val == 1