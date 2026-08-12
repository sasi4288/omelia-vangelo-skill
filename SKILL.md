---
name: omelia-vangelo-4-fonti
description: Genera il PDF del Vangelo del giorno (domenica o feriale/solennità) con glosse da fonti fisse — 5 per la domenica (Rosini, Armellini, Curtaz, Epicoco, Lectio unificata), 3 per l'infrasettimanale (Epicoco, Curtaz, Lectio unificata) — dimensionato per Viwoods AiPaper. Usare quando Salvatore chiede di preparare questo apparato per un'omelia, o per il rinnovo periodico del documento.
---

# Omelia — Vangelo con apparato a più fonti

Genera un PDF di studio per la preparazione di un'omelia: il Vangelo del giorno con le
glosse di più commentatori affiancate, organizzate per farne emergere il pensiero di
ciascuno, i concetti ricorrenti tra le fonti, possibili fili logici di predicazione, un
episodio di vita di uno o più santi collegato ai temi del brano, e approfondimenti
teologici estesi — il tutto navigabile con link ipertestuali interni e dimensionato
esattamente per lo schermo dell'e-reader Viwoods AiPaper di Salvatore.

Il documento **non è un unico foglio**: è un fascicolo multi-pagina strutturato così,
in quest'ordine:
1. Una pagina (o più, se il contenuto non ci sta) per ciascuna fonte: il Vangelo intero
   a sinistra (con le frasi commentate in **grassetto e link**), le glosse di quella sola
   fonte a destra, in ordine, collegate da brevi connettori logici — leggibili in fila
   come il ragionamento continuo di quell'autore
2. Una pagina "Concetti ricorrenti": temi su cui più fonti convergono, punti di vista
   affiancati
3. Una pagina "Sintesi — fili logici": 3-4 percorsi che ricombinano gli ancoraggi tra le
   fonti in possibili tracce di predicazione
4. Una pagina per ciascun santo scelto, con un episodio di vita e il collegamento
   esplicito al Vangelo (link a/da gli approfondimenti pertinenti)
5. Una sezione finale "Approfondimenti": una voce per ciascun ancoraggio usato nel
   documento, spiegazione biblico-teologica più estesa, con indice e link di ritorno sia
   al Vangelo (per ciascuna fonte) sia ai santi collegati

## Quando si attiva

- **Domenica**: le fonti sono pronte con un margine di alcuni giorni (Rosini ~5gg prima,
  Armellini anche 2-3 settimane prima, Curtaz-video ~3gg prima — quest'ultimo è il collo
  di bottiglia). Il giovedì precedente è un buon momento per generare il documento della
  domenica successiva.
- **Feriale o solennità infrasettimanale** (es. Assunta): Curtaz (sito) ed Epicoco
  pubblicano il commento solo ~1 giorno prima — **non generare con largo anticipo**, va
  fatto a ridosso della data (sera prima o mattina stessa). cristomaestro.it invece non
  ha questo vincolo (vedi sotto).
- Se una fonte non è ancora disponibile quando si prova a generare, segnalarlo a
  Salvatore invece di procedere con un apparato incompleto senza avvisare.

## Le fonti e come recuperarle

**Domenica (5 fonti):**
| Fonte | Come recuperarla |
|---|---|
| don Fabio Rosini | Video YouTube (cercare "don Fabio Rosini commento vangelo" + data, canale "Alzo gli Occhi verso il Cielo" o simili) |
| P. Fernando Armellini | Video YouTube (cercare "Armellini commento al vangelo" + data) |
| Paolo Curtaz | Video YouTube (cercare "Paolo Curtaz commento al vangelo" + data) |
| don Luigi Maria Epicoco | https://www.cercoiltuovolto.it/tag/don-luigi-maria-epicoco/ (sito, stesso URL dell'infrasettimanale — pubblica anche per la domenica) |
| Lectio unificata | cristomaestro.it, vedi sotto |

