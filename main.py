import requests
import time
from bs4 import BeautifulSoup
from rich.console import Console 

console = Console()

# pasta = "/paginas_baixadas/"

pag = ""

console.print("[bold]Html Downloader\n")

downloads_feitos = 0

print(f"Paginas baixadas: {downloads_feitos}")

while True:
    
    link = input("Cole um link: ")
    resultado = requests.get(link)
    soup = BeautifulSoup(resultado.text, "html.parser")
    
    if resultado.status_code == 200:
        console.print("Iniciando download...\n")
        pag = resultado.text
        nome = input("Digite um nome para salvar: ")
      
        nome = input("Digite um nome para salvar: ")
        doc = open(nome + ".html", "w")
        doc.write(pag)
        doc.close()
        console.print("[green] >>> Download concluído. \n")
        
        downloads_feitos = downloads_feitos + 1
        print(f"Paginas baixadas: {downloads_feitos}")
        
    else:
        console.print("[red] >>> Acesso 
negado.")
