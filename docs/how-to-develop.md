# Guia de Desenvolvimento

## Configuração Inicial

Este projeto é melhor desenvolvido usando GitHub Codespaces, que fornece um ambiente de desenvolvimento consistente com todas as ferramentas necessárias pré-configuradas.

### Configurando seu ambiente de desenvolvimento

1. Abra o repository em um codespace
2. Aguarde o container terminar de construir e instalar as dependencies
3. Instale as dependencies do Python executando:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Dependencies

O projeto requer os seguintes packages do Python:

- FastAPI - Modern web framework para construir APIs
- Uvicorn - ASGI server implementation para executar a aplicação FastAPI

Essas dependencies serão instaladas quando você executar `pip install -r requirements.txt`

## Debugging

### Executando o website localmente

1. Na view Run and Debug do VS Code (Ctrl+Shift+D), selecione "Launch Mergington WebApp" no dropdown de configuração de launch
2. Pressione F5 ou clique no botão verde play para iniciar o debugging
3. O website estará disponível em `http://localhost:8000`
4. A documentação da API estará disponível em `http://localhost:8000/docs`

### Dicas de debugging

- O feature auto-reload do FastAPI irá automaticamente reiniciar o server quando você fizer mudanças no código
- Use a documentação interativa da API em `/docs` para testar seus endpoints

## Começando

1. Instale as dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

2. Execute a aplicação:

   ```bash
   python app.py
   ```

3. Abra seu browser e vá para:
   - Documentação da API: http://localhost:8000/docs
   - Documentação alternativa: http://localhost:8000/redoc

## Uso

### API Endpoints

| Method | Endpoint                                                          | Descrição                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obter todas as activities com seus detalhes e contagem atual de participantes |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscrever-se em uma activity                                             |

> [!IMPORTANT]
> Todos os dados são armazenados na memória, o que significa que os dados serão resetados quando o server reiniciar.
