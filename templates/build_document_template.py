# -*- coding: utf-8 -*-
"""
TEMPLATE — DA RIGENERARE OGNI SETTIMANA (o per ogni festa/giorno feriale).
Dati per il documento finale: sequenze per autore (con connettori),
concetti ricorrenti, sintesi (fili logici), santi, approfondimenti.
Riusa GOSPEL_SEGMENTS e ANCHORS da build_apparato.py come base.

COSA CAMBIA OGNI VOLTA (vedi SKILL.md per il procedimento completo):
- GOSPEL_REF, LITURGICAL_LABEL, DOC_TITLE, FOOTER_CREDITS qui sotto
- SOURCE_ORDER / SOURCE_NAMES / SOURCE_LETTERS / SOURCE_COLORS: 4 fonti se domenica
  (rosini, armellini, curtaz, lectio), 3 se infrasettimanale (epicoco, curtaz, lectio)
- build_apparato.py: GOSPEL_SEGMENTS (testo del Vangelo del giorno, segmentato) e
  ANCHORS (le glosse delle fonti per ciascun ancoraggio)
- CONNECTORS, CONCEPTS, THREADS, SAINTS, APPROFONDIMENTI qui sotto
COSA NON CAMBIA MAI: render_document.py (motore di rendering/CSS/paginazione).
"""
from build_apparato import GOSPEL_SEGMENTS, ANCHORS

# ---------------------------------------------------------------------------
# METADATI DEL GIORNO — cambiano ogni volta
# ---------------------------------------------------------------------------
GOSPEL_REF = "Mt 14,22-33"
LITURGICAL_LABEL = "XIX Domenica del Tempo Ordinario · Anno A · 9 agosto 2026"
DOC_TITLE = f"{GOSPEL_REF} — Vangelo, glosse per autore, concetti, sintesi, santi"

# Ordine delle fonti in questo documento: 4 per la domenica, 3 per l'infrasettimanale
# (in tal caso usare "epicoco" al posto di "rosini" e togliere "armellini")
SOURCE_ORDER = ["rosini", "armellini", "curtaz", "lectio"]

SOURCE_NAMES = {
    "rosini": "Rosini", "armellini": "Armellini", "curtaz": "Curtaz", "lectio": "Lectio unificata",
    "epicoco": "Epicoco",  # usare al posto di "rosini" negli infrasettimanali
}
SOURCE_LETTERS = {"rosini": "R", "armellini": "A", "curtaz": "C", "lectio": "L", "epicoco": "E"}

# Colori per fonte: scelti con luminanza percepita ben distanziata (grigio equivalente
# 50/105/160/210 su 255) cosi' restano distinguibili anche desaturati su e-ink.
# Ciascuna coppia (bg, text) e' verificata per contrasto WCAG (>= 4.9:1).
# Per l'infrasettimanale (3 fonti: epicoco/curtaz/lectio) riusare 3 di questi 4 step
# di luminanza, mantenendo lo stesso criterio se si aggiungono colori nuovi.
SOURCE_COLORS = {
    "rosini":    {"bg": "#1A2E69", "text": "#F5F3EE"},
    "armellini": {"bg": "#237846", "text": "#F5F3EE"},
    "curtaz":    {"bg": "#DD8D5E", "text": "#1C1A17"},
    "lectio":    {"bg": "#E6D09C", "text": "#1C1A17"},
    "epicoco":   {"bg": "#7A2E4D", "text": "#F5F3EE"},  # bordeaux, luminanza ~ intermedia rosini/armellini
}

FOOTER_CREDITS = (
    "Fonti dei commenti: don Fabio Rosini (video) · P. Fernando Armellini (video) · "
    "Paolo Curtaz (video) · Lectio unificata rito romano, cristomaestro.it — "
    "XIX Domenica T.O., anno A, 9 agosto 2026."
)

