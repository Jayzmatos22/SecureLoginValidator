Este projeto é um script Python que simula um sistema completo de cadastro e login de usuário, executado inteiramente no terminal. Ele se destaca por suas funções de **validação robusta** que guiam o usuário a criar credenciais seguras (e-mail, senha e código de resgate) antes de permitir o acesso.

O script utiliza códigos de cores ANSI para uma interface de usuário mais amigável e informativa, destacando sucessos, erros e prompts.

## ✨ Principais Funcionalidades

* **Fluxo de Cadastro e Login:** Simula um fluxo completo onde o usuário primeiro cria suas credenciais e depois as utiliza para "acessar" o sistema.
* **Validação Múltipla de Erros:** Diferente de validadores simples, este script acumula *todos* os erros de uma entrada (ex: senha) e os exibe de uma só vez, permitindo que o usuário corrija tudo antes de tentar novamente.
* **Recuperação de Credenciais:** Implementa um sistema de "código de resgate" que permite ao usuário visualizar seu e-mail ou senha caso esqueça um deles durante o login.
* **Interface de Terminal Estilizada:** Usa cores e formatação de texto (negrito, sublinhado, fundo invertido) para melhorar a experiência do usuário.
* **Zero Dependências Externas:** O script utiliza apenas módulos nativos do Python (`time.sleep`).

---

## 📜 Critérios de Validação

O núcleo do projeto são suas três funções de validação, cada uma com regras específicas:

### 📧 Validação de E-mail (`validar_emaill`)

* Não pode estar vazio.
* Não pode conter espaços em branco.
* Deve ter um tamanho mínimo (padrão: 10 caracteres).
* Deve conter exatamente um símbolo `@`.
* Deve conter pelo menos um ponto (`.`).
* Não pode conter pontos consecutivos (`..`).
* A parte local (antes do `@`) não pode começar ou terminar com ponto.
* A parte do domínio (depois do `@`) não pode começar ou terminar com ponto.

### 🔑 Validação de Senha (`validar_senha`)

* Deve ter um tamanho mínimo (padrão: 6 caracteres).
* Deve conter pelo menos **uma letra maiúscula**.
* Deve conter pelo menos **uma letra minúscula**.
* Deve conter pelo menos **um dígito numérico**.
* Deve conter pelo menos **um símbolo especial** (ex: `@#$%&...`).

### 🔢 Validação de Código de Resgate (`validar_codigo`)

* Não pode estar vazio ou conter espaços.
* Deve ter um tamanho mínimo (padrão: 6 dígitos).
* Deve conter **apenas números**.

---

## 🚀 Como Usar

Como este é um script único e não possui dependências externas, você pode executá-lo diretamente.

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/Jayzmatos22/SecureLoginValidator.git](https://github.com/Jayzmatos22/SecureLoginValidator.git)
    ```

2.  Navegue até o diretório que contém o script:
    ```bash
    cd SecureLoginValidator/PyCharmMiscProject
    ```

3.  Execute o script Python:
    ```bash
    python SecureLoginValidator.py
    ```

---

## 📸 Exemplo de Uso (Fluxo)

O script guia o usuário por duas fases principais:

### 1. Área de Criação de Login

O usuário é solicitado a criar seu e-mail, senha e código de resgate.

**Exemplo de falha na validação da senha:**

```bash
----- ÁREA DE CRIAÇÃO DE LOGIN -----

 CRIE UM EMAIL: usuario.valido@email.com
EMAIL CRIADO COM SUCESSO!

 CRIE UMA SENHA: 123
---->VALIDANDO...
3 ERROS ENCONTRADOS NA SUA SENHA:

A SENHA DEVE CONTER AO MENOS 1 CARACTERE MAIÚSCULO!
A SENHA DEVE CONTER AO MENOS 6 CARACTERES!
A SENHA DEVE CONTER ALGUM SÍMBOLO ESPECIAL! @#$%^&*()-_=+[]{};:,.?/\|
### TENTE NOVAMENTE! ###

 CRIE UMA SENHA: SenhaForte123!
---->VALIDANDO...
SENHA CRIADA COM SUCESSO
