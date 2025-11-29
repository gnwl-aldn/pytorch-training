from utils.count import count_world

if __name__ == "__main__":
    s = "hello world"
    print("e:", count_world(s, "e")) # 1
    print("o:", count_world(s, "o")) # 2
    print("l:", count_world(s, "l")) # 3