# connettori: frase breve che lega la glossa precedente alla successiva, per ogni autore
CONNECTORS = {
    "rosini": {
        1: None,
        2: "prima di ogni traversata, l'incontro che la sostiene",
        3: "eppure la tempesta arriva comunque",
        5: "ed è lì che si smaschera cosa temiamo davvero",
        6: "ma è proprio nella prova che Dio si fa riconoscere",
        7: "ed è quella presenza a rendere possibile lo slancio",
        8: "finché lo sguardo non si sposta",
        9: "eppure Gesù non lascia cadere la domanda",
        10: "la stessa domanda vale per la barca a cui restiamo aggrappati",
    },
    "armellini": {
        1: None,
        2: "quella riluttanza nasconde un distacco più profondo",
        3: "e in quell'assenza, la prova si fa sentire sul serio",
        4: "ma chi cammina su quelle stesse acque è già lì",
        5: "eppure non lo riconoscono",
        6: "perché la sua presenza ora è diversa, non meno reale",
        7: "ed è a questa presenza che Pietro chiede di rispondere",
        8: "ma la sua vera paura viene a galla",
        9: "un dubbio che riguarda sé, non il Signore",
        10: "per questo il compito vero non era uscire dalla barca, ma farvi entrare Cristo",
    },
    "curtaz": {
        1: None,
        2: "un rifiuto che pesa anche su di lui",
        3: "un dubbio che la tempesta mette subito alla prova",
        5: "e infatti, quando arriva, non lo riconoscono nemmeno",
        6: "eppure è proprio nella fragilità che si fa vicino",
        7: "e Pietro, davanti a questo, si lancia comunque",
        8: "un coraggio ancora acerbo",
        9: "una fragilità che condivide con tutti, Elia compreso",
        10: "e allora l'unica cosa che davvero conta è",
    },
    "lectio": {
        3: None,
        4: "ma quello stesso mare, Cristo lo attraversa a piedi",
        5: "un segno che però i discepoli non colgono",
        6: "perché non si aspettavano che la prova avesse proprio questo volto",
        7: "e davanti a questa parola, resta solo una scelta",
        8: "una scelta da rinnovare ad ogni istante, non una volta sola",
        9: "ed è proprio lì che si gioca tutto",
        10: "così che, alla fine, quel che resta non va tolto, ma trasfigurato",
    },
}


def author_sequence(slug):
    """Ritorna la lista ordinata di (anchor_num, label, connector, thesis, body) per un autore."""
    seq = []
    for a in ANCHORS:
        for s_slug, letter, name, thesis, body in a["sources"]:
            if s_slug == slug:
                connector = CONNECTORS.get(slug, {}).get(a["num"])
                seq.append((a["num"], a["label"], connector, thesis, body))
    return seq


