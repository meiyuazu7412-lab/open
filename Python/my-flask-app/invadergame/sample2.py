import os
os.chdir(os.path.dirname(__file__))  # このファイルの場所に切り替える

import pygame
import random
from pygame import mixer #ゲームに音をつける
import math


pygame.init() #pygameを初期化

screen=pygame.display.set_mode((800,600))   #スクリーンのサイズ指定
screen.fill((135, 206, 235))    #背景の色を変える（pygame.display.update()を記載しないと反映されない）150は左からRed,Green、Blueを表す
pygame.display.set_caption('Invaders Game')     #題名をInvaders Gameに変える



 #Player
playerImg = pygame.image.load('hato.png')    #playerのイメージ画像をダウンロードした
playerX,playerY=370,480 #playerのイメージ画像を出す座標を指定
playerX_change = 0 #十字キーで動くように座標を設定

 #Enemy
enemyImg = pygame.image.load('pinkenemy.png')
enemyX = random.randint(0, 370) #ランダムな座標から敵が出現するようにする
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 0.5, 40

#Bullet
bulletImg = pygame.image.load('edamame.png')
bulletX,bulletY = 0,480 #弾が出るのはプレイヤーからだからプレイヤーと高さを合わせる
bulletX_change, bulletY_change = 0, 3#横には弾は飛ばないからXは0でよい
bullet_state ='ready'#弾が打てる状態にあるよって事

#score
score_value = 0

def player(x,y):
    screen.blit(playerImg,(x,y)) #pygame.image.load('player.png')~Y=480でダウンロードしたものを表示する

def enemy(x,y):
    screen.blit(enemyImg,(x,y)) 
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'#弾が発射されたらステータスがfireになる
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):#弾が敵とぶつかったか計算する関数。敵の座標と弾の座標で計算する
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))#敵の玉の距離を測る
    if distance < 27:#計算結果が27より小さかったら当たり判定
        return True
    else:
        return False

running = True         #screen=pygame.display.set_mode((800,600))はスクリーンを出すコード。それだと一瞬しか出ないためrunning = True~while running:で無限ループで表示させ続ける
while running:
    screen.fill((135, 206, 235)) 
    cloudImg = pygame.image.load('cloud.png')
    screen.blit(cloudImg, (150, 100))  # 好きな位置に配置できるよ
    cloudImg = pygame.image.load('cloud1.png')
    screen.blit(cloudImg, (550, 300))  # 好きな位置に配置できるよ
    cloudImg = pygame.image.load('cloud1.png')
    screen.blit(cloudImg, (5, 400))  # 好きな位置に配置できるよ
    cloudImg = pygame.image.load('sun.png')
    screen.blit(cloudImg, (650, 1))  # 好きな位置に配置できるよ
   
   
   
    for event in pygame.event.get():        #マウスの操作とか、どこを押したとかの情報を受け取れるようになるのが.event.gat（.event＝行動．get=受け取る）　
        if event.type == pygame.QUIT:        #event（行動）の種類が.QUITだった場合は（ウィンドウの左上（閉じるボタン））を押す場合は
            running = False   #running = Flaseになりループが終了し、ウィンドウが閉じる
            
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_LEFT: #左のキーを押したら
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:#右のキーを押したら
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:#スペースキーを押したら
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
              
        if event.type == pygame.KEYUP:#キーから手を離したら元の位置に戻る
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
                
     # Player
    playerX += playerX_change#playerが画面外に行かないようにする操作
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
        
     # Enemy  
    if enemyY > 440:
       break
   
    enemyX += enemyX_change  
    if enemyX <= 0: #左端に来たら
        enemyX_change = 0.8
        enemyY += enemyY_change
    elif enemyX >=736: #右端に来たら
        enemyX_change = -0.8
        enemyY += enemyY_change
        
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)#衝突した場合下記if文が動く
    if collision:
        bulletY = 480
        bullet_state = 'ready'#当たったらレディに戻る
        score_value += 1#当たったらスコアに1を足す。
        enemyX = random.randint(0, 736)#敵が撃破されたら再度出現される
        enemyY = random.randint(50, 150)
 
    if enemyY > 440:
        enemyY = 440
        
         # Bullet Movement
    if bulletY <=0:#敵に当たらず弾がフェードアウトした場合
        bulletY = 480#'ready'に戻す
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  
        
  # Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))

   
    player(playerX,playerY) # screen.blit(playerImg,(x,y)) の中身を起動して表示される
    enemy(enemyX, enemyY)
    
    pygame.display.update()         #screen上の物を書き換えた場合は必ずupdateする必要がある   
        