**Nota sui tempi di pubblicazione di Epicoco:** a differenza di Rosini/Armellini (che escono con giorni di anticipo), Epicoco pubblica a ridosso della data — anche per la domenica può non essere ancora online se si genera il documento il giovedì precedente. Non è un errore: trattarlo come le altre fonti video, provare a recuperarlo e procedere comunque se manca, senza che la sua assenza da sola blocchi la generazione (vedi soglia sotto).

**Infrasettimanale (3 fonti):**
| Fonte | Come recuperarla |
|---|---|
| don Luigi Maria Epicoco | https://www.cercoiltuovolto.it/tag/don-luigi-maria-epicoco/ |
| Paolo Curtaz | https://paolocurtaz.it/commenti/vangelo-del-giorno/ (NON il video, il sito) |
| Lectio unificata | cristomaestro.it, vedi sotto |

**cristomaestro.it — note tecniche importanti:**
- Provare prima **HTTPS**: in ambiente cloud (routine) risponde normalmente in 1-2
  secondi, nessun timeout osservato. Solo se HTTPS va sistematicamente in timeout
  (capitato in alcuni ambienti di lavoro locali, sia con WebFetch che con curl diretto)
  ripiegare su **HTTP** (`curl http://www.cristomaestro.it/...`), che finora ha sempre
  funzionato come fallback. Non escludere un metodo a priori: provare quello più veloce
  e passare all'altro solo se necessario.
- Le pagine di navigazione interattiva (`/rito-romano/AAAA-MM-GG`, `/calendario-liturgico`)
  sembrano funzionare solo per la domenica "corrente" — non affidarsi a queste per
  trovare il file.
- L'**archivio PDF vero e proprio è statico e sempre disponibile**, organizzato per nome
  non per data:
  - Domeniche: `files/Esegesi/Domeniche rito Romano/Anno {A|B|C}/[Nome Domenica].pdf`
  - Feste/solennità: `files/Esegesi/Feste e solennita romano/[data] - [Nome Festa]...pdf`
    (es. confermato: `10 agosto - San Lorenzo.pdf`)
  - Bisogna indovinare/verificare il nome esatto del file (spazi, virgole, "Anno X"):
    provare prima a dedurlo dal pattern, poi verificare con una richiesta HTTP diretta.
  - **L'archivio copre SOLO Domeniche e Feste/Solennità.** Per le memorie feriali
    (es. Santa Chiara, 11 agosto) e le ferie semplici **non esiste alcun file** — non è
    un errore né un problema temporaneo, è strutturale. Per questi giorni la Lectio
    unificata va considerata una fonte assente per definizione, non una fonte "non
    ancora pubblicata": non bloccare/segnalare la sua assenza in questi casi, procedere
    con le fonti infrasettimanali disponibili (vedi condizione di stop più sotto).

**Paolo Curtaz (sito, paolocurtaz.it) — limite noto:** il sito è protetto da un captcha
SiteGround che blocca sistematicamente l'IP dell'ambiente cloud (confermato su più run:
fetch diretto, WebFetch, feed RSS, reader proxy e Wayback Machine tutti bloccati — solo
la homepage in cache passa a volte). Non è un problema di rete generale né va aggirato
(niente tentativi di bypass di captcha/WAF). Trattarlo come fonte irraggiungibile per
quel run: un paio di tentativi standard (fetch diretto + WebFetch) sono sufficienti,
poi procedere senza, contandola come fonte mancante ai fini della condizione di stop.

**Estrazione dai video YouTube:**
1. `yt-dlp` è installato; usare `--extractor-args "youtube:player_client=android"` per
   evitare i blocchi PO-token.
2. Scaricare i sottotitoli italiani (spesso solo automatici):
   `yt-dlp --skip-download --write-auto-sub --sub-lang it --sub-format vtt --extractor-args "youtube:player_client=android" -o "nome" "URL"`
3. Se un video non ha sottotitoli disponibili, cercare un altro canale/video che tratti
   lo stesso commento dello stesso autore per lo stesso giorno (è già capitato) prima di
   ricorrere alla trascrizione con Whisper (installabile via `pip3 install openai-whisper`,
   lento: preferire sempre i sottotitoli se esistono).
