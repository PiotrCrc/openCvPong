import cv2 as cv

class ball:
    def __init__(self, start_x, start_y, ball_jump):
        self.wektor_x = ball_jump
        self.wektor_y = ball_jump
        self.pozycja_x = start_x
        self.pozycja_y = start_y
        self.ball_jump = ball_jump

    def nowa_pozycja(self):
       # print(self.pozycja_x,self.pozycja_y)
        self.pozycja_x += self.wektor_x
        self.pozycja_y += self.wektor_y

    def odbij_x(self):
        self.wektor_x *= -1

    def odbij_w_prawo(self):
        self.wektor_x = self.ball_jump

    def odbij_w_lewo(self):
        self.wektor_x = -self.ball_jump

    def odbij_y(self):
        self.wektor_y *= -1


class ponggame:
    def __init__(self,height,width):
       # print(f"Stworzono nową grę {width}, {height}")
        self.ball_jump = 1
        self.width = width
        self.height = height
        self.ball = ball(self.width // 2, self.height // 2 , self.ball_jump)

    def nastpena_klatka(self,image):
        # sprawdź czy na drodze jest przeszkoda
        crop = image[self.ball.pozycja_y-1:self.ball.pozycja_y+1,self.ball.pozycja_x-1:self.ball.pozycja_x+1]
        if crop.mean() > 0:
            if self.ball.pozycja_x < (self.width/2):
                self.ball.odbij_w_prawo()
            else:
                self.ball.odbij_w_lewo()
        # sprawdź czy pozycja jest prz brzegu
        if (self.ball.pozycja_x < 10) or (self.ball.pozycja_x > (self.width - 10)):
            self.ball.odbij_x()
        if (self.ball.pozycja_y < 10) or (self.ball.pozycja_y > (self.height - 10)):
            self.ball.odbij_y()

        self.ball.nowa_pozycja()

    def rysuj_pilke(self,image):
        cv.circle(image,(int(self.ball.pozycja_x),int(self.ball.pozycja_y)),5,(255,255,255),2)





