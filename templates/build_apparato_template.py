# -*- coding: utf-8 -*-
"""
Genera la pagina HTML completa: Vangelo con ancoraggi + apparato a 4 fonti + fili logici.
Dimensionata per Viwoods AiPaper 10.65" (1920x2560px @300ppi -> 162.56 x 216.75 mm).
"""

# ---------------------------------------------------------------------------
# DATI: Vangelo segmentato con ancore inline
# ---------------------------------------------------------------------------
GOSPEL_SEGMENTS = [
    # (testo_prima, parola_ancorata, testo_dopo, numero_ancora, marcatore_scrittura_o_None)
    ("", "Dopo che la folla ebbe mangiato, subito Gesù costrinse i discepoli", " a salire sulla barca e a precederlo sull'altra riva, finché non avesse congedato la folla.", 1, None),
    ("Congedata la folla, salì sul monte, in disparte, a pregare. Venuta la sera, egli se ne stava lassù,", " da solo.", "", 2, None),
    ("La barca intanto distava già molte miglia da terra ed era", " agitata dalle onde: il vento infatti era contrario.", "", 3, "α"),
    ("Sul finire della notte egli andò verso di loro", " camminando sul mare.", "", 4, "β"),
    ("Vedendolo camminare sul mare, i discepoli furono sconvolti e dissero:", " «È un fantasma!» e gridarono dalla paura.", "", 5, None),
    ("Ma subito Gesù parlò loro dicendo:", " «Coraggio, sono io, non abbiate paura!».", "", 6, "γ"),
    ("Pietro allora gli rispose: «Signore, se sei tu, comandami di venire verso di te sulle acque».", " Ed egli disse: «Vieni!».", "", 7, "δ"),
    ("", "Pietro scese dalla barca, si mise a camminare sulle acque e andò verso Gesù.", "", 7, None),
    ("Ma,", " vedendo che il vento era forte, s'impaurì e, cominciando ad affondare, gridò: «Signore, salvami!».", "", 8, "ε"),
    ("E subito Gesù tese la mano, lo afferrò e gli disse: «Uomo di poca fede,", " perché hai dubitato?».", "", 9, None),
    ("Appena saliti sulla barca, il vento cessò.", " Quelli che erano sulla barca si prostrarono davanti a lui,", " dicendo: «Davvero tu sei Figlio di Dio!».", 10, None),
]

