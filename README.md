# hello_pygame



파이썬의 ```pygame```으로 게임을 만들어보자!



### 💗 하트모으기 게임 



![dd](https://user-images.githubusercontent.com/51187540/111722329-fb79a700-88a4-11eb-9735-dfdaebe6a70b.gif)









- 설정해야 될 것

  - 보이의 움직임 

    - ```pygame.KEYDOWN```, ```pygame.K_LEFT```등으로 설정

  - 화면에 보일 하트의 개수

    ```python
    ##하트 이미지
        love_image = pygame.image.load('image/love.png')
        loves = []
        for i in range(3): # 화면에 세개만
            love = love_image.get_rect(left=random.randint(0, 600 - love_image.get_width()), top=-100) # 가로 위치를 0~600 사이의 랜덤으로
            dy = random.randint(3, 9) # 빠르기도 3~9 랜덤으로
            loves.append((love, dy))
    ```

  - 생명 개수



- 화면에 하트 세개가 있도록 설정, 랜덤 속도 설정, 화면을 벗어나거나 없어졌을 때 다시 하트 붙여주기

  ```python
  for love, dy in loves: # dy는 빠르기
  	love.top += dy
      if love.top > 800: # 하트가 바닥에 닿이면 하트 빼기
         lifes.pop()
      if len(lifes) == 0 : # 생명 없을 때는 게임오버
         game_over = True
      loves.remove((love, dy))
      love = love_image.get_rect(left=random.randint(0, 600 - love.width), top=-100)
      dy = random.randint(3, 9)
      loves.append((love, dy))
  ```

  

- 하트에 닿였을 때 

  ```python
  if love.colliderect(boy_pos):
  	score += 1 # 점수 추가
      loves.remove((love, dy)) # 하트 삭제 (이 때 삭제 안하면 점수가 계속 올라감)
  
      #하트 다시 붙여서 내려주기
      love = love_image.get_rect(left=random.randint(0, 600 - love.width), top=-100)
      dy = random.randint(3, 9)
      loves.append((love, dy))
  ```

  

