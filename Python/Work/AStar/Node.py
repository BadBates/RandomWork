import AStar
from AStar import *

class Vec2(object):
 def __init__(self, nx, ny):
  self.x = nx
  self.y = ny  
 
 def add2D(self, other):
  nv = Vec2(0,0)
  nv.x = self.x + other.x
  nv.y = self.y + other.y
  return nv
 
 def sub2D(self, other):
  nv = Vec2(0,0)
  nv.x = self.x - other.x
  nv.y = self.y - other.y
  return nv
    
 def mag2(self, other):
  nv = Vec2(0,0)
  nv = sqrt((self.x * self.x) + (self.y * self.y))
  return nv
  
 def nor2x(self, other):
  nv = Vec2(0,0)
  nv = (self.x / sqrt((self.x * self.x) + (self.y * self.y)))
  return nv 
  
 def nor2y(self, other):
  nv = Vec2(0,0)
  nv = (self.y / sqrt((self.x * self.x) + (self.y * self.y)))
  return nv 
  
 def multi2D(self, other):
  nv = Vec2(0,0)
  dv = 0
  nv.x = self.x * other.x
  nv.y = self.y * other.y
  dv = (nv.x + nv.y)
  return dv
 
 def lin2D(self,other):
  nv = Vec2(0,0)
  nv.x = (self.x +(.5 *(other.x - self.x)))
  nv.y = (self.y +(.5 *(other.y - self.y)))
  return nv
   
 def info2D(self):
  print (self.x, ",", self.y)
  
class Vec3(object):
 def __init__(self, nx, ny, nz):
  self.x = nx
  self.y = ny 
  self.z = nz

 def add3D(self, other):
  nv = Vec3(0,0,0)
  nv.x = self.x + other.x
  nv.y = self.y + other.y
  nv.z = self.z + other.z
  return nv

 def sub3D(self, other):
  nv = Vec3(0,0,0)
  nv.x = self.x - other.x
  nv.y = self.y - other.y
  nv.z = self.z - other.z
  return nv
 
 def mag3(self, other):
  nv = Vec3(0,0,0)
  nv = sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
  return nv
 
 def nor3x(self, other):
  nv = Vec3(0,0,0)
  nv = (self.x / sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z)))
  return nv 
  
 def nor3y(self, other):
  nv = Vec3(0,0,0)
  nv = (self.y / sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z)))
  return nv
  
 def nor3z(self,other):
  nv = Vec3(0,0,0)
  nv = (self.z / sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z)))
  return nv
  
 def multi3D(self, other):
  nv = Vec3(0,0,0)
  dv = 0
  nv.x = self.x * other.x
  nv.y = self.y * other.y
  nv.z = self.z * other.z
  dv = (nv.x + nv.y + nv.z)
  return dv
 
 def lin3D(self, other):
  nv = Vec3(0,0,0)
  nv.x = (self.x +(.5 *(other.x - self.x)))
  nv.y = (self.y +(.5 *(other.y - self.y)))
  nv.z = (self.z +(.5 *(other.z - self.z)))
  return nv
  
 def cross3D(self, other):
  nv = Vec3(0,0,0)
  nv = ((self.y * other.z) - (self.z * other.y),(self.z * other.x) - (self.x * other.z),(self.x * other.y) - (self.y * self.x))
  return nv
  
 def info3D(self):
  print (self.x, ",", self.y, ",", self.z)