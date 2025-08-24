

<h1 align="center"> API para encontrar o próximo número primo </h1>

 ## Descrição do Projeto
 A API recebe um número do usuario e retorna o próximo número primo, a partir do número digitado.

## 🧠 Como funciona
  utiliza um algoritmo otimizado para verificar se um número é primo:
  - Recebe um número inteiro como parâmetro na URL
  - Valida se o parâmetro é um número inteiro positivo

   ## Aplica verificações matemáticas para determinar se é primo:
      -Números menores que 2 não são primos
      - O número 2 é primo
      - Números pares maiores que 2 não são primos
      - Verifica divisibilidade por números ímpares até a raiz quadrada do número

## 📁 Estrutura dos arquivos

| arquivo         | Descrição                                         |
|-----------------|---------------------------------------------------|
| `main.py`       | Ponto de entrada do sistema                       |
| `routes.py`     | Rota para a API (Fastapi)                         |
| `services`      | Local aonde a parte lógica do programa acontece   |
| `test.py`       | Realiza testes automatizados                      |



## 🤝 Contribuindo
  - Contribuições são sempre bem-vindas! Sinta-se à vontade para:
  
  - Fazer um fork do projeto
  
  - Criar uma branch para sua feature (git checkout -b feature/AmazingFeature)
  
  - Commit suas mudanças (git commit -m 'commit')
  
  - Push para a branch (git push origin ...)
  
  - Abrir um Pull Request


## 👨‍💻 Autor
Feito  por Bruno Leonel
