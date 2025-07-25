## Passo 1: Habilitar Copilot coding agent

No exercício [Introdução ao GitHub Copilot](/skills/getting-started-with-github-copilot), aprendemos como usar o Copilot em nosso editor de código para fazer grandes atualizações no site de Atividades Extracurriculares da Mergington. 🎻 ⚽️ 

Na verdade, o site se tornou uma ferramenta escolar regular agora. E, embora você goste dessa atenção, você acabou de perceber um problema! Você está prestes a entrar em sabático no próximo semestre!

Após alguma discussão com o diretor, ele aceitou que novas funcionalidades serão adiadas, mas... ele está preocupado. Eles precisam pelo menos ter _algo_ para lidar com mudanças simples enquanto você estiver fora.

Vamos preparar nossos professores para o sucesso inscrevendo o Copilot (em nossa escola) para lidar com updates enquanto estivermos fora.

<img width="600" alt="screenshot of Mergington High School WebApp" src="https://github.com/user-attachments/assets/6f5c59ab-398b-4fb0-8efd-0aa7b72fef97" />

### O Copilot agora é seu coding agent!

Em exercícios anteriores, usamos o Copilot **chat**, **edits** e modo **agent**. Embora esses tenham sido super úteis, o **Copilot coding agent** leva isso para o próximo nível operando inteiramente no GitHub. Nenhum editor de código necessário! 😎

| Feature           | Copilot no editor             | Copilot coding agent         |
| ----------------- | ----------------------------- | ---------------------------- |
| **Interface**     | Seu editor de código          | Issues e Pull Requests       |
| **Work Scope**    | Arquivos locais               | Repository                   |
| **Activation**    | Sugestões inline, chat        | Atribuição de issue          |
| **Customization** | Instruções customizadas       | Instruções customizadas      |
| **MCP Support**   | Sim                           | Sim                          |
| **Vibe Coding**   | 😎                            | 😎                           |

### Como funciona?

Da perspectiva do contributor, o fluxo é muito similar a um workflow normal.

1. Um contributor com **write access** seleciona uma issue e a atribui ao Copilot (em vez de a si mesmo).
2. O Copilot cria um branch e pull request.
3. O Copilot trabalha no branch em um workflow do Actions e fornece updates via aba de conversação do pull request.
4. Quando o Copilot termina a issue, é solicitado ao atribuidor que faça review.
5. O atribuidor submete um review, adiciona comentários ou aprova.
6. Se feedback for fornecido, o Copilot continua trabalhando para implementá-lo.
7. O solicitante repete os steps acima até ficar satisfeito e então faz merge.

```mermaid
flowchart LR

    contributor((Contributor))
    copilot((Copilot))
    reviewer((Reviewer))

    issue@{ shape: notch-rect, label: "Issue" }
    repo@{ shape: cyl, label: "Repository" }
    branch@{ shape: subproc, label: "Branch" }
    review@{ shape: diamond, label: "Review" }


    subgraph PR[Pull Request]
        direction TB
        branch
        review
        reviewer
    end


    %% Assign
    contributor gl1@-->|Selects| issue
    issue gl2@-->|Assigns to| copilot

    %% Work
    copilot pl1@-->|Creates| branch
    branch pl3@-->|Starts| review

    %% Review
    reviewer gl3@-->|Provides feedback| review
    review pl4@--> |Implements feedback| branch

    %% Approved
    review gl4@-->|Approves and merges| repo


    classDef users fill:#08872B,stroke:#5FED83,color:#fff
    classDef repo fill:#08872B,stroke:#5FED83,color:#fff
    classDef agent fill:#501DAF,stroke:#C06EFF,color:#fff
    classDef pr fill:#0969DA,stroke:#0349B4,color:#fff

    classDef green-line stroke:#08872B, stroke-width:4px;
    classDef purple-line stroke:#501DAF, stroke-width:4px;

    class contributor,reviewer users
    class copilot agent
    class repo repo

    class gl1,gl2,gl3,gl4 green-line
    class pl1,pl2,pl3,pl4 purple-line
```

### Isso é seguro?

Várias precauções de segurança foram implementadas para ajudar a reduzir preocupações. Aqui estão algumas limitações que você pode precisar considerar ao pedir ao Copilot para trabalhar em uma issue.

