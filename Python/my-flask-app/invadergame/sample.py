import pygame
from pygame import mixer #ゲームに音をつける

pygame.init() #pygameを初期化

screen=pygame.display.set_mode((800,600))   #スクリーンのサイズ指定
screen.fill((150,150,150))        #背景の色を変える（pygame.display.update()を記載しないと反映されない）150は左からRed,Green、Blueを表す
pygame.display.set_caption('Invaders Game')     #題名をInvaders Gameに変える

img = pygame.image.load('invadergame/hato.png')    #playerのイメージ画像をダウンロードした
X=370  #playerのイメージ画像を出す座標を指定
Y=480

mixer.Sound('sound/laser.wav').play()      #laser.wavをインポートして音を出力する

running = True         #screen=pygame.display.set_mode((800,600))はスクリーンを出すコード。それだと一瞬しか出ないためrunning = True~while running:で無限ループで表示させ続ける
while running:
    screen.blit(img,(X,Y)) #pygame.image.load('player.png')~Y=480でダウンロードしたものを表示する
    
    font=pygame.font.SysFont(None,80) #フォントの種類とサイズの指定
    message = font.render('Hello World',False,225) #上記で指定したフォントでHello Worldを表示する(255,225,225)色の指定
    screen.blit(message,(20,50))  #フォントを表示する（20，50）は座標
    for event in pygame.event.get():        #マウスの操作とか、どこを押したとかの情報を受け取れるようになるのが.event.gat（.event＝行動．get=受け取る）　
        if event.type == pygame.QUIT:        #event（行動）の種類が.QUITだった場合は（ウィンドウの左上（閉じるボタン））を押す場合は
            running = False               #running = Flaseになりループが終了し、ウィンドウが閉じる
    pygame.display.update()         #screen上の物を書き換えた場合は必ずupdateする必要がある       
    