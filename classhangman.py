import turtle
t=turtle.Pen()
import re
class hangman:
    
    def __init__(self):
        self.hangingrod()
        self.headx,self.heady=t.position()
        self.word=self.loadword()
        t.penup()
        t.setpos(-150,-80)
        t.left(90)
        t.pendown()
        for i in range (len(self.word)-1):
            t.forward(25)
            t.penup()
            t.forward(20)
            t.pendown()
                    
    def loadword(self):
        import random
        try:
            with open ('wordfile.txt') as f:
                wrdlist=(f.readlines())
                randnum=random.randint(0,(len(wrdlist)-1))
                return(wrdlist[randnum])
        except:
            print('not open')
            pass
        
    def hangingrod(self):
        t.pendown()
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(30)
        
    def head(self):
        t.penup()
        t.setpos(self.headx,self.heady)
        t.backward(30)
        t.right(90)
        t.forward(30)
        t.pendown()
        t.circle(30)
        t.left(90)

    def body(self):
        t.penup()
        t.setpos(self.headx,self.heady-60)
        t.right(t.heading())
        t.right(90)
        t.pendown()
        t.forward(100)

    def lhand(self):
        t.penup()
        t.setpos(self.headx,self.heady-90)
        t.right(t.heading())
        t.right(180)
        t.right(45)
        t.pendown()
        t.forward(30)

    def rhand(self):
        t.penup()
        t.setpos(self.headx,self.heady-90)
        t.right(t.heading())
        t.left(45)
        t.pendown()
        t.forward(30)

    def lleg(self):
        t.penup()
        t.setpos(self.headx,self.heady-160)
        t.right(t.heading())
        t.right(180)
        t.left(45)
        t.pendown()
        t.forward(50)

    def rleg(self):
        t.penup()
        t.setpos(self.headx,self.heady-160)
        t.right(t.heading())
        t.right(45)
        t.pendown()
        t.forward(50)
        
    def fillspaces(self,pos,char):
        t.penup()
        xpos=-150
        t.setpos(xpos,-80)
        for i in range (len(pos)):
            xpos=-150
            t.penup()
            t.right(t.heading())
            xpos=xpos+45*pos[i]
            t.setpos(xpos,-80)
            t.pendown()
            self.print_char(char)
            
    def checkword(self):
        mis=[]
        c=0
        while True:
            char=input('Guess the letter')
            if len(char) > 1:
                print ("Error! Only 1 character allowed!")
            else:
                pos=[]
                for i in range (len(self.word)-1):
                    if self.word[i]==char:
                        pos.append(i)
                c=c+len(pos)
            
                
                            
                if len(pos)<1:
                    mis.append(char)
                    if len(mis)>=6:
                        self.rleg()
                        print('You lost!!!')
                        print('The word is-',self.word)
                        break
                
                    else:
                        self.error(len(mis))
                else:
                    self.fillspaces(pos,char)
                    
            if c==(len(self.word)-1):
                print('You won!!!')
                break
                    
    def printA(self):
        t.left(90)
        t.forward(33)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.left(90)
        
    def printB(self):
        t.left(90)
        t.forward(33.33)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)

    def printC(self):
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.right(90)
        t.forward(33.33)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        

    def printD(self):
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.right(90)
        t.forward(33.33)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(33.33)
        t.left(90)


    def printE(self):
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        

    def printF(self):
        t.left(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)

    def printG(self):
        t.forward(16.66)
        t.left(90)
        t.forward(16.66)
        t.right(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(33.33)
        t.right(90)
        t.forward(16.66)
        
    def printH(self):
        t.left(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(180)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.penup()
        t.right(90)
        t.forward(16.66)
        t.pendown()
        t.right(90)
        t.forward(33.33)
        t.left(90)


    def printI(self):
        t.forward(16.66)
        t.left(180)
        t.forward(8.33)
        t.right(90)
        t.forward(33.33)
        t.left(90)
        t.forward(8.33)
        t.left(180)
        t.forward(16.66)

    def printJ(self):
        t.left(90)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.left(90)
        t.forward(8.33)
        t.left(90)
        t.forward(33.33)
        t.left(90)
        t.forward(8.33)
        t.left(180)
        t.forward(8.33)
        t.right(90)
        t.forward(33.33)
        t.left(90)


    def printK(self):
        t.left(90)
        t.forward(33.33)
        t.left(180)
        t.forward(16.66)
        t.left(135)
        t.forward(23.55)
        t.left(180)
        t.forward(23.55)
        t.left(90)
        t.forward(23.55)
        t.left(45)

    def printL(self):
        t.left(90)
        t.forward(33.33)
        t.left(180)
        t.forward(33.33)
        t.left(90)
        t.forward(16.66)


    def printM(self):
        t.left(90)
        t.forward(33.33)
        t.right(135)
        t.forward(18.6)
        t.left(90)
        t.forward(18.6)
        t.right(135)
        t.forward(33.33)
        t.left(90)


    def printN(self):
        t.left(90)
        t.forward(33.33)
        t.right(150)
        t.forward(38.55)
        t.left(150)
        t.forward(33.33)
        t.left(180)
        t.forward(33.33)
        t.left(90)

    def printO(self):
        t.left(90)
        t.forward(1.66)
        t.forward(30)
        t.right(45)
        t.forward(1.35)
        t.right(45)
        t.forward(13.33)
        t.right(45)
        t.forward(1.35)
        t.right(45)
        t.forward(30)
        t.right(45)
        t.forward(1.35)
        t.right(45)
        t.forward(13.33)
        t.right(45)
        t.forward(1.35)
        t.right(180)
        t.forward(1.35)
        t.left(45)
        t.forward(13.33)
        t.forward(1.66)

    def printP(self):
        t.left(90)
        t.forward(33.33)
        t.right(90)
        t.forward(15)
        t.right(45)
        t.forward(7.07)
        t.right(45)
        t.forward(13.33)
        t.right(45)
        t.forward(7.07)
        t.right(45)
        t.forward(15)
        t.left(90)
        t.forward(16.66)

    def printQ(self):
        t.left(90)
        t.forward(30)
        t.right(45)
        t.forward(4.4)
        t.right(45)
        t.forward(10)
        t.right(45)
        t.forward(4.4)
        t.right(45)
        t.forward(26.66)
        t.right(45)
        t.forward(4.4)
        t.right(45)
        t.forward(10)
        t.right(45)
        t.forward(4.4)
        t.right(180)
        t.forward(4.4)
        t.left(45)
        t.forward(10)
        t.left(45)
        t.forward(2.35)
        t.left(90)
        t.forward(2.35)
        t.left(180)
        t.forward(25)

    def printR(self):
        t.left(90)
        t.forward(33.33)
        t.right(90)
        t.forward(15)
        t.right(45)
        t.forward(2.3)
        t.right(45)
        t.forward(13.33)
        t.right(45)
        t.forward(2.3)
        t.right(45)
        t.forward(15)
        t.left(180)
        t.forward(6.66)
        t.right(60)
        t.forward(20)
        t.left(60)

    def printS(self):
        t.forward(16.66)
        t.left(90)
        t.forward(16.66)
        t.left(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)
        t.right(90)
        t.forward(16.66)

    def printT(self):
        t.forward(10)
        t.left(90)
        t.forward(33.33)
        t.left(90)
        t.forward(10)
        t.left(180)
        t.forward(20)
        t.right(90)

    def printU(self):
        t.forward(0.55)
        t.left(135)
        t.forward(0.77)
        t.right(45)
        t.forward(31.66)
        t.left(180)
        t.forward(31.66)
        t.left(45)
        t.forward(2.35)
        t.left(45)
        t.forward(13.33)
        t.left(45)
        t.forward(2.35)
        t.left(45)
        t.forward(31.66)
        t.left(180)
        t.forward(31.66)
        t.right(45)
        t.forward(2.35)
        t.left(135)
        t.forward(1.66)

    def printV(self):
        t.forward(8.33)
        t.left(135)
        t.forward(18.63)
        t.right(45)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.left(45)
        t.forward(18.63)
        t.left(90)
        t.forward(18.63)
        t.left(45)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)

    def printW(self):
        t.left(90)
        t.forward(33.33)
        t.left(180)
        t.forward(33.33)
        t.left(135)
        t.forward(18.63)
        t.right(90)
        t.forward(18.63)
        t.left(135)
        t.forward(33.33)
        t.left(180)
        t.forward(33.33)
        t.left(90)

    def printX(self):
        t.forward(16.66)
        t.left(116.551)
        t.forward(37.26)
        t.left(180)
        t.forward(18.63)
        t.right(53.102)
        t.forward(18.63)
        t.left(180)
        t.forward(37.26)

    def printY(self):
        t.forward(8.33)
        t.left(90)
        t.forward(16.66)
        t.left(40)
        t.forward(21.66)
        t.left(180)
        t.forward(21.66)
        t.left(100)
        t.forward(21.66)
        t.left(180)
        t.forward(21.66)
        t.left(40)
        t.forward(16.66)
        t.left(90)
        t.forward(10)

    def printZ(self):
        t.left(63.45)
        t.forward(37.26)
        t.left(116.55)
        t.forward(16.66)
        t.left(180)
        t.forward(16.66)
        t.right(116.551)
        t.forward(37.26)
        t.left(116.55)
        t.forward(16.66)
        
    def print_char(self,char):
        switcher={
            'A':self.printA,
            'B':self.printB,
            'C':self.printC,
            'D':self.printD,
            'E':self.printE,
            'F':self.printF,
            'G':self.printG,
            'H':self.printH,
            'I':self.printI,
            'J':self.printJ,
            'K':self.printK,
            'L':self.printL,
            'M':self.printM,
            'N':self.printN,
            'O':self.printO,
            'P':self.printP,
            'Q':self.printQ,
            'R':self.printR,
            'S':self.printS,
            'T':self.printT,
            'U':self.printU,
            'V':self.printV,
            'W':self.printW,
            'X':self.printX,
            'Y':self.printY,
            'Z':self.printZ
            }
        switcher[char]()
        
    def error(self,bdnum):
        switcher={
            1:self.head,
            2:self.body,
            3:self.lhand,
            4:self.rhand,
            5:self.lleg,
            }
        switcher[bdnum]()
