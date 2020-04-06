def det_block(floor, pos, direction):
    ele_pos = 0
    for f, p in elevators:
        if f == floor:
            ele_pos = p
            break
    if ele_pos == 0:
        ele_pos = exit_pos
    if pos > ele_pos and direction == 'RIGHT':
        return True
    elif pos < ele_pos and direction == 'LEFT':
        return True

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = [list(map(int, input().split())) for _ in range(nb_elevators)]

# game loop
while True:   
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    if det_block(clone_floor, clone_pos, direction):
        print("BLOCK")
    else:
        print("WAIT")
