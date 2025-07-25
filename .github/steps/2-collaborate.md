## Passo 2: Colaborar com o Copilot

Quando o Copilot cria um pull request no qual você encontrará:

- **Pull Request Description** - O Copilot manterá uma visão geral concisa de seu objetivo e implementação.
- **Timeline** - O Copilot fornecerá notas de alto nível sobre iniciar working sessions e commits.
- **Session History** - Um log detalhado dos steps que o Copilot seguiu para implementar a issue.

Você pode fornecer feedback ao Copilot da mesma forma que faria com um colega. Essas ações fazem o Copilot iniciar outra working session.

- **Comments** - Adicione um comment na conversação do pull request.
- **Reviews** - Combine múltiplos comments em um pull request review.
- **@ mentions** - Você pode marcar o Copilot em um comment assim como um colega de trabalho.

#### Considerações Importantes

- O trabalho do Copilot é feito em um branch com a convenção `copilot/*` e não tem acesso a outros branches.
- O Copilot não pode disparar workflows do Actions.
  - Workflows disparados em pull requests requerem aprovação humana antes de executar.
- Rulesets e proteções similares ainda são aplicados.

> [!TIP]
> Todo trabalho criado pelo Copilot é committed com o assignee como co-contributor (mantendo seu contribution graph seguro). 💕

### ⌨️ Atividade: Ver o progresso do Copilot

1. Na issue, clique no link de referência para o pull request. Alternativamente, use a aba **Pull Requests** na navegação superior.

1. Assista em tempo real conforme o Copilot atualiza a descrição do pull request. Ele progredirá através de 3 fases:

   <details>
      <summary>1. Ao iniciar, o Copilot fornece uma cópia inicial da issue. <b>[mostrar imagem]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/967dbea0-01c2-4531-9bce-5a055d3dad25" />
   </details>

   <details>
      <summary>2. Após o planejamento, o Copilot fornece um conjunto de action items. <b>[mostrar imagem]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/acadb796-6545-4b6d-b2b3-9a00ea1744a2" />
   </details>

   <details>
      <summary>3. Após terminar, o Copilot fornece um summary. <b>[mostrar imagem]</b></summary>
      <img width="500" alt="image" src="https://github.com/user-attachments/assets/61204574-0262-4c2f-af4b-09b284f31b90" />
   </details>

1. Role ligeiramente para baixo para ver a timeline e notas de alto nível fornecidas pelo Copilot. Clique no botão **View session**.

   <img width="500" src="https://github.com/user-attachments/assets/088260e6-bae0-40af-8186-864eb3e7b8a2" />

1. A nova página mostra um journal do trabalho do Copilot. A navegação esquerda é uma lista de cada working session.

   <img width="500" src="https://github.com/user-attachments/assets/2c80fa91-1123-4813-a801-42af368240b9" />

1. Se necessário, aguarde o Copilot terminar de trabalhar nas mudanças.

> [!TIP]
> Você pode usar o dropdown **edited** para ver o histórico de mudanças da descrição do pull request.
>
> <details>
> <summary>Mostrar imagem</summary>
> <img width="500" alt="image" src="https://github.com/user-attachments/assets/cb88a67c-e42f-463c-88cd-b23a391b28a0" />
> </details>

### ⌨️ Atividade: Fornecer feedback ao Copilot

1. De volta no pull request, clique no botão **Add your review**.

   <img width="350" src="https://github.com/user-attachments/assets/d71847b9-573b-451e-9c85-946a6988e3f0" />

1. Encontre a nova entrada criada pelo Copilot. Passe o mouse sobre uma linha para mostrar o sinal de mais. **Clique** para abrir a dialog box de adicionar comment.

   <img width="350" src="https://github.com/user-attachments/assets/fd1375a4-fbdf-453e-a457-7bcb1fbbea23" />

1. Lendo a descrição, achamos que deveria ser mais interessante para combinar com o espírito do Manga. Vamos pedir ao Copilot para corrigir isso. Digite o seguinte texto e clique em **Start a review**.

   ```md
   Por favor, mude esta descrição para ser inspirada pelo Manga japonês.
   Precisa de mais personalidade para atrair estudantes.
   ```

   <img width="350" src="https://github.com/user-attachments/assets/f37da948-2062-4f46-ba75-bcff538800e4" />

1. No topo da lista de mudanças, clique no botão **Finish your review** e selecione **Submit Review**.

1. Após um momento, o Copilot adicionará uma nova entrada de session e indicará progresso na timeline.

1. Aguarde o Copilot terminar de trabalhar na mudança e então clique no botão **View changes** para ver a descrição da atividade atualizada.

   <img width="350" src="https://github.com/user-attachments/assets/a5ccd7b5-4df8-406a-b3a8-80328ba210e5" />

1. Ative os pull requests clicando no botão **Ready to Review** e então clique no botão **Merge**.

1. Com nosso review submetido e o pull request merged, a Mona deve estar verificando nosso trabalho. Dê a ela um momento para responder com a próxima lição.

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que commitou as mudanças no diretório `src/static/` para o branch `accelerate-with-copilot` e fez push/sincronizou com o GitHub.
- Se a Mona encontrou um erro, simplesmente faça uma correção e faça push de suas mudanças novamente. A Mona verificará seu trabalho quantas vezes for necessário.

</details>
