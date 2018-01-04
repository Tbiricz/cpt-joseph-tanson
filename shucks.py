def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)

class Bullet:
    def __init__(self, v1, v2):
        self.lo = PVector(v1.x, v1.y)
        self.sp = trajectory(v1, v2).mult(7)
        self.done = False
        
class Player:
    def __init__(self, lo, si):
        self.lo = PVector(lo.x, lo.y)
        self.si = si

class Slime:
    def __init__(self, lo, si, sp):
        self.lo = PVector(lo.x, lo.y)
        self.si = si
        self.sp = PVector(sp.x, sp.y)
