voll: int = int(input("what is the vollume?"))
if voll == 0:
    print("mute")
    match voll:
        case 1 | 2:
            print("very quiet")
        case 3 :
            print("quiet")
            case 3:
            print("quiet")
            case 4:
            print("moderately quiet")
            case 5:
            print("medium")
            case 6:
            print("moderatly loud")
            case 7:
            print("loud")
            case 8:
            print("very loud")
            case 9 | 10:
            print("extremely loud")