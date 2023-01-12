from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/entrar/')
def admin_index():
  return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    usuario = request.form['c_usuario']
    senha = request.form['c_senha']
    if usuario == "robson" and senha == 123:
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      #return redirect(url_for('login'))
      return redirect(url_for('admin', nome=usuario, senha=senha))
  else:
    usuario = request.args.get('c_usuario')
    senha = request.args.get('c_senha')

@app.route('/admin/<nome>/<senha>')
def admin(nome, senha):
  frase = "<b>Bem-vindo!!! </b>" + "Sua senha é:<i> " + senha + "</i>"
  return frase
  
if __name__ == '__main__':
  app.run('0.0.0.0')