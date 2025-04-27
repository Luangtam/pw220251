from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial com o formulário
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coletar os dados enviados no formulário
        nome = request.form['nome']
        formacao = request.form['formacao']
        curso = request.form['curso']
        instituicao = request.form['instituicao']
        ano_formacao = request.form['ano_formacao']
        experiencia = request.form['experiencia']
        empresa = request.form['empresa']
        ano_experiencia = request.form['ano_experiencia']
        
        # Passar os dados para a página de resultado
        return render_template('resultado.html', 
                               nome=nome, 
                               formacao=formacao, 
                               curso=curso, 
                               instituicao=instituicao, 
                               ano_formacao=ano_formacao, 
                               experiencia=experiencia, 
                               empresa=empresa, 
                               ano_experiencia=ano_experiencia)
    
    # Se for um GET, apenas renderiza a página de entrada
    return render_template('index.html')

# Rota para a página do autor
@app.route('/autor')
def autor():
    return '''
        <h1>Autor: Seu Nome</h1>
        <p>Formações acadêmicas: Curso, Instituição, Ano</p>
        <p>Experiências profissionais: Função, Empresa, Ano</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
