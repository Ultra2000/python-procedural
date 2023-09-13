animal = "lion"

match animal:
    case "chat":
        print("Je suis un Chat")
    case "chien":
        print("Je suis un chien")
    case "lion":
        print("Je suis un lion")
    case "souris":
        print("Je suis une belle souris")
    case _:
        print("Je ne connais pas cet animal")