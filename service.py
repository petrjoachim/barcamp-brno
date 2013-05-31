
# coding: utf-8

from barcamp import app
from flask import abort, redirect, url_for, flash
from login_misc import check_auth, auth_required
from login import send_mail
from talks import get_talks
from entrant import user_user_go
from collections import defaultdict
from entrant import get_entrants


@app.route("/jedna-dve-tri-ctyri-pet/")
@auth_required
def prepocet_hlasu():
    user = check_auth()
    if user['email'] != u'petr@joachim.cz':
        abort(418)

    data = defaultdict(lambda: 0)
    keys = app.redis.keys('votes_*')
    for key in keys:
        members = app.redis.smembers(key)
        for member in members:
            data[member] += 1

    talk_tuples = app.redis.zrevrange('talks', 0, -1, withscores=True)
    for talk, score in talk_tuples:
        if 0 is not int(score - data.get(talk, 0)):
            print "update talk %s from %d to %d votes" % (talk, score, data.get(talk, 0))
            app.redis.zadd('talks', talk, data.get(talk, 0))

    return "omg"


@app.route('/jede-jede-postacek/')
@auth_required
def poslani_newsletteru():
    user = check_auth()
    if user['email'] != u'petr@joachim.cz':
        abort(418)

    entrants = get_entrants()
    for entrant in entrants:
        #print entrant['email']
        pass

    print send_mail(
        u'Barcamp se blíží',
        'jocho.jocho@gmail.com',
        'data/newsletter.md')

    return 'omg'
