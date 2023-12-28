from flask import Flask, render_template, url_for, session, request, redirect
import os
import constants
import db_api

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = str(os.urandom(20).hex())
@app.route('/index.html')
@app.route('/')
def index():
    return render_template("index.html", autors=constants.AUTORS)
@app.route('/whoami.html', methods=["GET", "POST"])
def whoami():
    if ("isAutorise" in session):
        return render_template("whoami.html", who=session['user'], ads=session['ads'])
    else:
        return render_template("login.html")

@app.post("/login.html")
def login():
    login = request.form.get('loginName')  # запрос к данным формы
    firstName = request.form.get("firstName")
    secondName = request.form.get("secondName")
    lastName = request.form.get("lastName")
    password = request.form.get('password')
    email = request.form.get("email")
    work = request.form.get("work")
    numberOfPasportOfPasika = request.form.get("numberOfPassportofPasika")
    numberOfFamily = request.form.get("numberOfFamily")
    isStat = request.form.get("isStat")
    hasMoveablePlotform = request.form.get("hasMoveablePlotform")
    purpose = request.form.get("purpose")
    about = request.form.get("about")
    loginOrReg = request.form.get("loginOrReg")
    phone = request.form.get("phone")

    #print(loginOrReg)

    if (loginOrReg == "login"):
        info, ads = db_api.find_user(login, password)
        if (not (info == None)):
            session["isAutorise"] = 1
            session["user"] = info
            session["ads"] = ads
        else:
            session["isAutorise"] = 1
            session["user"] = constants.WHOAMI
            session["ads"] = constants.Ads
    elif (loginOrReg == "registr"):
        user_info = {
            "Login": login,
            "Passwd": password,
            "Name": lastName + " " + firstName + " " + secondName,
            "Work": work,
            "Email": email,
            "Telephon": phone,
            "About": about,
            "numberOfPassportofPasika": numberOfPasportOfPasika,
            "numberOfFamily": numberOfFamily,
        }
        if (isStat == 'stat'):
            user_info["isStat"] = "Стационар"
        else:
            user_info["isStat"] = "Кочевка"

        if (hasMoveablePlotform == "yes"):
            user_info["hasMoveablePlotform"] = "Да"

        if (purpose == "med"):
            user_info["purpose"] = "Цель: медовое направление"
        elif (purpose == "razvod"):
            user_info["purpose"] = "Цель: Разведение"
        elif (purpose == "opul"):
            user_info["purpose"] = "Цель: Опыление"

     #   print(user_info)
        status = db_api.regist_user(user_info)

    return redirect("whoami.html")


@app.route("/AddAdd.html")
def AddAddHTML():
    return render_template("AddAdd.html")

@app.route("/AddAdd/", methods=["POST",])
def AddAdd():
    title = request.form.get("title")
    id = request.form.get("id")
    adres = request.form.get("adres")
    about = request.form.get("about")
    #print(title, id, adres, about, session)
    newAdd = {
        "Title": title,
        "id": int(id),
        "Adres": adres,
        "About": about
    }
    status = db_api.add_ads_for_user(session["user"]["Login"], session["user"]["Passwd"], newAdd)
    session["ads"] += [newAdd]
    return redirect("/whoami.html")
@app.route("/changeAdd.html")
def changeAddHTML():
    return render_template("changeAdd.html")

@app.route("/ChangeAdd/", methods=["POST",])
def ChangeAdd():
    title = request.form.get("title")
    id = request.form.get("id")
    adres = request.form.get("adres")
    about = request.form.get("about")
    #print(title, id, adres, about, session)
    newAdd = {
        "Title": title,
        "id": int(id),
        "Adres": adres,
        "About": about
    }
    status = db_api.change_add_for_user(session["user"]["Login"], session["user"]["Passwd"], newAdd)
    index = 0
    for i, add in enumerate(session["ads"]):
        #print(i, add)
        if add['id'] == newAdd['id']:
         #   print(add['id'], newAdd['id'])
            index = i
            #print("index found")

    sAds = session.get("ads")
    sAds[index] = newAdd
    session['ads'] = sAds
    return redirect("/whoami.html")

@app.route("/removeAdd.html")
def removeAddHtml():
    return render_template("/removeAdd.html")

@app.route("/removeAdd/", methods=["POST",])
def removeAdd():
    id = int(request.form.get("id"))
    status = db_api.remove_add_for_user(session["user"]["Login"], session["user"]["Passwd"], id)
    index = 0
    for i, add in enumerate(session["ads"]):
        #print(i, add)
        if add['id'] == id:
            #print(add['id'], newAdd['id'])
            index = i
            #print("index found")

    sAds = session.get("ads")
    rm = sAds.pop(index)
    session['ads'] = sAds
    return redirect("/whoami.html")

@app.route("/beekeepers.html")
def beekeepers():
    adsf = db_api.find_all_ads_with_category("beekeepers")
    if not (adsf == None):
        return render_template("/beekeepers.html", ads=adsf)
    else:
        user = constants.WHOAMI
        adsf = constants.Ads
        for a in adsf:
            a["FIO"] = user["Name"]
            a["Tel"] = user["Telephon"]
        return render_template("/beekeepers.html", ads=adsf)

@app.route("/farmers.html")
def farmers():
    adsf = db_api.find_all_ads_with_category("farmers")
    if not (adsf == None):
        return render_template("/farmers.html", ads=adsf)
    else:
        # user = constants.WHOAMI
        # adsf = constants.Ads
        # for a in adsf:
        #     a["FIO"] = user["Name"]
        #     a["Tel"] = user["Telephon"]
        return render_template("/farmers.html", ads=None)


@app.route("/advertisers.html")
def advertisers():
    adsf = db_api.find_all_ads_with_category("advertisers")
    if not (adsf == None):
        return render_template("/advertisers.html", ads=adsf)
    else:
        # user = constants.WHOAMI
        # adsf = constants.Ads
        # for a in adsf:
        #     a["FIO"] = user["Name"]
        #     a["Tel"] = user["Telephon"]
        return render_template("/advertisers.html", ads=None)


@app.route("/workers.html")
def workers():
    adsf = db_api.find_all_ads_with_category("workers")
    if not (adsf == None):
        return render_template("/workers.html", ads=adsf)
    else:
        # user = constants.WHOAMI
        # adsf = constants.Ads
        # for a in adsf:
        #     a["FIO"] = user["Name"]
        #     a["Tel"] = user["Telephon"]
        return render_template("/workers.html", ads=None)

@app.route("/roscoltrol.html")
def roscoltrol():
    return render_template("/roscoltrol.html")

@app.route("/selectRegion.html")
def selectRegion():
    return render_template("/selectRegion.html")

if __name__ == '__main__':
    app.run()