## Passo 3: Preparando o ambiente do Copilot

Vamos adicionar algumas informações sobre a escola, roles a assumir, e tarefas típicas que os professores solicitam e um ambiente de desenvolvimento pré-configurado para torná-lo mais rápido e confiável (para que Jessica do IT não pergunte sobre o aumento no uso de minutos do Actions).

- **copilot instructions** - Fornecer contexto específico do projeto para o copilot antes de considerar a issue.
  - Fornecer considerações de negócio para desenvolver o projeto.
  - Fornecer roles para guiar o Copilot.
  - Fornecer commands úteis para tarefas comuns.
- **copilot setup steps** - Customizar o ambiente de desenvolvimento antecipadamente para tornar as sessions mais rápidas.
  - Pré-instalar ferramentas úteis para o Copilot.
  - Reduzir erros do Copilot instalando versões incorretas.
- **environment** - Usar environments do repository para configurações.
  - Fornecer variáveis para ajustar deployments para diferentes environments.
  - Fornecer secrets para acessar resources adicionais.

> [!TIP]
> Você também pode [habilitar um servidor Model Context Protocol (MCP)](https://docs.github.com/en/enterprise-cloud@latest/early-access/copilot/coding-agent/extending-copilot-coding-agent-with-model-context-protocol) para o Copilot fornecer ainda mais funcionalidade!

### ⌨️ Atividade: Criar instruções para guiar o Copilot

1. Na navegação superior, selecione a aba **Code**.

1. Crie um novo branch com o nome `prepare-environment`.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/c48deded-4214-4edd-9a50-d1368bfb12e8" />

1. Navegue e abra o arquivo `.github/copilot-instructions.md` para edição.

1. Substitua o texto placeholder por um link para o development guide.

   ```md
   ## Ambiente de Desenvolvimento

   Para instruções detalhadas de setup e desenvolvimento, por favor consulte nosso [Guia de Desenvolvimento](../docs/how-to-develop.md).
   ```

1. Adicione algumas informações adicionais sobre a escola e professores para ajudar o Copilot a interagir mais naturalmente.

   ```md
   ### Interação do usuário

   Considere o seguinte ao se comunicar com o staff.

   - O staff não é técnico. Explique em termos simples o máximo possível e evite jargão de software.
   - Qualquer código novo deve ser fácil de manter e entender, sem experiência significativa em programação.

   ## Arquitetura do programa

   - Os usuários do website são os estudantes e professores. Certifique-se de que a experiência do usuário seja simples.
   - Não faça apps ou services adicionais.
   - Não faça ferramentas de command line.
   - Não crie uma aplicação de arquivo único longo. Sempre use uma estrutura de diretório fácil de entender.
   - Use apenas HTML, CSS, Javascript e Python. Nenhuma outra linguagem.
   ```

   > 💡 Dica: Você pode adicionar mais detalhes. Confira o arquivo `copilot-instructions-ext.md` para ideias.

1. Quando terminar, **faça commit de suas mudanças** para o branch `prepare-environment`.

### ⌨️ Atividade: Preparar o ambiente de coding para o Copilot

Customizar o ambiente de desenvolvimento do Copilot e ajustar [permissions](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token) é feito com um [GitHub Actions](https://github.com/features/actions) workflow único. Para todas as opções de configuração, veja a documentação [pré-instalação de dependencies para o Copilot](https://docs.github.com/en/enterprise-cloud@latest/early-access/copilot/coding-agent/customizing-copilot-coding-agents-development-environment#pre-installing-tools-or-dependencies-in-copilots-environment).

1. Certifique-se de que você ainda está no branch `prepare-environment`.

1. Navegue para o diretório `.github/workflows/`.

1. No canto superior direito, clique no botão **Add file** e selecione **Create new file**.

   <img width="250" alt="image" src="https://github.com/user-attachments/assets/c135dd3f-72bd-4d2b-b21f-9c4968a06f5f" />

1. Defina o nome do arquivo como `copilot-setup-steps.yml`.

   <img width="650" alt="image" src="https://github.com/user-attachments/assets/ac615290-1045-45a5-8201-637721ef6fd2" />

1. Cole a seguinte configuração de workflow, que pré-instalará as dependencies para o backend Python do website.

   ```yml
   name: "Copilot Setup Steps"

   on: workflow_dispatch
   jobs:
     # Este é o nome do job obrigatório. Se for diferente, o Copilot irá ignorá-lo.
     copilot-setup-steps:
       runs-on: ubuntu-latest

       # Conceder ao Copilot acesso antecipado para ler o conteúdo do repository.
       permissions:
         contents: read

       steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: "3.x"
             cache: "pip"

         - name: Install Python dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r src/requirements.txt
   ```

   > 🪧 **Nota:** O Copilot irá automaticamente recuperar o conteúdo do repository mais tarde. Este workflow fornece acesso antecipado durante o setup para instalar as dependencies.

      > 🪧 **Nota:** O Copilot irá automaticamente identificar e instalar dependencies faltantes. Fazer isso agora economiza tempo do Copilot e garante a configuração adequada do ambiente.

1. No canto superior direito, clique no botão **Commit changes...** e faça commit de suas mudanças para o branch `prepare-environment`.

1. Crie um **pull request**, mas **NÃO** faça merge ainda. A Mona irá verificar seus arquivos para confirmar se estão corretos.

1. Depois que a Mona compartilhar os próximos passos, você pode fazer merge do pull request.

> 🙋 **Pergunta:** Como foi o processo manual comparado a deixar o Copilot fazer a maior parte do trabalho? 🤔


<details>
<summary>🤷 Tendo problemas?</summary><br/>

Se você acidentalmente fez merge do pull request antes da Mona compartilhar feedback sobre erros, tudo bem. Apenas recrie o branch e tente novamente com um novo pull request.

</details>
