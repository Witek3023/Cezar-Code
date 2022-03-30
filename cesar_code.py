alphabet = {'A': 'C', 'Ą': 'Ć', 'B': 'D', 'C': 'E', 'Ć': 'Ę', 'D': 'F', 'E': 'G', 'Ę': 'H', 'F': 'I', 'G': 'J',
            'H': 'K', 'I': 'L', 'J': 'Ł', 'K': 'M', 'L': 'N', 'Ł': 'Ń', 'M': 'O', 'N': 'Ó', 'Ń': 'P', 'O': 'R',
            'Ó': 'S', 'P': 'Ś', 'R': 'T', 'S': 'U', 'Ś': 'W', 'T': 'Y', 'U': 'Z', 'W': 'Ź', 'Y': 'Ż', 'Z': 'A',
            'Ź': 'Ą', 'Ż': 'B'}


def cezar(func):
    def wrapper():
        solution = []
        for i in func():   # encrypting loop
            i = i.upper()
            solution.append(alphabet[i])
        # for i in range(len(solution)):  writing encrypted word
        return "".join(solution)
    return wrapper


@cezar  # decorator
def word():
    return 'witek'


print(word())