# ---------------------------------------------------------------------------
# DATI: apparato — un blocco per ancora, con le glosse delle fonti disponibili
# ---------------------------------------------------------------------------
ANCHORS = [
    {
        "num": 1, "label": "Il guado — la forzatura",
        "verse_short": "«Gesù costrinse i discepoli a salire sulla barca…»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Il verbo greco indica una forzatura.",
             "Gesù obbliga i discepoli ad affrontare da soli la traversata. Nella Scrittura il “guado” è figura del cambiamento necessario, come Giacobbe allo Iabbok. Chi non attraversa resta ombra di sé."),
            ("armellini", "A", "Armellini",
             "Anankazein: dovette imporsi, loro resistevano.",
             "“Andare all'altra riva” significa andare verso Oriente, in terra pagana e impura. Non volevano portare il pane, cioè Cristo, ai pagani: volevano trattenerlo per il popolo eletto."),
            ("curtaz", "C", "Curtaz",
             "Li costringe perché non erano contenti di lui.",
             "Poco prima Gesù aveva chiesto di condividere il poco pane con la folla affamata, invece di rimandarla via: i Dodici non hanno gradito, e ora devono partire da soli."),
        ],
        "cross_ref": None,
    },
    {
        "num": 2, "label": "Il monte, la sera, la solitudine",
        "verse_short": "«Salì sul monte, in disparte, a pregare… da solo»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Come Elia sull'Oreb, il monte prepara il passaggio.",
             "Nella I lettura il monte è il luogo dell'incontro che sostiene il cambiamento. Prima della tempesta, Gesù prega: la traversata nasce da lì."),
            ("armellini", "A", "Armellini",
             "“Venuta la sera” è simbolo della fine della sua vita.",
             "Il monte indica il mondo di Dio. Come nel racconto di Marco, la “sera” rappresenta il compimento della missione di Gesù: per questo i discepoli si ritrovano soli, non più visibilmente con lui."),
            ("curtaz", "C", "Curtaz",
             "Forse Gesù si chiede se ha sbagliato a sceglierli.",
             "Tutta la notte, dice Marco; tutta la notte a pregare, dice Luca. Alla prima vera prova i Dodici non hanno capito niente — eppure lui sceglie di non sceglierne altri, di fare il fuoco con la legna che ha."),
        ],
        "cross_ref": None,
    },
    {
        "num": 3, "label": "La tempesta, il mare del caos",
        "verse_short": "«…agitata dalle onde: il vento infatti era contrario»",
        "sources": [
            ("rosini", "R", "Rosini",
             "In ogni cambiamento c'è di mezzo una perdita.",
             "L'acqua ingovernabile è segno di morte nella mentalità biblica: il diluvio, le acque primordiali, il Mar Rosso. La tempesta non è un incidente: è la forma che prende ogni vera crescita."),
            ("armellini", "A", "Armellini",
             "Basanizein: non sballottare, ma torturare, saggiare.",
             "Il verbo viene da basanos, la pietra usata per verificare i metalli preziosi. Le onde sono le prove che ogni comunità deve affrontare: la mondanità, gli scandali interni, le tradizioni obsolete (cfr. Sal 48; Sal 107)."),
            ("curtaz", "C", "Curtaz",
             "È lì, al largo, che si vede se hanno capito.",
             "La tempesta arriva proprio mentre sono soli, alla prima vera prova dopo la richiesta di condividere il pane."),
            ("lectio", "L", "Lectio unificata",
             "Il mare indica la minaccia del caos.",
             "La potenza delle tenebre preme sui margini della creazione per produrre disordine e morte, dove Dio aveva creato ordine e vita."),
        ],
        "cross_ref": "α  Sal 48 · Sal 107",
    },
    {
        "num": 4, "label": "Camminare sul mare — il dominio",
        "verse_short": "«Egli andò verso di loro camminando sul mare»",
        "sources": [
            ("armellini", "A", "Armellini",
             "Solo Dio cammina sulle onde del mare (Gb 9,8).",
             "In tutto il Vicino Oriente antico il mare era il simbolo del male e del caos (mito di Marduk e Yam). Il Dio di Israele non lo vince in una lotta epica: lo doma con la sua parola (Gb 38)."),
            ("lectio", "L", "Lectio unificata",
             "Esprime il dominio sulle potenze del male.",
             "Camminare sull'acqua è segno messianico: il dominio sulla minaccia del caos, di cui il mare è simbolo in tutta la tradizione biblica."),
        ],
        "cross_ref": "β  Gb 9,8 · Gb 38",
    },
    {
        "num": 5, "label": "Lo scambio di persona — «un fantasma»",
        "verse_short": "«Furono sconvolti e dissero: È un fantasma!»",
        "sources": [
            ("rosini", "R", "Rosini",
             "I nostri idoli ricevono un ruolo sbagliato.",
             "Tutto ciò che rendiamo più grande di Dio è un idolo, una paura. Come ricorda san Francesco: bisogna servire il padrone, non il servo."),
            ("armellini", "A", "Armellini",
             "È l'esperienza del “silenzio di Dio”.",
             "Come agli apostoli nel giorno di Pasqua, che si spaventano credendo di vedere un fantasma: solo lo sguardo della fede riconosce il Risorto, non gli occhi materiali."),
            ("curtaz", "C", "Curtaz",
             "Sì, Gesù c'è, ma è aleatorio come un fantasma.",
             "Non sappiamo dov'è in questo momento — è un'esperienza che facciamo anche noi, non solo i discepoli sulla barca."),
            ("lectio", "L", "Lectio unificata",
             "Avevano un'altra immagine del Messia in mente.",
             "Non riconoscono il segno perché non se lo aspettavano così — come Elia avrebbe potuto non riconoscere la teofania nuova sull'Oreb."),
        ],
        "cross_ref": None,
    },
    {
        "num": 6, "label": "«Sono io»",
        "verse_short": "«Coraggio, sono io, non abbiate paura!»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Non una formula di riconoscimento: è il Nome di Dio.",
             "La chiave del non temere non è il mare calmo, ma la presenza di Colui che è (cfr. Es 3,14)."),
            ("armellini", "A", "Armellini",
             "Il Risorto non è condizionato da spazio e tempo.",
             "Non si è allontanato: è al fianco di ognuno sempre, non fisicamente come a Nazaret o Cafarnao, ma non meno realmente."),
            ("curtaz", "C", "Curtaz",
             "Dio si manifesta nella debolezza, non nel prodigio.",
             "Come per Elia, non nel fuoco ma nel silenzio; e per Gesù, che sceglie di non scegliere altri discepoli e si affida a uomini fragili."),
            ("lectio", "L", "Lectio unificata",
             "“Sono io che vi pongo nella prova della fede.”",
             "Non è solo un'identificazione: la tempesta stessa è opera sua, non un incidente estraneo a lui."),
        ],
        "cross_ref": "γ  Es 3,14",
    },
    {
        "num": 7, "label": "Lo slancio di Pietro — «Vieni!»",
        "verse_short": "«Comandami di venire verso di te… Pietro scese dalla barca»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Camminare oltre ciò che temiamo, sulla Parola.",
             "Pietro scende dalla barca perché è Gesù a chiamarlo: quel “Vieni” è detto anche a noi, oggi."),
            ("armellini", "A", "Armellini",
             "La sua paura non è di annegare — è un nuotatore esperto.",
             "A un livello più profondo è la paura di donare la vita fino in fondo, di essere “inghiottito per sempre”, come temeva il salmista (Sal 18)."),
            ("curtaz", "C", "Curtaz",
             "Pietro “decide di fare il fenomeno”.",
             "Un coraggio un po' inopportuno, un po' sbruffone: non è ancora pronto. Ma è bello che la Chiesa sia affidata a uomini fragili come lui, come noi."),
            ("lectio", "L", "Lectio unificata",
             "Due sole strade, non ce n'è una terza.",
             "Fiducia in una Parola non dimostrabile, oppure valore assoluto alle proprie percezioni sensoriali."),
        ],
        "cross_ref": "δ  Sal 18",
    },
    {
        "num": 8, "label": "Il vento forte, la paura",
        "verse_short": "«Vedendo che il vento era forte, s'impaurì… Signore, salvami!»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Guardare il vento rende la difficoltà l'unica realtà.",
             "Immagine della preghiera e della debolezza umana: “Signore, salvami” è il grido di chi sa di non potercela fare da solo."),
            ("armellini", "A", "Armellini",
             "La paura di essere inghiottito per sempre.",
             "Non paura fisica dell'acqua, ma di non farcela a donare tutta la vita fino in fondo, come Gesù chiede."),
            ("curtaz", "C", "Curtaz",
             "Non è ancora pronto — e neppure noi lo siamo sempre.",
             "Ma proprio in questa fragilità, condivisa da Elia e da Gesù stesso, si realizza comunque il sogno di Dio."),
            ("lectio", "L", "Lectio unificata",
             "La fede teologale richiede un orientamento abituale.",
             "Distolto lo sguardo da Cristo verso il vento, Pietro sprofonda: non basta un attimo di fiducia isolato."),
        ],
        "cross_ref": "ε  Os 14,10 · Sal 18",
    },
    {
        "num": 9, "label": "«Perché hai dubitato?»",
        "verse_short": "«Gesù tese la mano, lo afferrò… perché hai dubitato?»",
        "sources": [
            ("rosini", "R", "Rosini",
             "Guarda quanta strada hai già fatto.",
             "Quante volte Dio ha già mostrato la sua potenza nella tua vita? La provvidenza ti ha sorretto fin qui."),
            ("armellini", "A", "Armellini",
             "Il dubbio non riguarda Gesù, ma se stesso.",
             "Forse sarebbe stato meglio restare in barca coi fratelli — è lì il compito che Gesù affiderà poi a Pietro: “conferma nella fede i tuoi fratelli”."),
            ("curtaz", "C", "Curtaz",
             "Anche Elia, anche Gesù vivono lo scoraggiamento.",
             "L'unica condizione per essere discepoli non è l'assenza di dubbio, ma “mettersi in strada”, camminare comunque."),
            ("lectio", "L", "Lectio unificata",
             "Il dubbio, non l'assenza di fede, lo fa affondare.",
             "Che Pietro cammini per alcuni passi dimostra che la sua fede è già in azione."),
        ],
        "cross_ref": None,
    },
    {
        "num": 10, "label": "La barca, la comunità, la confessione finale",
        "verse_short": "«Il vento cessò… Davvero tu sei Figlio di Dio!»",
        "sources": [
            ("rosini", "R", "Rosini",
             "La barca è la nostra zona di sopravvivenza.",
             "Chi resta aggrappato alla zattera sente la chiamata di Dio solo come minaccia. Camminare sulla Parola è ciò che rende bella la vita."),
            ("armellini", "A", "Armellini",
             "Doveva far accogliere Gesù dentro la barca.",
             "Il compito di Pietro non era uscirne, ma far riconoscere a tutti i fratelli che il Risorto non è un fantasma, ma presenza reale nella comunità."),
            ("curtaz", "C", "Curtaz",
             "“Mettersi in strada” è l'unica condizione.",
             "Come Elia, come Gesù, come Pietro — tutti in qualche modo scoraggiati — camminare comunque realizza il sogno di Dio, con la fragilità che abbiamo."),
            ("lectio", "L", "Lectio unificata",
             "La vittoria non è solo liberazione, ma trasformazione.",
             "Il peso che resta viene trasfigurato in gloria (cfr. 2Cor 4,16-17; 12,7-9), non semplicemente rimosso."),
        ],
        "cross_ref": "ζ  2 Cor 4,16-17 · 2 Cor 12,7-9",
    },
]

THREADS = [
    {
        "title": "Filo A — Lo sguardo come chiave della fede",
        "path": [6, 8, 9],
        "note": "“Sono io”: Dio presente anche nella prova → distogliere lo sguardo verso il vento fa affondare → fissarlo sul cammino già fatto, non sulla tempesta.",
    },
    {
        "title": "Filo B — Dalla forzatura al dono di sé",
        "path": [1, 3, 7, 9],
        "note": "Gesù costringe alla traversata → la tempesta come prova necessaria di ogni cambiamento → lo slancio di Pietro sulla Parola → il dubbio come paura di donare tutta la vita.",
    },
    {
        "title": "Filo C — La fragilità che comunque compie il sogno di Dio",
        "path": [2, 7, 10],
        "note": "Gesù stesso sembra dubitare della scelta dei Dodici → Pietro, sbruffone e non ancora pronto → la Chiesa affidata a uomini fragili realizza comunque la missione.",
    },
]

print("dati caricati:", len(ANCHORS), "ancore,", len(THREADS), "fili")
