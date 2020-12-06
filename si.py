from flask import Flask, render_template, request, redirect, session, g, flash
from ping3 import ping

app = Flask(__name__)
app.secret_key = 'llll'

d = {'ПСЫ': ['Этот человек был хозяином пса Гарма, а позже завел и более крупное животное.*Фермер Джайлз.',
             'Этого внука в один из периодов жизни не признал бы и дедушка-водолаз, даже если он был.*Шарик (или Шариков).',
             'Ему еще в Валиноре был подарен пес, способный трижды заговорить.*Келегорм (пес Хуан или Ган).',
             'Их иногда называли "подземными жителями, умеющими покорять и убивать силой своего духа"*Голованы ("Жук в муравейнике").',
             'Так звали любимого пса Понтия Пилата.*Банга.'],
     'name': ['1', '2', '3', '4', '5'],
     'name2': ['6', '7', '8', '9', '10'],
     'name3': ['11', '12', '13', '14', '15'],
     'name4': ['16', '17', '18', '19', '20'],
     'name5': ['21', '22', '23', '24', '25']}

q = []
login = ''
ballov = ''
ping_time = ''
users = []
name = list(d.keys())
for i in name:
    q.extend(d[i])


@app.route('/', methods=['POST', 'GET'])
def user_login():
    global login
    if request.method == 'POST':
        login = request.form.get('login')
        users.append(login)
        g.user = login
        print(g.user)
        print(type(g.user))

        # password = request.form.get('password')
        # print(login, password)
        if login == 'admin':
            # return render_template('game.html', name=name,q=q[nomer])
            return redirect('/game')
    return render_template('login.html')


@app.route('/game', methods=['POST', 'GET'])
def game():
    global login
    flash('Invalid password provided', 'error')

    if request.method == 'POST':
        # todo Await ping

        # try:
        #     ping_time = int((ping('dim5x.pythonanywhere.com', unit='ms'))) or None
        # except:
        #     pass

        nomer, ves = map(int, list(request.form.items())[0])
        print('nomer=', nomer, 'ves=', ves)
        return render_template('game.html', name=name, login=login, ballov=ballov, q=q[nomer],
                               ping_time=ping_time or None, users=users)

    return render_template('game.html', name=name, login=login, ballov=ballov, users=users)


if __name__ == '__main__':
    app.run(debug=True)
