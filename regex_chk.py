import re

def chkMailForm(txt):
    if re.match(r"(.*)@testmail.[com|net]{3}\b", txt):
        print('Email format is correct:',txt)
    else:
        print('Email format is incorrect:',txt)

def chkPhonNum(txt):
    # print(txt)
    if re.match(r"^02[0-9]{7}\b", txt):
      print('Phone nubmer format is correct:',txt)
    elif re.match(r"^08[0-9]{8}\b", txt):
      print('Phone nubmer format is correct:',txt)
    else:
      print('Phone nubmer format is incorrect:',txt)

def main():
    email = ['yellow@hotmail.com','brown@testmail.co','orange@gmail.net','black@testmail.nnet','white@testmail.net','red@testmail.com']
    phone_number = ['023912483','0239124834','02391248','0847837273','084783727','08478372733','084783727j','0147837273']

    for val in email:
        chkMailForm(val)

    # for val in phone_number:
    #     chkPhonNum(val)