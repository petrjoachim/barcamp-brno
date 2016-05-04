# coding: utf-8

from barcamp import app
from flask import render_template, abort, send_from_directory
from login_misc import check_auth, get_account
from talks import get_talks, get_talks_dict
from workshops import get_workshops
from utils import markdown_static_page, markdown_markup, stage_is_active
from entrant import get_count, get_entrants
from vote import get_user_votes
from program import times
import os

@app.route("/", redirect_to="/%s/index.html" % app.config['YEAR'])
@app.route("/%s/" % app.config['YEAR'], redirect_to="/%s/index.html" % app.config['YEAR'])
@app.route("/%s/index.html" % app.config['YEAR'])
def index():
    if stage_is_active(app.config['YEAR'], 'PROGRAM_READY'):
        talks = get_talks_dict()
        extra_talks = []
    else:
        talks, extra_talks = get_talks()

    workshops = get_workshops()

        # bez razeni talks = sorted(talks, key=lambda x: x['title'])

    stage_template = "index.html"
    if stage_is_active(app.config['YEAR'], 'END'):
        stage_template = "end.html"

    if stage_is_active(app.config['YEAR'], 'PREVIEW'):
        stage_template = "preview.html"

    return render_template(
        stage_template,
        times=times,
        entrant_count=get_count(),
        entrants=get_entrants()[:50],
        novinky=markdown_markup('novinky'),
        talks=talks, extra_talks=extra_talks,
        talks_dict=get_talks_dict(),
        workshops=workshops
    )


@app.route('/%s/ucastnici.html' % app.config['YEAR'])
def entrants():
    return render_template(
        "entrants.html",
        entrant_count=get_count(),
        entrants=reversed(get_entrants())
    )


@app.route('/%s/partneri.html' % app.config['YEAR'])
def sponsors():
    return render_template(
        "partneri.html",
        sponsors_other=markdown_markup('sponsors_other'),
    )

@app.route('/%s/doprovodny-program.html' % app.config['YEAR'])
def co_program():
    return render_template(
        "doprovodny-program.html"
    )


@app.route('/%s/pracovni-nabidky.html' % app.config['YEAR'])
def job_wall():
    return render_template(
        "job-wall.html"
    )


@app.route('/%s/prednasky.html' % app.config['YEAR'])
def talks_all():
    user = check_auth()
    user_hash = None
    talks, extra_talks = get_talks()

    if user:
        user_hash = user['user_hash']

    return render_template(
        "talks.html",
        talks=talks,
        user_votes=get_user_votes(user_hash),
        extra_talks=extra_talks
    )

@app.route('/%s/workshopy.html' % app.config['YEAR'])
def workshops_all():
    workshops = get_workshops()
    return render_template(
        "workshops.html",
        workshops=workshops,
    )

@app.route('/profil/<user_hash>/')
def profile(user_hash):
    data = get_account(user_hash)
    if not data:
        abort(404)

    return render_template(
        'profil.html',
        profile=data
    )

def stranky():
    files = []
    for _, _, keys in os.walk('data/%s' % app.config['YEAR']):
        files += keys;

    return [{"page": key.replace(".md", "")} for key in files]

@app.route("/%s/stranka/<page>.html" % app.config['YEAR'], generator=stranky)
def static_page(page):
    return markdown_static_page(page)


def archive_proxy(year, path):
    year = str(year)
    # send_static_file will guess the correct MIME type
    return send_from_directory(
        os.path.abspath('archive'),
        os.path.join(year, path)
    )


for year in app.config['YEAR_ARCHIVE']:
    app.add_url_rule(
        '/%s/<path:path>' % year,
        defaults={'year': year},
        view_func=archive_proxy
    )

