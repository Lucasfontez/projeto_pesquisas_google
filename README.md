# Projeto: Buscas Automáticas no Google com Python

Esse é um projeto simples em Python que criei com a ideia de automatizar buscas no Google.

A ideia é bem direta:  
Eu escrevo temas que quero pesquisar num arquivo `.txt` (um por linha), o script faz a busca pra mim e salva os principais links encontrados. Se eu rodar de novo depois, ele compara com a busca anterior e me mostra o que mudou. Útil pra acompanhar novidades sobre um assunto sem precisar procurar toda hora.

---

## Como usar

1. **Clone o repositório**  
git clone https://github.com/Lucasfontez/projeto_pesquisas_google.git

2. **Entre na pasta do projeto**  
cd projeto_pesquisas_google

3. **Instale as dependências**  
pip install -r requirements.txt

4. **Crie um arquivo `.txt` com os termos de busca** (ex: `termos.txt`)  
Cada linha deve conter um tema diferente.

5. **Execute o script**  
python core.py termos.txt

Você também pode definir quantos links deseja por tema:  
python core.py termos.txt 20

---

Se quiser testar ou contribuir, fica à vontade.  
É um projeto simples, mais voltado a prática do código junto a seu aperfeiçoamento.
