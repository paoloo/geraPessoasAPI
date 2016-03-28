# -*- coding: utf-8 -*-

from bottle import Bottle, response
import core

class srv:
  def __init__(self, host='', porta=8080):
    self._h = host
    self._p = porta
    self._a = Bottle()
    self._rota()
    self._g = core

  def _rota(self):
    self._a.route('/pessoa', callback=self.geraPessoa)
    self._a.route('/pessoas/<qtd>', callback=self.geraPessoa)

  def go(self):
    self._a.run(host=self._h, port=self._p)

  def geraPessoa(self, qtd=1):
    response.headers['Content-Type']='application/json'
    _temp = []
    for i in range(int(qtd)):
      _temp.append(self._g.gerapessoa())
    _dd = {'pessoas':_temp}
    return _dd

if __name__=='__main__':
  s=srv().go()
