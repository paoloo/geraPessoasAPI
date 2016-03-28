# geraPessoasAPI

### API geradora de dados pessoas ficticios randomicos para cadastros e testes

Trata-se de uma API para gerar dados pessoais falsos porem consistentes, para uso
em cadastros ou gerar dados para popular um banco-teste, conforme um algoritmo
descrito e implementado no meu blog em 2011
( encontrado em: http://paoloo.wordpress.com/2011/01/10/gerador-de-dados-pessoais/ ).
O valor retornado é um JSON contendo um array de identidades falsas.

### Requisitos
- python 2.7
- bottle ( bottlepy.org - mas ja vai embarcado)


### Uso
- diretamente no terminal:
```
python web.py
```
- ou, em modo *deamon*:
```
nohup python web.py &
```

### Requisição
```
http://localhost:8080/pessoa
```
para gerar uma pessoa ou
```
http://localhost:8080/pessoas/n
```
para gerar **n** pessoas.


### Exemplo da saida JSON
```
{
	"pessoas": [{
		"nome": "BRUNO GABRIEL FREITAS JUSTINO",
		"sexo": "M",
		"cartao de credito": {
			"numero": "5701.7724.1266.7391"
			"cvv": "185",
			"validade": "10/2024",
		},
		"mae": "SAMANTA PINTO COELHO LINHARES",
		"senha": "HYOReAVrUo",
		"documentos": {
			"rg": "995014280 SSP MG",
			"cpf": "691.525.197-91"
		},
		"sangue": "B+",
		"emprego": "cozinheiro",
		"nascimento": "03/08/1939",
		"telefone": "(35)1594-9692",
		"endereco": {
			"cidade": "P. DE CALDAS",
			"uf": "MG",
			"logradouro": "TRAVESSA MAJOR CARLOS ANTUNES, 506",
			"cep": "99.557-668"
		},
		"email": "BRUNO.GFJ@gmail.com",
		"peso": "79.10 kg",
		"altura": "1.83 m"
	}]
}
```

### be happy
