# PetData AI 🐾

Sistema inteligente para **gestão e análise de dados de adoção de animais**, desenvolvido com **Django**, **TDD** e foco em **Ciência de Dados aplicada ao impacto social**.

Este projeto faz parte de um **TCC em Ciência de Dados / Engenharia de Software**, com objetivo de demonstrar domínio técnico, boas práticas de desenvolvimento e base sólida para análises preditivas futuras.

---

## 🎯 Objetivo do Projeto

- Centralizar dados de **abrigos, pets, adotantes e adoções**
- Garantir **integridade das regras de negócio**
- Servir como base para **análises e modelos de Machine Learning**
- Demonstrar boas práticas profissionais (TDD, arquitetura por domínio, versionamento)

---

## 🧱 Arquitetura do Projeto

O projeto segue uma **arquitetura modular por domínio**, separando responsabilidades em apps independentes:

```
apps/
├── adopters/   # Adotantes
├── adoptions/  # Adoções
├── pets/       # Animais
├── shelters/   # Abrigos
```

Cada app possui:

- `models.py`
- `tests/`
- migrations isoladas
- regras de negócio próprias

---

## 🧪 Testes (TDD)

- Framework: **pytest + pytest-django**
- Testes focados em **regras de negócio**
- Cobertura de:
  - Criação de entidades
  - Relacionamentos
  - Restrições de domínio (ex: pet não pode ser adotado duas vezes)

Executar os testes:

```bash
pytest
```

---

## 🗄️ Banco de Dados

- **PostgreSQL**
- Migrations versionadas
- Integridade garantida via constraints e validações de modelo

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- Django 6
- PostgreSQL
- Pytest
- Pytest-Django
- Git & GitHub

---

## 🚀 Status do Projeto

✔ Models implementados
✔ Regras de negócio validadas
✔ Testes passando (TDD)
✔ Estrutura pronta para API REST
⏳ Próximo passo: Services e API

---

## 👨‍💻 Autor

**Jadson Silva**
Estudante de Ciência de Dados e Engenharia de Software
Projeto desenvolvido para fins acadêmicos e profissionais.
