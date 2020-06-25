from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request

from flask import make_response
import datetime
import json

# サンプルcookie
@app.route("/cookie")
def sample_cookie():
    count1 = request.cookies.get('count1')
    date = datetime.datetime.now()
    if count1 is None:
        count1 = 1
    else:
        count1 = int(count1) + 1
        print(date.strftime('%Y年%m月%d日 %H:%M:%S'))
    response = make_response("{}回目の訪問です".format(count1))
    response.set_cookie('count1', str(count1))


    return response





# 20章課題 cookie
@app.route("/cookie_kadai")
def cookie_kadai():
    # count = request.cookies.get('count')
    # if count is None:
    #     count = 1
    # else:
    #     count = int(count) + 1
    # response = make_response("{}回目の訪問です".format(count))
    # response.set_cookie('count', str(count))
    
    # count = datetime.datetime.now()
    # # now_time = count.strftime('%Y年%m月%D日 %H:%M:%S')
    # response_date = make_response(f"現在時刻：{count}"
    # return response_date

    # 変数宣言
    count = ""
    date_now = ""
    user_last_time = ""
    cookie = ""
    dic = ""


    dic = request.cookies.get('cookies_value')
    # dic = json.loads(cookie)

    if dic == None:
        count = ""
        user_last_time = ""

    else:
        count = dic["user_count"]
        user_last_time = dic["last_time"]


    # count = request.cookies.get('count')
    # last_time = request.cookies.get('last_time')
    date_now = datetime.datetime.now()
    # date_now = date.strftime('%Y年%m月 %H:%M:%S')

    if count == '':
        count = 1
    else:
        count = int(count) + 1


    user_count = "これで訪問数を表示できる？{}回目".format(count)
    user_date_time = "ここに現在時刻を表示する：{}".format(date_now)

    if user_last_time != "":
        response_count = make_response(render_template('cookie_kadai.html', user_count=user_count, user_date_time=user_date_time, user_last_time=user_last_time))
        # response_last_time = make_response(render_template('cookie_kadai.html', user_last_time=user_last_time))
    
    else:
        response_count = make_response(render_template('cookie_kadai.html', user_count=user_count, user_date_time=user_date_time))



    # response_count = make_response(render_template('cookie_kadai.html', user_count=user_count, user_date_time=user_date_time))

    # 前回訪れた時間を保存しておく
    user_last_time = "前回訪れた時間" + str(date_now)

    aaa = ""
    user_dic = {'user_count': str(count), 'last_time': user_last_time}
    response_count.set_cookie('cookies_value', value=user_dic)
    # response_count.set_cookie('cookies_value', value = json.dumps(user_dic))
    # response_count.set_cookie('count', str(count), 'last_time', user_last_time)
    # response_count.set_cookie('count', str(count))
    # response_count.set_cookie('last_time', user_last_time)
    # response_last_time.set_cookie('last_time', user_last_time)

    # user_date_time = "ここに現在時刻を表示する：{}".format(date_now)
    # response_time = make_response(render_template('cookie_kadai.html', user_date_time=user_date_time))
    # response_time.set_cookie('date_now', )


    # response_time = make_response("ここに現在時刻を表示する：{}".format(date_now))
    
    # return response_count
    # return response, response_count

    # params = {
    # "response_time" : response_time,
    # "response_count" : response_count
    # }

    # return render_template('cookie_kadai.html', **params)

    # return response_count, response_time

    # return response_count, response_time
    return response_count
