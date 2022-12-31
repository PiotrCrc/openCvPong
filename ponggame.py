import cv2 as cv

class ball:
    def __init__(self, start_x, start_y):
        self.wektor_x = 10.0
        self.wektor_y = 10.0
        self.pozycja_x = start_x
        self.pozycja_y = start_y

    def nowa_pozycja(self):
       # print(self.pozycja_x,self.pozycja_y)
        self.pozycja_x += self.wektor_x
        self.pozycja_y += self.wektor_y

    def odbij_x(self):
        self.wektor_x *= -1

    def odbij_y(self):
        self.wektor_y *= -1


class ponggame:
    def __init__(self,height,width):
       # print(f"Stworzono nową grę {width}, {height}")
        self.width = width
        self.height = height
        self.ball = ball(width // 2, height // 2 )

    def nastpena_klatka(self):
        # sprawdź czy pozycja jest prz brzegu
        if (self.ball.pozycja_x < 10) or (self.ball.pozycja_x > (self.width - 10)):
            self.ball.odbij_x()
        if (self.ball.pozycja_y < 10) or (self.ball.pozycja_y > (self.height - 10)):
            self.ball.odbij_y()
        self.ball.nowa_pozycja()

    def rysuj_pilke(self,image):
        cv.circle(image,(int(self.ball.pozycja_x),int(self.ball.pozycja_y)),5,(255,255,255),2)





