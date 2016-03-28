# -*- coding: utf-8 -*-

from random import randint, uniform
from string import lower, upper
from math import sqrt

alfanum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
email = ['yahoo.com.br', 'hotmail.com', 'gmail.com', 'bol.com.br', 'terra.com.br', 'globo.com', 'ig.com.br']
emailsep = ['.', '', '_', '-']
empregos = [['professor', 'motorista', 'gari', 'mecanico', 'engenheiro', 'advogado', 'desempregado', 'medico', 'empresario', 'enfermeiro', 'vendedor', 'bancario', 'estudante', 'taxista', 'gerente de vendas', 'cozinheiro', 'gogo-boy', 'programador', 'politico', 'animador', 'digitador'],['professora', 'motorista', 'gari', 'domestica', 'engenheira', 'advogada', 'desempregada', 'medica', 'empresaria', 'enfermeira', 'vendedora', 'bancaria', 'estudante', 'taxista', 'gerente de vendas', 'cozinheira', 'jornalista', 'prostituta', 'politica', 'animadora', 'digitadora']]
nomes = [['JOAO', 'LUCAS', 'GABRIEL', 'MATHEUS', 'PEDRO', 'LUIZ', 'JOSE', 'GUILHERME', 'CARLOS', 'RAFAEL', 'FELIPE', 'BRUNO', 'GUSTAVO', 'PAULO', 'MARCOS', 'LEONARDO', 'VINICIUS', 'DANIEL', 'LUIS', 'THIAGO', 'MATIAS', 'RICARDO', 'ALFREDO', 'ALESSANDRO'],['MARIA', 'ANA', 'JULIA', 'LETICIA', 'LARISSA', 'BEATRIZ', 'JESSICA', 'BRUNA', 'AMANDA', 'GABRIELA', 'LUANA', 'SAMANTA', 'MAYARA', 'SAMARA', 'JAQUELINE', 'RACHEL', 'RAQUEL', 'LUCIA', 'DENISE', 'DANIELA', 'ERICA']]
sobrenomes = ['ABREU', 'ALVES', 'ALBINO', 'ALMEIDA', 'AMARAL', 'ARAUJO', 'ANDRADE', 'ANTUNES', 'AZEVEDO', 'ASSIS', 'BARRETO', 'BARROS', 'BAHR', 'BATISTA', 'BENTO', 'BRASIL', 'BRAGA', 'BRITO', 'CAMARGO', 'CAMPOS', 'CARDOSO', 'CANDIDO', 'CARVALHO', 'CASTRO', 'CHAGAS', 'COELHO', 'CORREIA', 'DUTRA', 'FAGUNDES', 'FERNANDES', 'FRAGA', 'FRANCA', 'FREITAS', 'JUSTINO', 'LEAL', 'LEITE', 'LIMA', 'LINHARES', 'LOPES', 'MACHADO', 'MACEDO', 'MACIEL', 'MARTINS', 'MATOS', 'MARQUES', 'MEDEIROS', 'MIRANDA', 'MORAES', 'MONTEIRO', 'NASCIMENTO', 'NEVES', 'OLIVEIRA', 'ONOFRE', 'PACHECO', 'PADILHA', 'PAIVA', 'PEREIRA', 'PESSOA', 'PINHO', 'PINTO', 'PIRES', 'PRADO', 'RABELO', 'RAMOS', 'RIBEIRO', 'ROCHA', 'RODRIGUES', 'ROSA', 'SALES', 'SABINO', 'SANTOS', 'SILVA', 'SILVEIRA', 'SOARES', 'TEIXEIRA', 'VARGAS', 'VASCONCELOS', 'VIEIRA', 'XAVIER']
sexo = ['M', 'F']
sangueT = ['A', 'B', 'AB', 'O']
sangueF = ['+', '-']
logradouro = ['RUA', 'AVENIDA', 'TRAVESSA', 'ALAMEDA', 'PRACA']
ruas = ['PROFESSOR', 'DOUTOR', 'MAJOR', 'TIPOGRAFO', '', 'DESEMBARGADOR', 'SARGENTO']
slDDD = ['68', '82', '96', '92', '97', '71', '73', '74', '75', '77', '85', '88', '61', '27', '28', '62', '64', '98', '99', '65', '66', '67', '31', '32', '33', '34', '35', '37', '38', '91', '93', '94', '83', '41', '42', '43', '44', '45', '46', '81', '87', '86', '89', '21', '22', '24', '84', '51', '53', '54', '55', '69', '95', '47', '48', '49', '11', '12', '13', '14', '15', '16', '17', '18', '19', '79', '63']
lsDDD = {
  '68': ['AC', 'Rio Branco'],
  '82': ['AL', 'Maceio'],
  '96': ['AP', 'Macapa'],
  '92': ['AM', 'Manaus'],
  '97': ['AM', 'Interior'],
  '71': ['BA', 'Salvador'],
  '73': ['BA', 'Ilheus'],
  '74': ['BA', 'Juazeiro'],
  '75': ['BA', 'Feira de Santana'],
  '77': ['BA', 'Vitoria da Conquista'],
  '85': ['CE', 'Fortaleza'],
  '88': ['CE', 'Interior'],
  '61': ['DF', 'Brasilia'],
  '27': ['ES', 'Vitoria'],
  '28': ['ES', 'Interior'],
  '62': ['GO', 'Goiania'],
  '64': ['GO', 'Interior'],
  '98': ['MA', 'Sao Luis'],
  '99': ['MA', 'Interior'],
  '65': ['MT', 'Cuiaba'],
  '66': ['MT', 'Interior'],
  '67': ['MA', 'Campo Grande'],
  '31': ['MG', 'Belo Horizonte'],
  '32': ['MG', 'Juiz de Fora'],
  '33': ['MG', 'Gov Valadares'],
  '34': ['MG', 'Uberlandia'],
  '35': ['MG', 'P. de Caldas'],
  '37': ['MG', 'Divinopolis'],
  '38': ['MG', 'Montes Claros'],
  '91': ['PA', 'Belem'],
  '93': ['PA', 'Santarem'],
  '94': ['PA', 'Maraba'],
  '83': ['PB', 'Joao Pessoa'],
  '41': ['PR', 'Curitiba'],
  '42': ['PR', 'Ponta Grossa'],
  '43': ['PR', 'Londrina'],
  '44': ['PR', 'Maringa'],
  '45': ['PR', 'Foz do Iguacu'],
  '46': ['PR', 'Fco Beltrao'],
  '81': ['PE', 'Recife'],
  '87': ['PE', 'Interior'],
  '86': ['PI', 'Teresina'],
  '89': ['PI', 'Interior'],
  '21': ['RJ', 'Rio de Janeiro'],
  '22': ['RJ', 'C. dos Goytacazes'],
  '24': ['RJ', 'Petropolis'],
  '84': ['RN', 'Natal'],
  '51': ['RS', 'Porto Alegre'],
  '53': ['RS', 'Pelotas'],
  '54': ['RS', 'Caxias do Sul'],
  '55': ['RS', 'Santa Maria'],
  '69': ['RO', 'Porto Velho'],
  '95': ['RR', 'Boa Vista'],
  '47': ['SC', 'Joinville'],
  '48': ['SC', 'Florianopolis'],
  '49': ['SC', 'Chapeco'],
  '11': ['SP', 'Sao Paulo'],
  '12': ['SP', 'Sao Jose dos Campos'],
  '13': ['SP', 'Santos'],
  '14': ['SP', 'Bauru'],
  '15': ['SP', 'Sorocaba'],
  '16': ['SP', 'Ribeirao Preto'],
  '17': ['SP', 'Sao Jose do Rio Preto'],
  '18': ['SP', 'Presidente Prudente'],
  '19': ['SP', 'Campinas'],
  '79': ['SE', 'Aracaju'],
  '63': ['TO', 'Palmas'],
}


