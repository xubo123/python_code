from flask import Flask
from redis import Redis 

app = Flask(__name__)
redis = Redis(host = "192.168.58.135",port="6379")
@app.route("/add/<int:added_number>")
def add(added_number):
    try:
        print "added_number:" + repr(added_number)
        if redis.get("count") == None:
            redis.set("count",1)
        else:
            count = int(redis.get("count")) + added_number
            print "count:" + repr(count)
            redis.set("count", count)
    except Exception, e:
        print repr(e)
        return "add failed!"
    return "Successfully add count!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
