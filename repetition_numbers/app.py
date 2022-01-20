import json

# import requests
# 最初に2以上の整数値を入力し、次の規則で計算し、計算回数と計算結果を表示し、計算結果が1になるまで繰り返すプログラムを作成せよ。
# 規則：ある値が偶数ならその値を1/2にする。奇数ならその値を3倍して1を足す。

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def is_repetition_numbers(num): 
    lists = []
    while  num !=1:
        if num%2 == 0:
            num = num//2
            lists.append(num)
        else:
            num = num*3+1
            lists.append(num)
        num = int(num)
    else:
        None
    return lists

def validate_number(x):
    if x < 2:
        raise InvalidError("2以上の整数値を入力してください。")




def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = number(n)
        validate_number(n)
        print(n)
    except Exception as e:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":str(e)
        },ensure_ascii=False).encode("utf8"),
    }
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    results = is_repetition_numbers(n)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "count": len(results),
            "result":results,
            # "location": ip.text.replace("\n", "")
        }),
    }