- O Copilot só pode fazer mudanças no branch que criou e resources fornecidos pelo repository.
- O Copilot tem [firewall configurável](https://docs.github.com/en/enterprise-cloud@latest/early-access/copilot/coding-agent/customizing-copilot-coding-agents-development-environment#customizing-or-disabling-the-agents-firewall) que restringe o acesso à internet.
- Apenas usuários com write access podem atribuir uma issue ao Copilot.
- Conteúdo oculto em issues (como código comentado) é ignorado.

> [!IMPORTANT]
> A lista completa de mitigations e configurações pode ser encontrada na documentação [Riscos & Mitigações](https://docs.github.com/en/enterprise-cloud@latest/early-access/copilot/coding-agent/using-copilot-coding-agent#copilot-coding-agent-risks-and-mitigations).

## ⌨️ Atividade: (opcional) Conheça nosso site de atividades extracurriculares

> [!NOTE]
> Abrir um ambiente de desenvolvimento e executar a aplicação não é necessário para completar este exercício. Você pode pular esta atividade se desejar.

<details>
<summary>Mostrar Passos</summary>

Em outros exercícios, temos desenvolvido o website de Atividades Extracurriculares. Você pode seguir estes passos para iniciar o ambiente de desenvolvimento e experimentá-lo.

1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Aguarde algum tempo para o ambiente ser preparado. Ele instalará automaticamente todos os requirements e services.

1. Valide se as extensions **GitHub Copilot** e **Python** estão instaladas e habilitadas.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. Tente executar a aplicação. Na sidebar esquerda, selecione a aba **Run and Debug** e então pressione o ícone **Start Debugging**.

   <details>
   <summary>📸 Mostrar screenshot</summary><br/>

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   </details>

   <details>
   <summary>🤷 Tendo problemas?</summary><br/>

   Se a área **Run and Debug** estiver vazia, tente recarregar o VS Code: Abra a command palette (`Ctrl`+`Shift`+`P`) e busque por `Developer: Reload Window`.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. Use a aba **Ports** para encontrar o endereço da webpage, abri-lo e verificar se está funcionando.

   <details>
   <summary>📸 Show screenshot</summary><br/>

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   </details>

</details>

## ⌨️ Atividade: Habilitar Copilot coding agent no seu repository

Antes de podermos começar a delegar requests dos professores para o Copilot, precisamos conceder acesso ao nosso repository.

1. No canto superior direito, clique no seu **ícone de usuário** e selecione **Settings**.

   <img width="300" src="https://github.com/user-attachments/assets/7f8c3602-6de2-4c75-8047-8f4853495f46"><br/>
   <img width="300" src="https://github.com/user-attachments/assets/2aedfd6e-8b9f-40bb-bdf9-c9fd597f94a4">

1. Na navegação esquerda, expanda a seção **Copilot** e selecione **Coding agent**.

   <img width="300" src="https://github.com/user-attachments/assets/79800990-6d5c-4055-acc9-b15734fe8b80">

1. Mude o campo **Repository access** para `Only selected repositories`.

   <img width="300" src="https://github.com/user-attachments/assets/7a665042-b064-4baf-a7e7-0dfc0261063e">

1. Clique no botão **Select repositories** e certifique-se de que este exercício esteja selecionado.

   <img width="300" src="https://github.com/user-attachments/assets/4bec16dc-7b52-4e95-b554-47252b622adb">

## ⌨️ Atividade: Atribuir uma issue ao Copilot

Há várias issues importantes para resolver antes de partirmos, mas vamos fazer um teste primeiro com uma das opções simples. Isso nos permitirá ver como as interações e colaboração funcionam, para que possamos atualizar nossos docs para orientar os outros professores. A maioria não sabe como usar um editor de código tradicional!

> [!TIP]
> Tente deixar claro o objetivo e critérios de aceitação de uma issue. Além disso, dividir tarefas grandes em menores oferece mais oportunidade para feedback!

1. Retorne ao seu [repository do exercício](<(https://github.com/{{full_repo_name}})>).

1. Na navegação superior, selecione a aba **Issues**.

1. Acima da lista, no canto superior direito, clique no botão **New Issue**.

1. Defina o **Title** como:

   ```md
   Missing Activity: Manga Maniacs
   ```

   Digite o texto abaixo como descrição, e clique no botão **Create**.

   ```md
   O clube de mangá foi anunciado recentemente e naturalmente está faltando no website. Por favor, adicione-o.

   Aqui estão os detalhes:

   Descrição: Explore as histórias fantásticas dos personagens mais interessantes dos Mangás japoneses (graphic novels).

   Horário: Terças às 19h
   Lotação máxima: 15 pessoas
   ```

1. No canto superior direito, clique na área **Assignees** e selecione **Copilot**.

   <img width="350" src="https://github.com/user-attachments/assets/444f9432-17c3-4466-bb8e-aa4e44238130" />

1. Na parte inferior, clique no botão **Create**. Após um momento, você notará:

   - A issue terá uma reaction `👀` para mostrar que o Copilot está lendo a issue.
   - O log de atividade mostra que você atribuiu a issue ao Copilot.
   - O log da issue inclui um pull request vinculado.

   <img width="350" src="https://github.com/user-attachments/assets/40245540-e717-43b3-b2be-90f25cc494d0" />

1. Com a issue atribuída, a Mona deve estar ocupada verificando seu trabalho. Dê a ela um momento para compartilhar os próximos steps.

<details>
   <summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que atribuiu a issue correta. Se você praticar em outras issues, elas serão ignoradas.

</details>
