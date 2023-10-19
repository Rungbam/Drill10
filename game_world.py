# 게임월드 모듈

# 게임월드 표현
world = [ [], [] ] # 2개의 레이어

# 게임월드에 객체 담기
def add_object(o, depth = 0):
    world[depth].append(o)  # 지정된 깊이의 레이어에 객체 추가


# 게임월드 객체들을 몽땅 업데이트
def update():
    for o in world:
        o.update()


# 게임월드의 객체들을 몽땅 그리기
def render():
    for o in world:
        o.draw()


# 객체 삭제
def remove_object(o):
    world.remove(o)