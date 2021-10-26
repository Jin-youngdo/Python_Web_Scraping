from flask import Flask, render_template,\
    request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file
db = {}

app = Flask("SuperScrapper")

# /(app의 경로)에 접속하면 발생하는 함수 생성
# 호스트의 웹 서버에 접속하면 보이는 문구
# @데코레이터 : 바로 밑 함수를 참조
@app.route("/")
def home() :
    return render_template("home.html")

# request.args.get() 함수를 통해 home.html(/)의 input 란에
# 입력한 word를 가져온다.
# render_template() 함수를 통해 함수 실행 시 해당 html로 이동
@app.route("/report")
def report() :
    word = request.args.get('word')
    # input란에 문자가 들어오면 소문자 처리,
    # 만약 아무것도 입력하지 않고 input한다면 home으로 redirect 처리
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs :
            jobs = existingJobs
        else :
            jobs = get_jobs(word)
            db[word] = jobs
    else :
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)

@app.route("/export")
def export() :
    try :
        word = request.args.get('word')
        if not word :
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs :
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except :
        return redirect("/")

app.run()