""" epoch time script """

# imports
import os
import datetime
import pandas as pd
from flask import Flask
# ==================================

APP = Flask(__name__)
# ---------------------------------

# APP.secret_key = b"\xe0\x95\xf2`W8'X,2\xfc\x88Z\x8c\x97\xad~1\xd8k\xbb\xaf\xd7\xab"
# APP.secret_key = os.environ.get('SECRET_KEY').encode()
# ------------------------------------------

def time_format(time):
    """ format time """
    day_of_week = pd.Timestamp(time).day_name()
    month_of_year = pd.Timestamp(time).month_name()
    day = str(pd.Timestamp(time).day)
    year = str(pd.Timestamp(time).year)
    hms = time.strftime("%H:%M:%S")

    return ", ".join((day_of_week, " ".join((month_of_year, day)), year, hms))

def time_conversion(epoch):
    """ response -> local and GMT time corresponding to epoch time """
    local_time = datetime.datetime.fromtimestamp(epoch)
    gmt_time = datetime.datetime.utcfromtimestamp(epoch)

    return "\n ".join(["".join(("Local time: ", time_format(local_time))),
                       " || ",
                       "".join(("GMT: ", time_format(gmt_time)))])

# ---------------------------------
@APP.route('/')
def base():
    """ application """
    page = """
        <b>Enter epoch (10-dig.) in url (eg:/1581709472) to get datetime</b>
        """
    return page

@APP.route('/<epoch_time>/')
def epoch_tm(epoch_time):
    """ application """
    dtm = time_conversion(int(epoch_time))
    page = """
        <b>{0}</b>
        <hr></hr>
            <a href="/">Back to start-up page</a>
        <hr></hr>
        """.format(dtm)

    return page

# =================================
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    APP.run(host="0.0.0.0", port=PORT)
    #APP.run(debug=True)
