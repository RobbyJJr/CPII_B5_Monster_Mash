class Orc:
  def __init__ (self, _name,_health=100, _damage=50, _speed=10):
    self.name = _name
    self.health = _health
    self.damage = _damage
    self.speed = _speed
  def attack(self, _target):
    #print(self.name + ' Attacked ' + _target.name)
    print(f'{self.name} Attacked {_target.name}')
  def defend(self):
    print('Defend')
  def heal(self):
    print('Heal')
  def isAlive(self):
    print('isAlive')
  



class Fairy:
  def __init__ (self,_name, _health = 50, _damage = 25, _magic_power = 150, _speed = 50):
    self.name = _name
    self.health = _health
    self.damage = _damage
    self.magic_power = _magic_power
    self.speed = _speed
  def attack(self, _target):
    #print(self.name + ' Attacked ' + _target.name)
    print(f'{self.name} Attacked {_target.name}')
  def defend(self):
    print('Defend')
  def heal(self):
    print('Heal')
  def isAlive(self):
    print('isAlive')
  def magicAttack(self):
    print('magicAttack')




class Elf:
  def __init__ (self,_name, _health = 75, _damage = 50, _magic_power = 100, _speed = 100):
    self.name = _name
    self.health = _health
    self.damage = _damage
    self.magic_power = _magic_power
    self.speed = _speed
  def attack(self):
    print('Attack')
  def defend(self):
    print('Defend')
  def heal(self):
    print('Heal')
  def isAlive(self):
    print('isAlive')
  def magicAttack(self):
    print('magicAttack')
    