# ---------------------------------------------------------------------------
# Concetti ricorrenti tra le fonti
# ---------------------------------------------------------------------------
CONCEPTS = [
    {
        "title": "La paura come cattivo maestro",
        "intro": "Guardare la tempesta invece di Gesù è, per tutte e quattro le fonti, la vera causa dell'affondare — ma ciascuna la legge a modo suo.",
        "views": [
            ("rosini", "Guardare il vento rende la difficoltà l'unica realtà percepita: è l'immagine della preghiera e della debolezza umana."),
            ("armellini", "Non è paura fisica — Pietro nuota bene. È la paura di donare la vita fino in fondo, di essere inghiottito per sempre."),
            ("curtaz", "Un coraggio ancora acerbo, 'un po' sbruffone': la fragilità di Pietro è la stessa di chiunque si lanci prima di essere pronto."),
            ("lectio", "La fede teologale ha bisogno di un orientamento abituale, non di un attimo isolato di fiducia."),
        ],
    },
    {
        "title": "Il mare come luogo del caos e della morte",
        "intro": "Il simbolismo biblico del mare — non semplice scenario, ma linguaggio teologico — ricorre in tre delle quattro fonti.",
        "views": [
            ("rosini", "L'acqua ingovernabile è segno di morte nella mentalità biblica: il diluvio, le acque primordiali, il Mar Rosso."),
            ("armellini", "In tutto il Vicino Oriente antico il mare è il mostro del caos (Marduk-Yam); Dio non lo vince in una lotta epica, lo doma con la parola."),
            ("lectio", "Il mare indica la minaccia del caos: la potenza delle tenebre che preme sui margini della creazione per produrre disordine."),
        ],
    },
    {
        "title": "«Sono io»: la presenza di Dio dentro la prova, non dopo",
        "intro": "Le quattro fonti concordano che la frase non è una semplice rassicurazione, ma un'affermazione più radicale sulla natura stessa della prova.",
        "views": [
            ("rosini", "Non una formula di riconoscimento: è il Nome di Dio (Es 3,14). La chiave del non temere è che Lui è."),
            ("armellini", "Il Risorto non è condizionato da spazio e tempo: è al fianco di ognuno sempre, non fisicamente ma non meno realmente."),
            ("curtaz", "Dio si manifesta nella debolezza, non nel prodigio — come per Elia, non nel fuoco ma nel silenzio."),
            ("lectio", "«Sono io che vi pongo nella prova della fede»: la tempesta stessa è opera sua, non un incidente estraneo a lui."),
        ],
    },
    {
        "title": "La fragilità di Pietro come immagine della Chiesa",
        "intro": "Pietro non è un modello di eroismo compiuto, ma — proprio per questo — un'icona più credibile della comunità cristiana reale.",
        "views": [
            ("armellini", "Il compito di Pietro non era uscire dalla barca, ma farvi accogliere Cristo: far riconoscere ai fratelli che il Risorto non è un fantasma."),
            ("curtaz", "È bello che la Chiesa sia stata affidata a uomini fragili come lui, come noi: la fragilità non impedisce che si realizzi il sogno di Dio."),
            ("rosini", "Guarda quanta strada hai già fatto: la stessa domanda rivolta a Pietro vale per la barca — la zattera — a cui anche noi restiamo aggrappati."),
        ],
    },
]

