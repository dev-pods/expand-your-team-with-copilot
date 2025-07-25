### Visão Geral da Escola

- O nome da escola é "Mergington High School"
- A escola é uma high school pública em Mergington, Florida.
- O lema da escola é "Branch out and grow".
- Atende da 9ª à 12ª série e normalmente tem de 100 a 150 estudantes por série.

- O ano letivo começa em agosto e termina em maio.
- Há 3 trimestres por ano.
- Há um 4º ciclo de verão, mas é opcional.

Abaixo está uma lista de funções comuns e tarefas com as quais eles podem querer ajuda.
Se um usuário especificar sua função, você pode usar essa informação para fornecer sugestões mais direcionadas ou oferecer maneiras de ajudá-los.

## Ambiente de Desenvolvimento

Para instruções detalhadas de setup e desenvolvimento, por favor consulte nosso [Guia de Desenvolvimento](../docs/how-to-develop.md).

### Interação com o Usuário

Considere o seguinte ao se comunicar com o staff.

- O staff não é técnico. Explique em termos simples o máximo possível e evite jargão de software.
- Qualquer código novo deve ser fácil de manter e entender, sem experiência significativa em programação.

## Arquitetura do Programa

- Os usuários do website são os estudantes e professores. Certifique-se de que a experiência do usuário seja simples.
- Não faça apps ou services adicionais.
- Não faça ferramentas de command line.
- Não crie uma aplicação de arquivo único longo. Sempre use uma estrutura de diretório fácil de entender.
- Use apenas HTML, CSS, Javascript e Python. Nenhuma outra linguagem.

### Documentação

- Sempre atualize o arquivo README para explicar como usar o programa. Assuma que o usuário esquecerá rapidamente, então uma boa documentação é importante.
- Uma vez que o readme ficar muito longo, comece a organizá-lo em um diretório docs.

### Considerações de Qualidade

- Se as tarefas envolvem notas, pontuações ou outros dados numéricos, isole essas functions e certifique-se de que estejam corretas com unit tests.

### Considerações de Segurança

- Informações pessoais podem ser processadas, então privacidade e segurança são importantes.
- Não forneça exemplos que encorajem o usuário a hardcode secrets, passwords ou outras informações sensíveis.
- Se credentials ou outras informações sensíveis forem necessárias, adicione features ao programa para solicitá-las, armazená-las localmente e fazer logout. Por exemplo, uma dialog box de login.
