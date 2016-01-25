import flask
import os
import pickle
import datetime
app = flask.Flask("__name__")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Group messages together if time between is less than this amount:
_dt = datetime.timedelta(minutes=5)
# This is really not secure or file safe, but will work for local purposes:
f = open("messages.pickle", "r")
Chat = pickle.load(f)
f.close()


def format_datetime(date, at=False):
    if at:
        format = "%d %B %Y at %H:%M%p"
    else:
        format = "%d/%m/%Y  %H:%M"
    return date.strftime(format)
app.jinja_env.filters['datetime'] = format_datetime


@app.route('/')
def home():
    return flask.render_template('index.html', chat=Chat, _myname=Chat._myname)


@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png', mimetype='image/png')


@app.route('/thread/<username>')
def thread(username):
    if username not in Chat._thread_dict:
        return page_not_found("There is no thread with name \"%s\"." % username)
    return flask.render_template('thread3.html', thread=Chat[str(username)], _myname=Chat._myname,
                                 chat=Chat, dt=_dt)


@app.route('/thread')
def thread_blank():
    return flask.redirect('/')


@app.route('/thread/')
def thread_blank_slash():
    return flask.redirect('/')


@app.route('/search', methods=["POST", "GET"])
def search():
    if (flask.request.method == 'POST'):
        string = flask.request.form['search_str']
        thread_name = flask.request.form["search_thread"]
        scope = str(flask.request.form["search_scope"])
        if thread_name == "":
            scope = "CHAT"
        if scope == "THREAD":
            if string == "":
                return thread(thread_name)
            return flask.render_template("search_thread.html", thread=Chat[str(thread_name)],
                                         messages=Chat[str(thread_name)].search(string),
                                         search_str=string, chat=Chat)
        else:
            if string == "":
                return home()
            messages = sorted(Chat.search(string), key=lambda m: m.thread_name)
            return flask.render_template("search_chat.html", messages=messages,
                                         search_str=string, total_messages=Chat._total_messages,
                                         chat=Chat)
    else:
        return home()


@app.errorhandler(404)
def page_not_found(error=None):
    return flask.render_template('404.html', error=error), 404


if __name__ == '__main__':
    print "Starting Server . . ."
    # Run a server in debug mode. DO NOT SPECIFY 'host='! That would allow anyone
    # to access both your data and a Python console running on your machine!
    app.run(debug=True)
