There are 3 versions of the `thread.html` file; ranging from simple to far too complicated.

1. `thread.html` simply shows which messages are from which participant, none of them are grouped or otherwise formatted.

2. `thread2.html` groups consecutive messages by the same author together, to reduce repeated info on the page.

3. `thread3.html` fixes an issue in 'thread2.html` where messages that might have been months or years apart are grouped; it introduces a maximum time gap before ungrouping again. This is something like how Facebook behaves.

All of the complicated code to do this resides in `macros.html` which is more Jinja2 templating code than HTML! It applies the correct class, and the CSS does the rest.

Any of the versions can be tried by changing [Line 40](https://github.com/jsharkey13/flask_facebook_messages/blob/master/server.py#L40) of `server.py` to the appropriate filename.
The time interval used when grouping is set by `_dt` on [Line 10](https://github.com/jsharkey13/flask_facebook_messages/blob/master/server.py#L10) of the same file.
