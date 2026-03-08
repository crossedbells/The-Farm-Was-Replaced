import is_even

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			
			if is_even.check(get_pos_x(),get_pos_y())==True:
				plant(Entities.Tree)
				use_item(Items.Fertilizer)
			else:
				till()
				plant(Entities.Carrot)
				
				#get_water()
				
				#if get_water()==0:
			use_item(Items.Water)
			move(North)
		
		move(East)
		if can_harvest():
				harvest()
				
				
				
				
				