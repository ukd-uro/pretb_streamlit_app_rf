# Prätherapeutisches Tumorboard für Prostatakarzinompatienten

Dieser Algorithmus dient der automatischen Generierung von Empfehlungen für das prätherapeutische Tumorboard.
Es handelt sich hierbei um Patienten mit einem histologisch gesicherten Prostatakarzinom, wo die weitergehende Diagnostik und Therapie multidisziplinär besprochen werden soll.

Das Modell basiert auf einem multivariablen Random Forest mit einem multilabel Ausgang mit den Inputvariablen Alter, PSA, DRU (Digital Rektale Untersuchung), Gleason-Score, Anzahl positiver Stanzen, Gesamtzahl der Stanzen
und den Outputvariablen CT, Knochenszintigraphie, PSMA-PET, Aktive Überwachung, radikale Prostatektomie und Strahlentherapie. Die Outcomevariablen werden nach der Prädiktion in den entsprechenden Empfehlungstext konvertiert.

Die App benutzt das Streamlit Framework als Frontend und läuft als Server über die [Streamlit Community Cloud](https://pretbappapprf-jrjlsn4igt49nrtd3xy3pd.streamlit.app/).


> [!Warning]
> Es handelt sich um ein Projekt in Entwicklung ohne entsprechende Zulassung und ist daher nur für den experimentellen Einsatz geeignet.
