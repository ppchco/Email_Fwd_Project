# Estrutura do Projeto (Project Structure)
# 📁 fwd_email_project
# ├── 📁 src
# │   ├── __init__.py
# │   └── fwd_email.py
# ├── 📁 tests
# │   └── test_fwd_email.py
# ├── README.md
# ├── requirements.txt
# ├── .gitignore
# └── config.env

# src/__init__.py
# Declara a estrutura do pacote para processamento de emails
from .fwd_email import main, forward_email, decode_email_body

__all__ = ["main", "forward_email", "decode_email_body"]