def calcCPF(num):
  somatorio = 0
  qtde = (len(num)+1)
  for i in xrange(qtde-1):
    somatorio += (num[i]*(qtde-i))
  resto = 11-(somatorio % 11)
  if resto < 10: return resto
  return 0


def getCPF():
  n = [randint(0,9) for i in xrange(9)]
  n.append(calcCPF(n))
  n.append(calcCPF(n))
  n.insert(3,'.')
  n.insert(7,'.')
  n.insert(11,'-')
  mm = ''.join([str(n[j]) for j in xrange(14)])
  return mm

def calcCC(num):
  somatorio = 0
  for i in range(len(num)):
    if ((i+1)%2==0):
      somatorio+=num[i]
    else:
      if ((num[i]*2)>9): somatorio += (2*num[i]-9)
      else: somatorio += (2*num[i])
  if ((somatorio%10)==0): return 0
  else: return (10-(somatorio%10))

def getCC():
  n = [randint(0,9) for i in xrange(15)]
  n[0] = randint(3,6)
  n.append(calcCC(n))
  n.insert(4,'.')
  n.insert(9,'.')
  n.insert(14,'.')
  mm = ''.join([str(n[j]) for j in xrange(19)])
  return mm

def genrg():
  rg = [randint(0,9) for i in range(8)]
  soma = sum([(2+i)*rg[i] for i in range(8)])
  rg = ''.join([str(x) for x in rg])
  for dv in range(10):
    if (soma + dv*100) % 11 == 0:
      break
  return rg + str(dv)

