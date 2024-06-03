from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas
tarefas = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Adiciona uma nova tarefa
        nova_tarefa = request.form.get('tarefa')
        if nova_tarefa:
            tarefas.append(nova_tarefa)
        return redirect(url_for('index'))

    return render_template('index.html', tarefas=tarefas)


@app.route('/delete/<int:tarefa_id>')
def delete(tarefa_id):
    # Remove a tarefa pelo índice
    if 0 <= tarefa_id < len(tarefas):
        tarefas.pop(tarefa_id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
