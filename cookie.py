from flask import make_response
@app.route("/cookie")
def sample_cookie():
    count = request.cookies.get('count')
    if count is None:
        count = 1
    else:
        count = int(count) + 1
    response = make_response("{}回目の訪問です".format(count))
    response.set_cookie('count', str(count))
    return response