def gerapessoa():
  genero = randint(0,1)
  ddd=slDDD[randint(0,len(slDDD)-1)]
  _nomec = '%s %s' % ( ' '.join([nomes[genero][randint(0 ,len(nomes[genero])-1)] for k in xrange(randint(1,2))]) , ' '.join([sobrenomes[randint(0,len(sobrenomes)-1)] for k in xrange(randint(1,3))]) )
  _logradouro = '%s %s %s %s, %s' % ( logradouro[randint(0,len(logradouro)-1)],ruas[randint(0,len(ruas)-1)],nomes[0][randint(0,len(nomes[0])-1)],sobrenomes[randint(0,len(sobrenomes)-1)], str(randint(1,999)) )
  cep = [str(randint(0,9)) for k in xrange(8)]
  cep.insert(2,'.')
  cep.insert(6,'-')
  _cidade = (upper(lsDDD[ddd][1]))
  _uf = lsDDD[ddd][0]
  _cep = ''.join(cep)
  _fone = '(%s)%s-%s' % (ddd,''.join([str(randint(0,9)) for k in xrange(4)]),''.join([str(randint(0,9)) for k in xrange(4)]))
  _sexo = sexo[genero]
  _cpf = getCPF()
  _rg = '%s SSP %s' % (genrg(),lsDDD[ddd][0])
  _dt_nasc = '%02d/%02d/%d' % (randint(1,30),randint(1,12),randint(1930,2005))
  _vencimentocc = '%02d/%d' % (randint(1,12),randint(2016,2025))
  _mae = '%s %s' % ( ' '.join([nomes[1][randint(0 ,len(nomes[1])-1)] for k in xrange(randint(1,2))]) , ' '.join([sobrenomes[randint(0,len(sobrenomes)-1)] for k in xrange(randint(1,3))]) )
  _sangue = '%s%s' % (sangueT[randint(0,len(sangueT)-1)],sangueF[randint(0,1)])
  zimeiu = _nomec.split(' ')
  _email = lower('%s%s%s@%s') % (zimeiu[0],emailsep[randint(0,len(emailsep)-1)],''.join([zimeiu[k][0] for k in range(1,len(zimeiu))]),email[randint(0,len(email)-1)])
  _senha = '%s' % ''.join([alfanum[randint(0,len(alfanum)-1)] for k in xrange(randint(4,21))])
  _cc = '%s' % getCC()
  _cvv = '%d' % randint(100,999)
  imc = uniform(19,29)
  peso = uniform(42,89)
  altura = sqrt(peso/imc)
  _peso = '%.2f kg' % peso
  _altura ='%.2f m' % altura
  _emprego = '%s' % empregos[genero][randint(0,len(empregos[0])-1)]
  return {'nome':_nomec, 'endereco': {'logradouro': _logradouro, 'cidade': _cidade, 'uf': _uf, 'cep':_cep}, 'telefone': _fone, 'sexo':_sexo, 'documentos': {'cpf':_cpf,'rg':_rg}, 'nascimento':_dt_nasc,'mae':_mae,
          'sangue':_sangue,'email':_email,'senha':_senha,'cartao de credito': {'numero': _cc, 'cvv': _cvv, 'validade':_vencimentocc }, 'peso': _peso, 'altura':_altura, 'emprego':_emprego}

if __name__ == '__main__':
  print gerapessoa()