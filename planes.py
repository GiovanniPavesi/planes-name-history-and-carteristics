caccia_dict={
    'F-35': 'Caccia di quinta generazione progetatto dalla Lokling Martin sotto commissione degli Stati Uniti di America',
    'F-22': 'Primo caccia di quinta generazione mai creato ed è cosiderato ancora oggi relativamente moderno anche esso sotto commissione degli Stati Uniti di America',
    'F-18': 'r'
    }
parola = input("Scrivi un nome di un caccia americano (il nome deve essere tutto maiuscolo e contenere trattini per spaziare numeri da lettere):")
if parola in caccia_dict.keys():
    print(parola + '=' + caccia_dict[parola])
else:
    print('non è ancora presente oppure è stato scritto male, provi a riscriverlo')
