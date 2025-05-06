# Descrição
Sistema de gerenciamento de ramais

# Pré-requisitos
- Python 3.13+
- Windows 11+

# Instalação
- Clone o repositório
```bash
git clone https://github.com/gabriel-pagani/ramais-control.git
```
- Entre na pasta clonada
```powershell
cd ramais-control
```
- Crie um ambiente virtual
```powershell
python -m venv venv
```
- Ative o ambiente virtual
```powershell
venv\Scripts\activate
```
- Instale as dependências
```powershell
pip install -r requirements.txt
```

- Aplique as migrações
```powershell
python .\manage.py migrate
```
- Crie um super usuário
```powershell
python .\manage.py createsuperuser
```

# Estrutura do Projeto
```
projeto/
├── app/
├── project/
├── venv/
├── .gitignore
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt
```

# Mode de Uso
- Execulte o seguinte comando no terminal
```powershell
python manage.py runserver
```

# Licença 
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/gabriel-pagani/ramais-control/blob/main/LICENSE) para mais detalhes. A Licença MIT é uma licença de software livre que permite o uso, cópia, modificação e distribuição do código, desde que incluída a nota de direitos autorais e a permissão original.

# Contato 
Email - gabrielpaganidesouza@gmail.com