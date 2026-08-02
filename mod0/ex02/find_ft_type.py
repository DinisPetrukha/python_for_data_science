def all_thing_is_obj(object: any) -> int:
    if (type(object) is int):
        print("Type not found")
    elif (type(object) is str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
    	print(f"{(type(object).__name__).capitalize()} : {type(object)}")
	return 42