# ---------------------------------------------------------------------------
# Fili logici (sintesi finale)
# ---------------------------------------------------------------------------
THREADS = [
    {
        "title": "Filo A — Lo sguardo come chiave della fede",
        "path": [6, 8, 9],
        "note": (
            "«Coraggio, sono io» non è una rassicurazione che arriva a tempesta finita: è pronunciata "
            "proprio dentro il vento contrario, ed è già di per sé la prova che Dio non abbandona la "
            "barca nel momento peggiore. Ma il «sono io» da solo non basta a tenere Pietro a galla: "
            "appena il suo sguardo si sposta da Gesù al vento, comincia ad affondare — non perché la "
            "fede sia sparita, ma perché ha smesso, per un istante, di essere l'unico punto fermo. La "
            "domanda finale, «perché hai dubitato?», non è un rimprovero ma un invito a guardare "
            "indietro: quanta strada è già stata fatta fidandosi? Il filo che lega questi tre punti è "
            "tutto qui: la fede non elimina il vento, ma decide dove va lo sguardo — e la memoria di "
            "ciò che Dio ha già fatto è il modo concreto per tenerlo fisso."
        ),
        "saint_link": None,
    },
    {
        "title": "Filo B — Dalla forzatura al dono di sé",
        "path": [1, 3, 7, 9],
        "note": (
            "Tutto comincia con una costrizione: Gesù non lascia scelta ai discepoli, li obbliga alla "
            "traversata. È una forzatura che assomiglia a molti passaggi della vita che non si "
            "sceglierebbero mai da soli, e infatti subito arriva la tempesta — non come incidente, ma "
            "come la forma quasi obbligata che ogni vero cambiamento prende. Dentro quella tempesta, "
            "Pietro fa un passo che nessuno gli ha chiesto: scende dalla barca sulla sola parola di "
            "Cristo. È lo slancio più alto del racconto, eppure proprio lì si rivela la sua vera paura "
            "— non quella di annegare, ma quella di dover davvero donare tutta la vita, fino in fondo, "
            "come gli viene chiesto. Il filo è un crescendo: dalla forzatura subita all'inizio, al dono "
            "che si comincia a intuire e che ancora fa paura fino alla fine."
        ),
        "saint_link": {
            "slug": "francesco", "emoji": "🕊️",
            "phrase": "la chiamata che arriva nella rovina, il dono totale di sé",
        },
    },
    {
        "title": "Filo C — La fragilità che comunque compie il sogno di Dio",
        "path": [2, 7, 10],
        "note": (
            "Anche Gesù, in questo racconto, sembra attraversare un momento di dubbio: sale sul monte "
            "da solo dopo aver affidato la missione a dodici uomini che, alla prima vera prova, non "
            "hanno capito quasi nulla. Pietro lo conferma pochi versetti dopo, con uno slancio generoso "
            "ma acerbo, «un po' sbruffone», che lo fa affondare quasi subito. Eppure il racconto non si "
            "chiude con un fallimento: si chiude con tutti, insieme, dentro la stessa barca, che "
            "riconoscono chi hanno davanti. Il filo che attraversa questi tre momenti è una "
            "consolazione precisa per chi guida una comunità: Dio non aspetta persone già pronte per "
            "realizzare qualcosa di grande — sceglie di fare il fuoco con la legna fragile che ha, ed è "
            "proprio così che il suo sogno si compie comunque."
        ),
        "saint_link": None,
    },
    {
        "title": "Filo D — Il mare, la Pasqua, la trasfigurazione della prova",
        "path": [3, 4, 10],
        "note": (
            "Per la mentalità biblica il mare non è mai solo scenario: è la figura stessa del caos che "
            "minaccia di inghiottire l'ordine della creazione, la stessa acqua del diluvio, delle acque "
            "primordiali, del Mar Rosso. Che Cristo lo attraversi camminandoci sopra non è un prodigio "
            "isolato: è un segno messianico preciso, leggibile solo da chi conosce quella grammatica "
            "biblica — il dominio di Dio sul caos, reso visibile in un uomo. Il racconto si chiude non "
            "con la tempesta rimossa come se non fosse mai accaduta, ma con una prova che lascia il "
            "segno e insieme apre alla confessione più alta, «Davvero tu sei Figlio di Dio». Il filo è "
            "pasquale in senso pieno: la prova non viene tolta, viene attraversata e trasfigurata — è "
            "la stessa logica per cui, ancora oggi, ciò che resta di una difficoltà superata spesso "
            "diventa il luogo più fecondo della fede."
        ),
        "saint_link": {
            "slug": "bakhita", "emoji": "✝️",
            "phrase": "la sofferenza riletta come luogo dove Dio si è fatto incontrare",
        },
    },
]

