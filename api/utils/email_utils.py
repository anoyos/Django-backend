

def sendy_subscribe(email, username):
    from sendy.api import SendyAPI
    api = SendyAPI(
        host='https://newsletter.cgafrica.com',
        api_key='j3EzTaXINuWggfQbvGoR',
    )
    res = api.subscribe(
        '763j1dKWA763ZB7636xmi3mI0M0w',
        email,
        username
    )
    print(res)


def sendy_subscribe_v2(email, username):
    from sendy.api import SendyAPI
    api = SendyAPI(
        host='https://newsletter.cgafrica.com',
        api_key='j3EzTaXINuWggfQbvGoR',
    )
    res = api.subscribe(
        't2Mr763F8cYw4pQmttWKi7OQ',
        email,
        username
    )
    print(res)



