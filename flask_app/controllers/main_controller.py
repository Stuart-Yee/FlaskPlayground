from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.config.settings import bcrypt
from flask_app.config.codes import codes

@app.route("/")
def root_route():
    if not session.get("blah"):
        session["blah"] = 1
    else:
        session["blah"] += 1
    return render_template("index.html")

GUESSES = [
    '123456789',
    'aaron',
    'samples',
    'Aaron',
    'Samples',
    'AaronSamples',
    '123456789',
    'pa55word',
    'pa55w0rd',
    '123456',
    'qwerty',
    'password',
    '12345',
    '12345678',
    '111111',
    '1234567',
    '123123',
    'qwerty123',
    '1q2w3e',
    '1234567890',
    'DEFAULT',
    '000000',
    'abc123',
    '654321',
    '123321',
    'qwertyuiop',
    'Iloveyou',
    '666666',
    'KI6FZB',
    'RAWANN',
    'SHELDURAY88',
    'KJ1017',
    'PUSSY310',
    'KARAAGE4',
    'TH3EMPRESS',
    'ELLEGRA',
    '81PIRTER73',
    'KORRESHI',
    'CLC47',
    'ROMELP',
    'OFTROY',
    'MVN2006',
    'MIKYONE',
    'JAMFILE',
    'TRIATA',
    'IAMTHATIS',
    'PEACHKA1',
    'JAHAAD',
    'SARAHMIA1',
    'LEBIN',
    'WINGK2',
    'CHARLIEXX',
    'MB1229',
    'EMETI',
    'KITABLAR',
    'JENGARY',
    'GODSPELL2',
    'LETSTALK2',
    '1MEMO1',
    'jeff',
    'billy'
]

@app.route("/hash-test/<hash>")
def render_hash_with_hash(hash):
    hashed_bytes = bcrypt.generate_password_hash(hash)
    hashed = hashed_bytes.decode('utf-8')
    test = None
    for key, val in codes.items():
        if hashed == val:
            test = key

    winner = None

    for key, val in codes.items():
        print(f"checking for {key}:")
        for guess in GUESSES:
            if bcrypt.check_password_hash(val, guess):
                winner = f"Cracked {key}, passowrd is {guess}"
                print(winner)
                break
            else:
                print(f"Didn't score with {guess}")
        if winner:
            break


    return render_template("hashform.html", hashed=hashed, test=test)

@app.route("/hash-test")
def render_hash():

    return render_template("hashform.html", hashed=None, test=None)

@app.route("/hash-submit", methods=["POST"])
def receive_hash():
    unhashed = request.form.get("unhashed")
    return redirect(f"/hash-test/{unhashed}")


@app.route("/potato")
def potato_route():
    return render_template("index.html")