# ---------------------------------------------------------------------------
# Approfondimenti — uno per ciascuno dei 10 ancoraggi, spiegazione estesa
# ---------------------------------------------------------------------------
APPROFONDIMENTI = {
    1: {
        "title": "Il guado — la forzatura",
        "text": (
            "Il verbo greco ἀναγκάζω (anankazō), \"costrinse\", indica una forzatura vera e propria: "
            "non un invito, ma un obbligo a cui i discepoli non si sarebbero sottratti volentieri. "
            "Nella Scrittura, attraversare un'acqua — un guado, un fiume, un mare — è quasi sempre "
            "figura di un passaggio esistenziale che non si sceglie mai fino in fondo da soli. "
            "Giacobbe passa il guado dello Iabbok proprio la notte prima di incontrare il fratello "
            "Esaù che teme di perdere tutto, e ne esce con un nome nuovo, Israele (Gen 32,23-33). "
            "Il popolo d'Israele attraversa il Mar Rosso e poi il Giordano, non per iniziativa propria "
            "ma perché Dio apre la strada e la vita, semplicemente, lo richiede. In questo senso la "
            "forzatura di Gesù non è durezza: è la stessa logica per cui, nella vita spirituale, certi "
            "passaggi — un lutto, una separazione, l'ingresso in una nuova responsabilità — arrivano "
            "prima che siamo pronti, e proprio per questo diventano il luogo dove la fede smette di "
            "essere teoria e diventa cammino reale sull'acqua."
        ),
    },
    2: {
        "title": "Il monte, la sera, la solitudine",
        "text": (
            "Il monte, nella Bibbia, è il luogo per eccellenza dell'incontro con Dio: l'Oreb-Sinai per "
            "Mosè e per Elia (1Re 19), il monte della Trasfigurazione, il monte degli Ulivi. Che Gesù "
            "salga a pregare da solo, immediatamente prima della tempesta, non è un dettaglio di "
            "cronaca ma indica dove nasce la forza per affrontare ciò che segue: non nell'azione, ma "
            "nel silenzio che la precede. La \"sera\" evocata dal testo ha, in tutta la tradizione "
            "biblica, una carica simbolica precisa — è il tempo del bilancio, del limite, talvolta "
            "della fine (si pensi alla sera del primo giorno della creazione, o al \"si fa sera\" dei "
            "discepoli di Emmaus). Leggerla come immagine di un compimento — non necessariamente la "
            "morte, ma ogni forma di conclusione di una tappa — aiuta a capire perché i discepoli, "
            "proprio in quel momento, si sentano lasciati soli: non perché Dio si sia allontanato, ma "
            "perché la sua presenza, in quella fase, non è più quella rassicurante e visibile a cui "
            "erano abituati."
        ),
    },
    3: {
        "title": "La tempesta, il mare del caos",
        "text": (
            "Per la mentalità biblica il mare non è mai neutro: è la figura stessa del caos che "
            "precede e minaccia l'ordine della creazione. Genesi 1 si apre con lo Spirito di Dio che "
            "aleggia sulle acque informi; il diluvio è il ritorno di quelle stesse acque a inghiottire "
            "la terra; l'attraversamento del Mar Rosso, che i cristiani leggono come figura del "
            "Battesimo e della Pasqua, è precisamente il passaggio attraverso ciò che dà la morte verso "
            "una vita nuova. Il Salmo 104 canta che Dio ha fissato all'acqua \"un limite che non "
            "oltrepasserà\", e nel libro di Giobbe il Signore stesso ricorda: \"Fin qui giungerai e non "
            "oltre, qui si infrangerà l'orgoglio delle tue onde\" (Gb 38,11). La tempesta della barca, "
            "allora, non è meteorologia: è il riemergere di quella minaccia primordiale proprio nel "
            "momento in cui i discepoli sono soli, senza la presenza visibile di Gesù. Ogni prova che "
            "sembra rimettere in discussione l'ordine faticosamente costruito della propria vita "
            "attinge, in fondo, alla stessa immagine — ed è per questo che la vittoria su di essa non è "
            "mai solo psicologica, ma ha sempre il sapore di una piccola Pasqua."
        ),
    },
    4: {
        "title": "Camminare sul mare — il dominio messianico",
        "text": (
            "In tutte le mitologie del Vicino Oriente antico un dio doma il mare in una lotta titanica: "
            "Marduk contro Tiamat a Babilonia, Baal contro Yam a Ugarit. La Bibbia conosce questo "
            "immaginario ma lo trasforma radicalmente: il Dio d'Israele non combatte il mare da pari a "
            "pari, lo doma con la semplice potenza della sua parola. Giobbe 9,8 dice di Dio: \"da solo "
            "distende i cieli e cammina sulle onde del mare\" — un'affermazione che nella tradizione "
            "ebraica è riservata esclusivamente a Dio. Quando Matteo racconta che Gesù cammina sul "
            "mare, non sta descrivendo un prodigio fine a se stesso: sta affermando, con il linguaggio "
            "denso di simboli della Scrittura, che in quell'uomo si manifesta la stessa signoria di Dio "
            "sul caos. È un segno messianico preciso, leggibile solo da chi conosce già quella "
            "grammatica biblica — ed è proprio per questo che i discepoli, presi dalla paura, non "
            "riescono a decifrarlo e scambiano il segno più alto per il suo opposto, un fantasma."
        ),
    },
    5: {
        "title": "Lo scambio di persona — «è un fantasma»",
        "text": (
            "Il fraintendimento dei discepoli non è ingenuità, ma un caso particolare di un fenomeno "
            "che la Scrittura registra più volte: il Risorto, o il divino che si manifesta in modo "
            "inedito, viene scambiato per altro perché non corrisponde all'immagine che ci si era fatti "
            "in anticipo. Accadrà identico ai discepoli di Emmaus, che camminano per ore accanto a "
            "Gesù senza riconoscerlo (Lc 24,13-35), e agli apostoli riuniti nel cenacolo, che alla sua "
            "apparizione pensano anch'essi di vedere \"uno spirito\" (Lc 24,37). Il punto teologico è "
            "che la fede non è potenziamento della vista, ma un organo diverso di conoscenza: si "
            "riconosce Dio non guardando meglio, ma lasciandosi ricalibrare da Lui. Questo apre anche "
            "al tema degli idoli: se ci si è già fatti un'idea fissa di come Dio debba manifestarsi, "
            "tutto ciò che non corrisponde a quell'attesa — compreso Dio stesso quando agisce in modo "
            "libero — viene respinto come minaccia. È la radice di ogni idolatria: non l'assenza di "
            "fede, ma una fede già chiusa in un'immagine troppo piccola."
        ),
    },
    6: {
        "title": "«Sono io» — il Nome che rassicura",
        "vedi_anche": ["bakhita"],
        "text": (
            "L'espressione greca ἐγώ εἰμι (egō eimi), \"io sono\", tradotta qui con \"sono io\", è "
            "esattamente la formula con cui la versione greca dei Settanta rende il Nome che Dio "
            "rivela a Mosè dal roveto: \"Io sono colui che sono\" (Es 3,14). Matteo non la usa per "
            "caso: la stessa identica scena — Gesù che cammina sul mare e pronuncia questa formula — "
            "compare anche in Giovanni 6,20, e nel racconto della passione Gesù la userà di nuovo "
            "davanti a chi viene ad arrestarlo, con un effetto che fa cadere a terra le guardie (Gv "
            "18,5-6). Non è dunque un semplice \"sono io, non un fantasma\": è un'auto-rivelazione "
            "divina nel cuore della tempesta. Per questo la chiave del \"non abbiate paura\" non è una "
            "rassicurazione psicologica — non è detto che il pericolo scompaia — ma la certezza che "
            "Colui che si rivela come \"Colui che è\" è presente proprio lì, in mezzo a ciò che minaccia "
            "di travolgere. La fede non consiste nel credere che la tempesta non ci sia, ma nel "
            "riconoscere chi cammina dentro di essa."
        ),
    },
    7: {
        "title": "Lo slancio di Pietro — «Vieni!»",
        "vedi_anche": ["bakhita", "francesco"],
        "text": (
            "Solo Matteo, tra i quattro evangelisti, racconta l'episodio di Pietro che chiede di "
            "camminare sulle acque: un dettaglio che porta la firma tipica di questo Vangelo, sempre "
            "attento alla figura di Pietro come modello (spesso imperfetto, ma autentico) del "
            "discepolo. La richiesta di Pietro — \"comandami di venire\" — non è presunzione, ma "
            "un'intuizione teologica precisa: sa che da solo non potrebbe mai camminare sull'acqua, e "
            "per questo chiede un comando, cioè si affida interamente alla parola di Gesù come unica "
            "base possibile. \"Vieni\" è la stessa parola-chiamata con cui Gesù aveva reclutato i primi "
            "discepoli sul lago (Mt 4,19-22): qui diventa l'invito a un secondo livello di sequela, non "
            "più solo lasciare le reti ma affidare il proprio corpo, letteralmente, a una parola priva "
            "di ogni garanzia sensibile. È il cuore della fede teologale: non un sentimento di fiducia "
            "generico, ma la disponibilità a fare un passo che la sola ragione o i soli sensi non "
            "giustificherebbero mai."
        ),
    },
    8: {
        "title": "Il vento forte, la paura",
        "text": (
            "Il versetto chiave dell'intero episodio è il 29: \"mentre camminava verso Gesù\" — cioè "
            "finché lo sguardo di Pietro resta fisso su di Lui, l'acqua lo sostiene. Il verso "
            "successivo registra il cambiamento: \"vedendo che il vento era forte\", Pietro sposta lo "
            "sguardo, e comincia ad affondare. La fede teologale, insegna la tradizione spirituale "
            "cristiana, non è un atto isolato ma un orientamento abituale del cuore: si può credere "
            "sinceramente e, un istante dopo, lasciare che l'attenzione scivoli sull'ostacolo invece "
            "che sulla promessa. Il Salmo 18 descrive in immagini quasi identiche l'esperienza di chi "
            "si sente inghiottito da \"flutti di morte\" e \"torrenti infernali\": è la stessa "
            "grammatica della paura che riconosce nell'acqua un potere più grande di sé. La Lettera "
            "agli Ebrei suggerisce l'antidoto esatto a questa dinamica: tenere \"fisso lo sguardo su "
            "Gesù\" (Eb 12,2) — non perché il vento smetta di soffiare, ma perché è lo sguardo, non "
            "l'assenza di vento, a decidere se si affonda o si cammina."
        ),
    },
    9: {
        "title": "«Perché hai dubitato?»",
        "text": (
            "Gesù non rimprovera a Pietro l'assenza di fede, ma il dubbio: sono due cose distinte. Il "
            "fatto che Pietro sia riuscito a fare alcuni passi sull'acqua dimostra che la sua fede era "
            "reale e operante; il dubbio è ciò che interviene dopo, quando la fiducia iniziale viene "
            "eroso dal confronto con la difficoltà concreta. La Lettera di Giacomo lo descrive con "
            "un'immagine che sembra scritta apposta per questa scena: chi dubita \"è simile a un'onda "
            "del mare, agitata dal vento e spinta qua e là\" (Gc 1,6) — la stessa onda che sta facendo "
            "affondare Pietro. La domanda di Gesù, \"perché hai dubitato?\", non è retorica ma "
            "pedagogica: invita a guardare indietro, a ricordare. È lo stesso movimento che la Bibbia "
            "chiede continuamente a Israele — \"ricordati del cammino\" (Dt 8,2) — perché la memoria "
            "di ciò che Dio ha già fatto è, molto concretamente, il fondamento su cui si può continuare "
            "a camminare quando la vista non basta più."
        ),
    },
    10: {
        "title": "La barca, la comunità, la confessione finale",
        "text": (
            "Nell'arte cristiana più antica, ancora prima della croce, il simbolo più diffuso per la "
            "Chiesa è proprio la barca: lo si trova già nelle catacombe. Che il racconto si chiuda con "
            "tutti — non solo Pietro — dentro la stessa barca, in pace, dopo che il vento è cessato, "
            "non è un semplice ritorno alla normalità: è un'immagine ecclesiale. La comunità dei "
            "discepoli, fragile e reale, è il luogo dove la presenza di Cristo viene accolta e "
            "riconosciuta insieme, non conquistata da soli. Il gesto di \"prostrarsi\" (proskynesis nel "
            "testo greco) è lo stesso verbo che Matteo userà per i Magi davanti al Bambino (Mt 2,11) e "
            "per le donne davanti al Risorto (Mt 28,9): è il gesto dell'adorazione, riservato solo a "
            "Dio. E la confessione \"Davvero tu sei Figlio di Dio\" anticipa, quasi alla lettera, sia la "
            "professione di fede di Pietro a Cesarea di Filippi (Mt 16,16) sia quella del centurione "
            "pagano ai piedi della croce (Mt 27,54): Matteo costruisce così, con questi tre episodi, "
            "un filo che attraversa tutto il suo Vangelo."
        ),
    },
}