4. **Pulire il VTT** (i sottotitoli automatici sono "a scorrimento", ogni blocco ripete
   parte del precedente): script di deduplica per prefisso comune riga per riga —
   vedere lo storico di questa conversazione per l'algoritmo esatto, oppure
   ricostruirlo: per ogni blocco di testo, trovare il prefisso di parole in comune col
   blocco precedente e aggiungere solo le parole nuove.

## Il santo — indice riusabile, non ripartire da zero

**Consultare sempre per primo `Indice_Santi_per_Tema.md` in questo stesso repository**
(copia sincronizzata di `03_Formazione_e_Studio/Indice_Santi_per_Tema.md` sul workspace
locale dell'utente — quella locale è la fonte "madre", questa nel repo è quella
raggiungibile anche dagli agenti cloud, che non hanno alcun accesso al Mac dell'utente).
È un indice di episodi di santi già ricercati e verificati, taggato per tema. Se un
tema del Vangelo del giorno corrisponde a un tag già presente, riusare quell'episodio.

**Regola non negoziabile, in questo file e in quello sincronizzato:** il campo
"Episodio" di ogni voce contiene SEMPRE il racconto per intero in prosa, mai un rimando
a un libro/file esterno — un agente cloud non può aprire `05_Libri/...` sul Mac
dell'utente, quindi un rimando lì per lui equivale a non avere nulla.

Se nessun tema corrisponde, cercare una fonte nuova, in quest'ordine:
1. `05_Libri/Santi e Testimonianze/Catechesi sugli Apostoli, i Padri della Chiesa, gli
   Scrittori e i Santi (Benedetto XVI).pdf` — 661 pagine, leggibile direttamente, copre
   Apostoli/Padri della Chiesa/santi fino a inizio '900. Solo se si lavora in locale con
   accesso al workspace: un agente cloud non ha questo file, salta direttamente al
   punto 2. Cercare con `pdftotext -layout file.pdf - | grep -i "nome"` invece di
   rileggere tutto.
2. causesanti.va (raggiungibile via HTTPS normale) per verificare date/dati ufficiali —
   le sue schede biografiche sono spesso troppo sintetiche come fonte narrativa primaria.
3. Ricerca web incrociata su più fonti indipendenti per i dettagli d'episodio.

**Dopo aver trovato un episodio nuovo, scrivere la voce per intero (racconto completo,
non un rimando) in ENTRAMBE le copie** se si sta lavorando in locale con accesso a
tutto il workspace; un agente cloud aggiorna solo la copia nel repository (e la fa
confluire nel repo con un commit), lasciando che l'utente o una sessione locale
successiva la riporti anche nella copia "madre" sul Mac. Stesso formato delle voci
esistenti: Temi, Episodio, Collegamento possibile, Fonte, Usato in.

## Procedimento

1. **Determinare il giorno liturgico target** (di norma la prossima domenica; oppure la
   data specifica richiesta) e se è domenica o feriale/solennità — questo determina
   quale set di fonti usare.
2. **Recuperare il Vangelo del giorno** (testo CEI) e le 3-5 fonti come sopra.
3. **Segmentare il Vangelo** in `GOSPEL_SEGMENTS` (vedi `templates/build_apparato_template.py`):
   ogni voce è `(testo_prima, frase_ancorata, testo_dopo, numero_ancora, marcatore_scrittura_o_None)`.
   La `frase_ancorata` è quella che verrà messa in grassetto e collegata: sceglierla in
   corrispondenza dei punti su cui almeno una fonte fa un'osservazione specifica.
4. **Costruire `ANCHORS`**: un blocco per ogni numero di ancora, con la lista delle fonti
   che commentano quel punto — `(slug, lettera, nome, tesi_breve, corpo)`. Non tutte le
   fonti devono comparire su ogni ancoraggio: solo quelle che dicono davvero qualcosa di
   specifico su quel punto (è normale avere 2-4 fonti per ancoraggio, mai forzare).
5. **Scrivere i connettori** (`CONNECTORS` in `build_document_template.py`): per ogni
   fonte, una frase brevissima che lega la glossa precedente alla successiva, in modo che
   leggendo in fila le glosse di un solo autore si ricostruisca il suo ragionamento.
6. **Identificare i concetti ricorrenti** (`CONCEPTS`): 3-5 temi su cui almeno 3 fonti
   convergono, con il punto di vista di ciascuna.
7. **Costruire i fili logici** (`THREADS`): 3-4 percorsi che attraversano ancoraggi
   diversi, mescolando le fonti, con un titolo e una frase di sintesi ciascuno — sono
   proposte di traccia per l'omelia, non l'omelia già scritta.
8. **Scegliere il/i santo/i** (`SAINTS`) — vedi sezione sopra — e collegarli agli
   ancoraggi pertinenti tramite `link_phrases` (frasi nel testo "connection" da
   trasformare in link) e aggiungere `"vedi_anche"` nell'approfondimento corrispondente.
9. **Scrivere gli approfondimenti** (`APPROFONDIMENTI`): uno per ogni numero di ancora,
   150-220 parole, contesto biblico/teologico più esteso di quanto stia nelle glosse
   brevi — etimologie, sfondo storico-religioso, rimandi scritturistici ulteriori. Attingere
   al materiale già raccolto dalle fonti più conoscenza teologica generale (verificata),
   cercando altrove solo se manca qualcosa di specifico.
10. **Aggiornare i metadati** in testa a `build_document_template.py`: `GOSPEL_REF`,
    `LITURGICAL_LABEL`, `DOC_TITLE`, `SOURCE_ORDER`, `FOOTER_CREDITS`.
11. **Copiare i tre file** (`build_apparato_template.py` → `build_apparato.py`,
    `build_document_template.py` → `build_document.py`, `render_document.py` invariato)
    in una cartella di lavoro, con i dati di questa settimana.
12. **Generare**: `python3 render_document.py` produce l'HTML, poi
    `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" --print-to-pdf-no-header "file://$(pwd)/vangelo_documento_finale.html"`.
13. **Verificare prima di consegnare**:
    - Numero di pagine ragionevole (nessuna pagina anomala: controllare le dimensioni dei
      PNG resi con `pdftoppm -png -r 130` — una pagina sospettosamente piccola in byte è
      quasi sempre una pagina vuota/rotta)
    - Nessun margine mancante sulle pagine di continuazione
    - Link interni funzionanti: `python3 -c "import pypdf; r=pypdf.PdfReader('output.pdf'); print(sum(1 for p in r.pages for a in (p.get('/Annots') or []) if a.get_object().get('/Subtype')=='/Link'))"`
      deve dare un numero sostanzialmente maggiore di zero (per il caso a 4 fonti/10
      ancoraggi il numero di riferimento era 194)
    - Ispezionare visivamente almeno la prima pagina di ogni sezione con il tool Read
14. **Salvare** in `01_Parrocchia_e_Ministero/Omelie/` con nome
    `Vangelo_[riferimento breve]_[Nome Domenica o Festa]_AiPaper.pdf`.
15. **Aprire per la revisione** con
    `"/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" "percorso/file.pdf"`
    (l'estensione `tomoki1207.pdf` gestisce l'anteprima) — il link cliccabile in chat da
    solo NON apre l'anteprima corretta, va sempre usato questo comando.

## Consegna e archiviazione (run automatici in cloud)

Le routine cloud (non l'uso locale) consegnano così:
- **Unico canale, sempre**: invio del PDF via Telegram Bot API — è il solo canale
  verificato affidabile e va sempre tentato. È anche l'unico archivio di fatto (il PDF
  resta scaricabile dalla chat).
- **Google Drive: abbandonato.** Il connettore MCP disponibile richiede il contenuto
  inline in base64 con un tetto di ~256KB — i PDF di questo documento (tipicamente
  180-250KB già compressi) lo superano quasi sempre. Non tentare l'upload su Drive.
- **GitHub push: abbandonato (per ora).** Anche con un Personal Access Token valido
  (verificato con permesso di scrittura reale via chiamata diretta all'API GitHub), il
  push da un ambiente cloud Claude Code fallisce con 403: il proxy dell'ambiente
  gestisce/sovrascrive l'autenticazione verso github.com e richiede che un admin
  colleghi la "Claude GitHub App" a livello di organizzazione — un meccanismo separato
  dai permessi del token, per cui non abbiamo trovato un percorso self-service. Non
  tentare più il push nei run cloud finché questo non viene sbloccato lato Anthropic/
  account. Se in futuro si vuole riprovare, verificare prima se è comparsa una gestione
  esplicita della GitHub App per le routine in claude.ai/code.

## Specifiche tecniche fisse (non richiedono conferma ogni volta)

- **Pagina**: 162.56 × 216.75 mm (Viwoods AiPaper 10.65", 1920×2560px @300ppi),
  `@page { size: 162.56mm 216.75mm; margin: 0; }`, padding interno 15mm sopra/sotto,
  9.5mm ai lati.
- **Stile**: scala di grigi (l'utente legge su e-reader) — MAI usare sfumature di grigio
  diverse per distinguere le fonti (troppo sottili, spariscono su e-ink). Le fonti si
  distinguono con un bollino a iniziale (R/A/C/L/E) + stile del bordo (continuo /
  tratteggiato / punteggiato / doppio) come doppia codifica.
- **Tipografia**: una sola scala per tutto il documento (variabili CSS `--fs-h1`,
  `--fs-h2`, `--fs-thesis`, `--fs-body`, `--fs-caption`) — non introdurre dimensioni
  diverse per le stesse categorie di testo in punti diversi del documento.
- **Paginazione**: mai affidarsi solo all'overflow automatico del browser per contenuti
  lunghi (perde il padding superiore sulla pagina di continuazione e può generare pagine
  vuote) — per le pagine-autore si usa un calcolo esplicito di quante righe entrano per
  pagina (`paginate_rows` in `render_document.py`); per le altre sezioni più corte basta
  `box-decoration-break: clone` + `break-inside: avoid` sui blocchi.

## File del progetto

- `templates/build_apparato_template.py` — struttura dati del Vangelo segmentato e degli
  ancoraggi (da rigenerare ogni volta)
- `templates/build_document_template.py` — metadati, connettori, concetti, fili logici,
  santi, approfondimenti (da rigenerare ogni volta)
- `templates/render_document.py` — motore di rendering/CSS/paginazione, generico, non
  richiede modifiche da una settimana all'altra
- `../../.claude/../03_Formazione_e_Studio/Indice_Santi_per_Tema.md` (relativo alla
  radice del workspace) — indice riusabile degli episodi di santi

## Cosa chiedere a Salvatore (se non specificato)

- Per quale domenica/giorno generare (default: la prossima domenica)
- Se per un giorno feriale/solennità, conferma che le fonti infrasettimanali abbiano già
  pubblicato il contenuto (altrimenti avvisare che è troppo presto, non generare un
  apparato incompleto)
- Se un santo scelto non è ovvio dal tema del Vangelo, proporre 2-3 candidati invece di
  sceglierne uno arbitrariamente

## Condizione di stop (quando fermarsi e avvisare invece di generare)

Non generare mai un apparato con fonti mancanti senza avvisare — ma cosa conta come
"mancante" dipende dal rango liturgico del giorno:

- **Domenica, festa o solennità**: fermarsi e avvisare se manca la Lectio unificata
  OPPURE se mancano entrambe le altre fonti previste (per la domenica: Rosini+Armellini,
  Curtaz, o combinazioni — vedi sopra; per festa/solennità infrasettimanale: Epicoco e
  Curtaz). Per questi giorni la Lectio esiste sempre nell'archivio, quindi la sua
  assenza segnala quasi certamente che non è ancora stata pubblicata (non un limite
  strutturale) ed è corretto trattarla come blocco.
- **Memoria feriale o feria semplice**: la Lectio unificata è strutturalmente assente
  dall'archivio (vedi sopra) — la sua mancanza NON è una condizione di stop. Fermarsi e
  avvisare solo se mancano ENTRAMBE Epicoco e Curtaz. Se è disponibile anche solo una
  delle due, procedere con quella (più la Lectio se per caso esistesse).
