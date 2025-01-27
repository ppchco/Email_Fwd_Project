# Meu Projeto de Encaminhamento de Emails

Este projeto permite a automação do encaminhamento de emails com base em regras específicas, como destinatários e análise de corpo de mensagem. Pode ser configurado para trabalhar com servidores de email via IMAP e SMTP.

---

## Estrutura do Projeto

```
📁 fwd_email_proj
├── 📁 src
│   ├── __init__.py           # Declaração do pacote
│   └── fwd_email.py   # Lógica principal para processamento de emails
├── 📁 tests
│   └── test_email_processing.py # Testes unitários do projeto
├── README.md                 # Documentação do projeto
├── requirements.txt          # Dependências do Python
├── .gitignore                # Arquivos ignorados pelo Git
└── config.env                # Configuração de ambiente (não comitada ao Git)
```

---

## Funcionalidades

1. **Leitura de Emails:**
   - Conecta à caixa de entrada e busca emails não lidos.

2. **Encaminhamento Automático:**
   - Reenvia emails para destinatários predefinidos com base em regras personalizadas.

3. **Decodificação de Conteúdo:**
   - Processa o corpo e os anexos de emails.

---

## Pré-Requisitos

- **Python 3.8+**
- **Serviços de Email:** Servidor IMAP/SMTP configurado.
- **Pacotes Python:** Listados no `requirements.txt`.

### Instalação das Dependências

Instale as bibliotecas necessárias com:

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `config.env` com as seguintes variáveis:

```env
EMAIL_USERNAME=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@gmail.com
SMTP_PASSWORD=sua_senha
```

Certifique-se de que o arquivo `config.env` não seja adicionado ao controle de versão. Ele estará listado no `.gitignore`.

---

## Uso

Execute o script principal para processar emails:

```bash
python src/email_processing.py
```

### Testes

Execute os testes unitários com:

```bash
python -m unittest discover tests
```

---

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

**Autor:**
https://github.com/ppchco.