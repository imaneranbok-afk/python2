donnees = [
    ("Sara", "Math", 12, "G1"),
    ("Sara", "Info", 14, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"),
    ("Sara", "Math", 11, "G1"),
    ("Bouchra", "Info", "abc", "G2"),
    ("", "Math", 10, "G1"),
    ("Yassine", "Info", 22, "G2"),
    ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"),
    ("Sara", "Chimie", 16, "G1"),
    ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"),
    ("Hana", "Physique", 15, "G3"),
    ("Hana", "Math", 8, "G3"),
]

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not nom or not matiere or not groupe:
        return (False, "champ vide")
    try:
        note = float(note)
    except:
        return (False, "note invalide")
    if note < 0 or note > 20:
        return (False, "note inacceptable")
    return (True, "")

valides = []
erreurs = []
doublons_exact = set()
vus = set()

for enr in donnees:
    if enr in vus:
        doublons_exact.add(enr)
    else:
        vus.add(enr)
    ok, raison = valider(enr)
    if ok:
        nom, matiere, note, groupe = enr
        valides.append((nom, matiere, float(note), groupe))
    else:
        erreurs.append({"ligne": enr, "raison": raison})

matieres = set()
etudiants = {}
groupes = {}

for nom, matiere, note, groupe in valides:
    matieres.add(matiere)
    if nom not in etudiants:
        etudiants[nom] = {}
    if matiere not in etudiants[nom]:
        etudiants[nom][matiere] = []
    etudiants[nom][matiere].append(note)
    if groupe not in groupes:
        groupes[groupe] = set()
    groupes[groupe].add(nom)

def somme(liste):
    if not liste:
        return 0
    return liste[0] + somme(liste[1:])

def moyenne(liste):
    if not liste:
        return 0
    return somme(liste) / len(liste)

moyennes_etudiants = {}
for nom in etudiants:
    toutes_notes = []
    moyennes_matieres = {}
    for matiere in etudiants[nom]:
        notes = etudiants[nom][matiere]
        moyennes_matieres[matiere] = moyenne(notes)
        toutes_notes.extend(notes)
    moyennes_etudiants[nom] = {
        "moyenne_generale": moyenne(toutes_notes),
        "moyennes_matieres": moyennes_matieres
    }

alertes = {
    "doublons_matiere": [],
    "profil_incomplet": [],
    "groupes_faibles": [],
    "ecarts_importants": []
}

for nom in etudiants:
    for matiere in etudiants[nom]:
        if len(etudiants[nom][matiere]) > 1:
            alertes["doublons_matiere"].append((nom, matiere))
    if set(etudiants[nom].keys()) != matieres:
        alertes["profil_incomplet"].append(nom)
    notes = []
    for matiere in etudiants[nom]:
        notes.extend(etudiants[nom][matiere])
    if notes:
        if max(notes) - min(notes) > 10:
            alertes["ecarts_importants"].append(nom)

seuil = 10
for groupe in groupes:
    notes_groupe = []
    for nom in groupes[groupe]:
        for matiere in etudiants[nom]:
            notes_groupe.extend(etudiants[nom][matiere])
    if moyenne(notes_groupe) < seuil:
        alertes["groupes_faibles"].append(groupe)

        print("Valides:", valides)
print("Erreurs:", erreurs)
print("Doublons exacts:", doublons_exact)
print("Moyennes:", moyennes_etudiants)
print("Alertes:", alertes)