# ---------------------------------------------------------------------------
# Santi
# ---------------------------------------------------------------------------
SAINTS = [
    {
        "slug": "bakhita",
        "name": "Santa Giuseppina Bakhita",
        "dates": "1869 ca. – 1947",
        "theme": "Il guado dalla paura alla libertà",
        "link_phrases": [
            ("«Vieni!»", 7),
            ("«sono io che vi pongo nella prova della fede»", 6),
        ],
        "episode": (
            "Rapita bambina in Darfur e venduta cinque volte come schiava, Bakhita subì per anni "
            "torture e umiliazioni — tra cui un rituale di scarificazione con sale e farina "
            "strofinati sulle ferite. Giunta in Italia al servizio della famiglia Michieli, fu "
            "affidata alle suore Canossiane di Venezia come catecumena. Quando i Michieli tornarono "
            "dall'Africa per riprenderla, Bakhita rifiutò con determinazione: il Cardinale Patriarca "
            "di Venezia, Domenico Agostini, fece valere che la schiavitù non era riconosciuta dalla "
            "legge italiana. Il 29 novembre 1889 fu dichiarata legalmente libera; il 9 gennaio 1890 "
            "ricevette il battesimo, prendendo il nome di Giuseppina. Le è attribuita questa frase sui "
            "suoi aguzzini: se li avesse incontrati di nuovo, si sarebbe inginocchiata a baciar loro le "
            "mani, perché senza quel dolore non sarebbe diventata cristiana e religiosa."
        ),
        "connection": (
            "Un attraversamento reale, non simbolico — dalla schiavitù e dal terrore alla libertà e "
            "alla fiducia — scelto con coraggio in un momento preciso, un vero e proprio «Vieni!» "
            "a cui Bakhita risponde scendendo dalla sua barca. E la sua rilettura della sofferenza "
            "passata, come luogo dove Dio si è fatto incontrare, è un'eco esatta di «sono io che vi "
            "pongo nella prova della fede»."
        ),
        "source": "causesanti.va/it/santi-e-beati/giuseppina-bakhita.html; fonti storiche incrociate su più siti indipendenti per i dettagli del 1889 (non presenti nella scheda ufficiale).",
    },
    {
        "slug": "francesco",
        "name": "San Francesco d'Assisi",
        "dates": "1181/82 – 1226",
        "theme": "Una chiamata che arriva nella rovina",
        "link_phrases": [
            ("«Vieni!»", 7),
        ],
        "episode": (
            "Verso il 1205, nella chiesetta diroccata di San Damiano, Francesco — ancora immerso nella "
            "vita mondana — sente il Crocifisso animarsi e dirgli tre volte: «Va', Francesco, e ripara "
            "la mia Chiesa in rovina». Comprende alla lettera l'invito e comincia a restaurare quella "
            "chiesetta con le proprie mani; solo più tardi capirà che quella rovina era simbolo di una "
            "crisi più profonda, quella della Chiesa del suo tempo. Poco dopo, davanti al Vescovo di "
            "Assisi e a suo padre Bernardone, Francesco si spoglia pubblicamente dei suoi abiti, "
            "rinunciando all'eredità paterna: non ha più nulla, se non la vita che Dio stesso gli ha "
            "donato."
        ),
        "connection": (
            "La chiamata arriva non in un momento di forza ma di rovina — come Gesù raggiunge i "
            "discepoli nel cuore della tempesta, non dopo che è passata. Francesco risponde "
            "spogliandosi di tutto: un attraversamento concreto dalla sicurezza alla fiducia nuda, "
            "lo stesso gesto di Pietro che scende dalla barca. Il «Va'» rivolto a Francesco è dello "
            "stesso tipo del «Vieni!» rivolto a Pietro: una chiamata che precede la comprensione."
        ),
        "source": "Benedetto XVI, Catechesi sugli Apostoli, i Padri della Chiesa, gli Scrittori e i Santi — mercoledì 27 gennaio 2010, «San Francesco d'Assisi» (05_Libri/Santi e Testimonianze/).",
    },
]

if __name__ == "__main__":
    for slug in ["rosini", "armellini", "curtaz", "lectio"]:
        seq = author_sequence(slug)
        print(slug, "->", len(seq), "glosse")
