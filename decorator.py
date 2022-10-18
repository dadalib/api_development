import json

def jsonify(func):
    def inner(*args):
        return json.dumps(func(*args),indent=2)

    return inner

@jsonify
def greet(greeting,recipient):
    return {'greetting':greeting,'recipient':recipient}

if __name__ == '__main__':
    print(greet('Hello','World'))
