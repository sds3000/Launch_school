def local_greet(locale):
    code = extract_language(locale)
    return greet(code)


def greet(code):
    match code:
        case "US":
            return "Hi"
        case "GB":
            return "Oi"
        case "FR" | "CA" | "MA":
            return "Salut"
        case _:
            return "unknown language"


def extract_language(lang):
    lst = lang.split(".")[0].split("_")[1]
    return lst


print(local_greet("en_US.UTF-8"))  # Hey!
print(local_greet("en_GB.UTF-8"))  # Hello!
print(local_greet("en_AU.UTF-8"))  # Howdy!
print(local_greet("fr_FR.UTF-8"))  # Salut!
print(local_greet("fr_CA.UTF-8"))  # Salut!
print(local_greet("fr_MA.UTF-8"))  # Salut!
