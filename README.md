# Flask Facebook Messages
A simple server to view exported Facebook messages in a browser. Based on [Facebook Message Parser](https://github.com/jsharkey13/facebook_message_parser), adds a more reasonable user interface to the Python format.

#### Running the Code
The Python is all contained in `server.py` and can be run simply using `python server.py`. It will attempt to load in an export created by the [Facebook Message Parser](https://github.com/jsharkey13/facebook_message_parser) saved to `messages.pickle`; if this doesn't exist, creating it needs to be Step 1. See that repository for more instructions; but put the `messages.pickle` file created by adding the line `Facebook.dump_to_pickle()` to the end of `facebook.py` in the server directory along with `fb_chat.py`.

After that, run the server and open up a browser to `http://localhost:5000`. That's it!

It's only been properly tested in Chrome (or rather, Chrome is the only browser I attempted to make it work in), and large conversations may kill the server, since it loads them into memory to create the HTML page before sending it to the browser.

#### Dependencies
The code is written in Python 2.7

It relies upon many of the classes in [Facebook Message Parser](https://github.com/jsharkey13/facebook_message_parser), and may need those files adding to its directory in order to work correctly.

The server is powered by [Flask](http://flask.pocoo.org/), and the HTML templates all use the [Jinja2](http://jinja.pocoo.org/docs/dev/) templating engine.

The CSS is produced using [Sass](http://sass-lang.com/), compiled using [node-sass](https://github.com/sass/node-sass). To play with the Sass, try running `node-sass -w scss/ -o static/` from the main directory. Or just edit the CSS directly; it doesn't actually need the scss file once compiled!

[Anaconda Python](https://store.continuum.io/cshop/anaconda/) for scientific computing is a simple and easy way to install all the Python dependencies for the code, alongside many other useful libraries. It can be downloaded [here](http://continuum.io/downloads).
