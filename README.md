# Show Unread IMAP Emails
Polybar client for checking email status, you can add as much webmails as you want.

Polybar .dot file changes:
```
[module/unread_mail]
type = custom/script
label = %{F#3caea3} %{F-}%output%
format = <label>
exec = python .config/polybar/scripts/UnreadEmails/unreademails.py
interval = 5
```

When there are unread images, number is shown as red
![This is an image](/images/2022-01-15_23-27.png)

Otherwise it is green
![This is an image](/images/2022-01-15_23-29.png)

Label can be shown as text or icon (fontawesome used by me for gmail):
```
webmails = [
    {
        'imap': 'your.imap.server.com', # set your email server
        'port': 993,
        'username': 'your_username_or_email',
        'password': 'your_password',
        'label': 'my@email.com' # show email label on polybar
    }, {
        'imap': 'imap.gmail.com',
        'port': 993,
        'username': 'your.email@gmail.com',
        'password': 'your_password',
        'label': '' # show icon on polybar (fontawesome)
    }
]
```
