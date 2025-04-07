Esse é um projeto simples em Python que criei com a ideia de automatizar buscas no Google.

A ideia é bem direta:
Eu escrevo temas que quero pesquisar num arquivo .txt (um por linha), o script faz a busca pra mim e salva os principais links encontrados. Se eu rodar de novo depois, ele compara com a busca anterior e me mostra o que mudou. Útil pra acompanhar novidades sobre um assunto sem precisar procurar toda hora.

Como usar:

-Clone o repositório:
git clone https://github.com/Lucasfontez/projeto_pesquisas_google.git

-Entre na pasta do projeto:
cd projeto_pesquisas_google

-Instale as dependências:
pip install -r requirements.txt

-Crie um arquivo .txt com os termos de busca (ex: termos.txt), cada linha com um tema.

-Execute o script:
python core.py termos.txt

Você também pode passar um terceiro argumento pra definir quantos links por busca:
python core.py termos.txt 20

Estrutura do projeto:

projeto_pesquisas_google

core.py               >   Arquivo principal do projeto

termos.txt            >   Arquivo com os temas a serem pesquisados

requirements.txt      >   Dependências do projeto

outputs/              >   Aqui ficam os arquivos gerados com os resultados



Se quiser testar ou contribuir, fica à vontade. Projeto simples, mas funcional e com potencial pra crescer.
